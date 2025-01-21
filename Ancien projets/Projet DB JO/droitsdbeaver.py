import pandas
from sqlalchemy import create_engine
from sqlalchemy import sql
from sqlalchemy.pool import NullPool

# DEFINE THE DATABASE CREDENTIALS
user = 'postgres'
password = ''
host = '127.0.0.1'
port = 5434
database = 'jo' # puis changer à sport une fois la base créée



def get_connection():
    return create_engine(url="postgresql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database), poolclass=NullPool)


##### Give droits à Dbeaver pour acceder à la table ##########
engine = ""
mysql_conn = ""
try:
    engine = get_connection()
    print(f"Connecting...")
    with engine.connect() as mysql_conn:
        print(f"Connection to the {host} for user {user} created successfully.")

        query = "GRANT SELECT ON TABLE table TO PUBLIC" ###remplacer table par le nom de la table souhaitée

        #
        sql_query = sql.text(query)
        mysql_conn.execution_options(isolation_level="AUTOCOMMIT").execute(sql_query)


except Exception as ex:
    print("Connection could not be made due to the following error: \n", ex)

finally:
    mysql_conn.close()
    engine.dispose()
    print(f"Disconnection to the {host} for user {user} successfull.")


# # Fichiers CSV
# coach = 'D:/Code/Git/Projet/DATA JO/coaches.csv'
# athletes = 'D:/Code/Git/Projet/DATA JO/athletes.csv'
# events = 'D:/Code/Git/Projet/DATA JO/events.csv'
# medalist = 'D:/Code/Git/Projet/DATA JO/medallists.csv'
# medals = 'D:/Code/Git/Projet/DATA JO/medals.csv'
# medalstotal = 'D:/Code/Git/Projet/DATA JO/medals_total.csv'
# nocs = 'D:/Code/Git/Projet/DATA JO/nocs.csv'
# schedules = 'D:/Code/Git/Projet/DATA JO/schedules.csv'
# schedules_preliminary = 'D:/Code/Git/Projet/DATA JO/schedules_preliminary.csv'
# teams = 'D:/Code/Git/Projet/DATA JO/teams.csv'
# technical_officials = 'D:/Code/Git/Projet/DATA JO/technical_officials.csv'
# torch_route = 'D:/Code/Git/Projet/DATA JO/torch_route.csv'
# venues = 'D:/Code/Git/Projet/DATA JO/venues.csv'
