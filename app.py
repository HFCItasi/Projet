
from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import requests
from openrouteservice import client
from geopy.distance import great_circle
import os

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.secret_key = os.urandom(24)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    preferedcity = db.Column(db.String(250), nullable=True)

with app.app_context():
    db.create_all()

@login_manager.user_loader
def loader_user(user_id):
    return db.session.get(User, user_id)

ORS_API_KEY = '5b3ce3597851110001cf62489a1301189d7947caa7f482153012f28c'
JCD_API_KEY = 'b0dfc23d24bc58c11f5aecfc5e67c48749e12292'
ors = client.Client(key=ORS_API_KEY)

@app.route('/')
@login_required
def home():
    city = current_user.preferedcity if current_user.is_authenticated else 'Lyon'
    return render_template('index.html', city=city)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        city = request.form.get('preferedcity', 'Lyon')

        if not username or not password:
            flash("Tous les champs sont requis.")
            return redirect(url_for('register'))

        if User.query.filter_by(username=username).first():
            flash('Nom d’utilisateur déjà pris.')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, password=hashed_password, preferedcity=city)
        db.session.add(new_user)
        db.session.commit()
        flash('Compte créé avec succès. Connectez-vous maintenant.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Identifiants incorrects')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/getBikesAround', methods=['GET'])
def get_bikes():
    city = request.args.get('city', 'Lyon')
    url = f'https://api.jcdecaux.com/vls/v1/stations?contract={city}&apiKey={JCD_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        stations = response.json()
        usable_stations = [s for s in stations if s['status'] == 'OPEN' and (s['available_bikes'] > 0 or s['available_bike_stands'] > 0)]
        return jsonify(usable_stations)
    else:
        return jsonify({"error": "Impossible de récupérer les données"}), 500

@app.route('/getNearestStation', methods=['GET'])
def get_nearest_station():
    lat = float(request.args.get('lat'))
    lon = float(request.args.get('lon'))
    city = request.args.get('city', 'Lyon')
    return jsonify(get_nearest_station_coords(lat, lon, city))

@app.route('/getTrajectory', methods=['GET'])
def get_trajectory():
    start_coords = request.args.get('start_coords').split(',')
    end_coords = request.args.get('end_coords').split(',')
    city = request.args.get('city', 'Lyon')
    start_lat, start_lon = map(float, start_coords)
    end_lat, end_lon = map(float, end_coords)
    start_station = get_nearest_station_coords(start_lat, start_lon, city)
    end_station = get_nearest_station_coords(end_lat, end_lon, city)

    if not start_station or not end_station:
        return jsonify({"error": "Station introuvable."}), 500

    bike_start_lat, bike_start_lon = start_station['position']['lat'], start_station['position']['lng']
    bike_end_lat, bike_end_lon = end_station['position']['lat'], end_station['position']['lng']

    routes = []
    for (start, end, mode) in [
        ((start_lon, start_lat), (bike_start_lon, bike_start_lat), 'foot-walking'),
        ((bike_start_lon, bike_start_lat), (bike_end_lon, bike_end_lat), 'cycling-regular'),
        ((bike_end_lon, bike_end_lat), (end_lon, end_lat), 'foot-walking')
    ]:
        direction_params = {
            'coordinates': [start, end],
            'profile': mode,
            'format_out': 'geojson',
            'geometry': 'true'
        }
        route = ors.directions(**direction_params)
        routes.append(route)

    return jsonify({
        "routes": routes,
        "start_station_name": start_station["name"],
        "end_station_name": end_station["name"],
        "start_station_coords": start_station["position"],
        "end_station_coords": end_station["position"]
    })

def get_nearest_station_coords(lat, lon, city):
    url = f'https://api.jcdecaux.com/vls/v1/stations?contract={city}&apiKey={JCD_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        stations = response.json()
        if not stations:
            return None
        closest_station = min(stations, key=lambda s: great_circle((lat, lon), (s['position']['lat'], s['position']['lng'])).meters)
        return closest_station
    else:
        return None

if __name__ == "__main__":
    app.run(debug=True, port=5001)


@app.route('/getTrajectory', methods=['GET'])
@login_required
def get_trajectory():
    start_coords = request.args.get('start_coords').split(',')
    end_coords = request.args.get('end_coords').split(',')
    city = request.args.get('city', 'Lyon')
    start_lat, start_lon = map(float, start_coords)
    end_lat, end_lon = map(float, end_coords)
    start_station = get_nearest_station_coords(start_lat, start_lon, city)
    end_station = get_nearest_station_coords(end_lat, end_lon, city)

    if not start_station or not end_station:
        return jsonify({"error": "Station introuvable."}), 500

    bike_start_lat, bike_start_lon = start_station['position']['lat'], start_station['position']['lng']
    bike_end_lat, bike_end_lon = end_station['position']['lat'], end_station['position']['lng']

    routes = []
    for (start, end, mode) in [
        ((start_lon, start_lat), (bike_start_lon, bike_start_lat), 'foot-walking'),
        ((bike_start_lon, bike_start_lat), (bike_end_lon, bike_end_lat), 'cycling-regular'),
        ((bike_end_lon, bike_end_lat), (end_lon, end_lat), 'foot-walking')
    ]:
        direction_params = {
            'coordinates': [start, end],
            'profile': mode,
            'format_out': 'geojson',
            'geometry': 'true'
        }
        route = ors.directions(**direction_params)
        routes.append(route)

    return jsonify({
        "routes": routes,
        "start_station_name": start_station["name"],
        "end_station_name": end_station["name"],
        "start_station_coords": start_station["position"],
        "end_station_coords": end_station["position"]
    })

