import os
import pandas as pd
from sqlalchemy import create_engine, sql, text
from flask import Flask, render_template

# Fonction pour obtenir une connexion à la base de données
def get_connection(db_name):
    return create_engine(
        url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, db_name
        )
    )

# Informations de connexion à la base de données
user = 'postgres'
password = ''
host = '127.0.0.1'
port = 5434
database = 'cinema'
newdatabase = 'stations'

new_engine = get_connection(newdatabase)
nom_table = 'stations'


# Fonction pour récupérer les villes de la database 
def get_cities(engine, nom_table):
    """
    Nom table : Nom de la table de la Database contenant les stations 
    """
    query = f"""
    SELECT ville
    FROM (SELECT DISTINCT ville FROM {nom_table}) AS distinct_cities
    ORDER BY RANDOM();
    """
    with engine.connect() as conn:
        result = conn.execute(sql.text(query)).fetchall()
        cities = [row[0] for row in result]  # Utilisez row[0] au lieu de row['city']
    return cities

def get_bike_locations(engine, ville):
    """
    Récupère les coords de chaque station de vélo présente dans la ville 
    
    ville : Nom de la ville souhaitée
    """
    try:
        query = """
        SELECT name, latitude, longitude 
        FROM stations 
        WHERE ville = :ville AND latitude IS NOT NULL AND longitude IS NOT NULL;
        """
        with engine.connect() as conn:
            result = conn.execute(sql.text(query), {"ville": ville}).fetchall()
            locations = [
                {"name": row[0], "lat": row[1], "lng": row[2]} 
                for row in result
            ]
        return locations
    except Exception as ex:
        print(f"Erreur lors de la récupération des emplacements : {ex}")
        return []

def get_coord_ville(engine, ville):
    """
    Récupère les coordonnées de la ville souhaitée 
    ville : Nom de la ville   
    """
    try:
        query = "SELECT latitude, longitude FROM stations WHERE ville = :ville;"
        with engine.connect() as conn:
            result = conn.execute(sql.text(query), {"ville": ville}).fetchall()
            if result:
                lat = result[0][0]  #Récupère les coordonnées de la première station dans la database concernant la ville voulue 
                lng = result[0][1]  
                return lat, lng
            else:
                print(f"Aucune coordonnée trouvée pour la ville {ville}")
                return None, None
    except Exception as ex:
        print(f"Erreur lors de la récupération des coordonnées pour {ville}: {ex}")
        return None, None

# Verifie l'existence du repertoire templates
if not os.path.exists('templates'):
    os.makedirs('templates')


# Serveur web Flask
app = Flask(__name__, template_folder='templates') 


#Création du fichier html de la page d'accueil

chemin_accueil = 'templates/accueil.html'
if not os.path.exists(chemin_accueil):
    cities = get_cities(new_engine, nom_table)
    with open(chemin_accueil, encoding="utf-8", mode='w') as f:
        f.write(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>🚴 Vélos du Monde</title>
            <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
            <style>
                body {{
                    font-family: 'Poppins', sans-serif;
                    margin: 0;
                    padding: 0;
                    color: #f7f7f7;
                    height: 100vh;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    overflow: hidden;
                }}
                .background {{
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background: url('https://images.frandroid.com/wp-content/uploads/2024/04/velo-electrique-libre-service-lime-paris.jpg') no-repeat center center fixed;
                    background-size: cover;
                    z-index: -1;
                    filter: brightness(60%);
                }}
                .overlay {{
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background: rgba(0, 0, 0, 0.5);
                    z-index: 0;
                }}
                header {{
                    background: rgba(0, 0, 0, 0.156);
                    padding: 40px;
                    color: rgb(68, 181, 15);
                    width: 100%;
                    box-sizing: border-box;
                    position: absolute;
                    top: 0;
                    left: 0;
                    text-align: center;
                    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
                    z-index: 1;
                }}
                h1 {{
                    margin: 0;
                    font-size: 3.5rem;
                    font-weight: 600;
                }}
                h2 {{
                    margin: 10px 0;
                    font-size: 1.5rem;
                    font-weight: 400;
                }}
                main {{
                    margin-top: 150px;
                    width: 100%;
                    max-width: 1000px;
                    display: grid;
                    grid-template-columns: repeat(3, 1fr);
                    gap: 20px;
                    padding: 0 20px;
                    z-index: 1;
                }}
                .city {{
                    padding: 15px;
                    background-color: rgba(0, 0, 0, 0.8);
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(10, 182, 7, 0.701);
                    text-align: center;
                    transition: transform 0.3s ease, background-color 0.3s ease;
                }}
                .city a {{
                    color: rgb(255, 255, 255);
                    text-decoration: none;
                    font-size: 1.2rem;
                }}
                .city:hover {{
                    transform: scale(1.05);
                    background-color: rgba(0, 0, 0, 0.9);
                }}
                .city a:hover {{
                    color: #2bd700;
                }}
                .instagram-icon {{
                    position: absolute;
                    bottom: 20px;
                    right: 20px;
                    z-index: 2;
                    text-align: center;
                }}
                .instagram-icon img {{
                    width: 60px;
                    height: 60px;
                    border-radius: 50%;
                    transition: transform 0.3s ease;
                }}
                .instagram-icon img:hover {{
                    transform: scale(1.2);
                    cursor: pointer;
                }}
                .tooltip {{
                    position: absolute;
                    bottom: 80px;
                    right: 20px;
                    background: rgba(0, 0, 0, 0.8);
                    color: #ffffff;
                    padding: 10px 15px;
                    border-radius: 5px;
                    font-size: 1rem;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                    display: none;
                    z-index: 3;
                }}
            </style>
        </head>
        <body>
            <div class="background"></div>
            <div class="overlay"></div>
            <header>
                <h1>Bienvenue sur Vélos du Monde !</h1>
                <h2>Selectionnez la ville de votre choix</h2>
            </header>
            <main>
                {''.join([f'<div class="city"><a href="/ville/{city.lower()}">{city}</a></div>' for city in cities])}
            </main>
            <div class="tooltip" id="tooltip">Retrouvez les avis de Emmanuel Macron et Kylian Mbappé !</div>
            <div class="instagram-icon" 
                onmouseover="document.getElementById('tooltip').style.display = 'block';" 
                onmouseout="document.getElementById('tooltip').style.display = 'none';">
                <a href="https://www.instagram.com/velosdumonde_/" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram">
                </a>
            </div>
        </body>
        </html>
        """)
    print(f"Fichier '{chemin_accueil}' créé avec succès.")
else:
    print(f"Le fichier '{chemin_accueil}' existe déjà.")


#Création du fichier html de la page de la carte 
chemin_carte = 'templates/carte.html'
if not os.path.exists(chemin_carte):
    with open(chemin_carte, encoding="utf-8", mode='w') as f: 
        f.write("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Vélos du monde</title>
            <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
            <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.3/dist/leaflet.css" />
            <script src="https://unpkg.com/leaflet@1.9.3/dist/leaflet.js"></script>
            <style>
                html, body {
                    font-family: 'Poppins', sans-serif;
                    height: 100%;  
                    margin: 0;     
                    padding: 0;    
                }

                
                .background {
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background: url('https://images.frandroid.com/wp-content/uploads/2024/04/velo-electrique-libre-service-lime-paris.jpg') no-repeat center center fixed;
                    background-size: cover;
                    filter: brightness(50%); 
                    z-index: -1;
                }

                header {
                    background: rgba(0, 0, 0, 0.7);
                    padding: 40px;
                    color: white;
                    text-align: center;
                    position: relative;
                    z-index: 1;
                    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
                }
                h1 {
                    margin: 0;
                    font-size: 2.5rem;
                    font-weight: 600;
                }

                main {
                    display: flex;
                    justify-content: center;
                    align-items: flex-start;
                    width: 100%;
                    margin-top: 15px;  
                    flex-direction: column;
                    align-items: center; 
                }

                #map {
                    height: 500px;  
                    width: 100%;
                    max-width: 1000px;  
                    border: 2px solid #00af26;
                    border-radius: 10px;
                    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
                    z-index: 1;
                }

                button {
                    display: block;
                    font-family: 'Poppins', sans-serif;
                    margin-top: 20px; 
                    padding: 10px 20px;
                    font-size: 1rem;
                    background-color: #000000;
                    box-shadow: 0 4px 8px rgba(10, 182, 7, 0.701);
                    color: white;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    z-index: 2;
                    transition: background-color 0.3s ease, transform 0.3s ease; 
                }

                /* Effet hover sur le bouton */
                button:hover {
                    background-color: #25b32c; 
                    transform: scale(1.05);     
                }

                a {
                    text-decoration: none;
                    color: #ffffff;
                    font-weight: 600;
                    font-size: 1.2rem;
                    display: block;
                    padding: 8px 16px;
                    border-radius: 8px;
                    transition: 0.3s ease-in-out;
                }

                a:hover {
                    background-color: #25b32c;
                    color: white;
                }
            </style>
        </head>
        <body>
            <div class="background"></div>  
            <header>
                <h1>Stations de vélos en libre service à {{ ville }}</h1>
            </header>
            <main>
                <div id="map"></div>
                <button id="calculate">Calculer la station la plus proche</button>
            </main>
            <script>
                // Initialisation de la carte
                var map = L.map('map').setView([{{ city_coords.lat }}, {{ city_coords.lng }}], 13);
                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 19
                }).addTo(map);

                var userMarker = null;
                var lineToClosestStation = null;
            
                // Clic sur la carte pour ajouter un marqueur
                map.on('click', function(e) {
                    if (userMarker) {
                        map.removeLayer(userMarker);
                    }
                    userMarker = L.marker(e.latlng, {
                        icon: L.icon({
                            iconUrl: 'https://leafletjs.com/examples/custom-icons/leaf-red.png',
                            iconSize: [38, 38],
                            iconAnchor: [19, 38],
                            popupAnchor: [0, -38]
                        })
                    }).addTo(map);
                });

                // Les emplacements des stations
                var locations = {{ locations|tojson }};
                
                // marqueurs pour chaque station de vélo
                locations.forEach(function(location) {
                    L.marker([location.lat, location.lng])
                        .addTo(map)
                        .bindPopup(location.name);  
                });

                // Calcul de la station la plus proche au clic
                document.getElementById('calculate').addEventListener('click', function() {
                    if (userMarker) {
                        var userLatLng = userMarker.getLatLng();
                        var closestStation = null;
                        var minDistance = Infinity;

                        // Parcours des stations pour trouver la plus proche
                        locations.forEach(function(location) {
                            var stationLatLng = L.latLng(location.lat, location.lng);
                            var distance = map.distance(userLatLng, stationLatLng);
                            if (distance < minDistance) {
                                minDistance = distance;
                                closestStation = location;
                            }
                        });

                        // Affichage du nom et de la distance de la station la plus proche
                        if (closestStation) {
                            var closestStationLatLng = L.latLng(closestStation.lat, closestStation.lng);
                            var distanceInKm = (minDistance / 1000).toFixed(2);

                            // Ajouter un popup sur le marqueur de l'utilisateur
                            userMarker.bindPopup('Position sélectionnée' + '<br>Station la plus proche : ' + closestStation.name + '<br>Distance : ' + distanceInKm + ' km').openPopup();

                            // Ajouter une ligne pour relier l'utilisateur à la station la plus proche
                            if (lineToClosestStation) {
                                map.removeLayer(lineToClosestStation);
                            }
                            lineToClosestStation = L.polyline([userLatLng, closestStationLatLng], { color: 'blue' }).addTo(map);
                        }
                    } else {
                        alert('Veuillez placer un marqueur sur la carte pour calculer la station la plus proche.');
                    }
                });
            </script>
        </body>
        </html>
            """)
        f.close()
    print(f"Fichier '{chemin_carte}' créé avec succès.")
else:
    print(f"Le fichier '{chemin_carte}' existe déjà.")

@app.route('/')
def accueil():
    return render_template('accueil.html')

@app.route('/ville/<ville>')
def carte(ville):
    locations = get_bike_locations(new_engine, ville)
    lat, lng = get_coord_ville(new_engine, ville)
    coords = {'lat': lat, 'lng': lng}  
    return render_template('carte.html', ville=ville, locations=locations, city_coords=coords)

if __name__ == '__main__':
    app.run(debug=True, port=5001, use_reloader=False)






