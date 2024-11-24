import pandas as pd
from sqlalchemy import create_engine, sql



# PYTHON FUNCTION TO CONNECT TO THE POSTGRESQL DATABASE AND RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection(db_name):
   return create_engine(
       url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
           user, password, host, port, db_name
       )
   )


# Create database and table dynamically
def create_database(database):
#    # Connect to the default database to create the new database
#    engine = get_connection(database)

    #Connexion et création de la database
   try:
       with engine.connect() as conn:
           print(f"Connection to the {host} for user {user} created successfully.")

           # Create the database if it doesn't exist
           create_db_query = "CREATE DATABASE " +database
           conn.execution_options(isolation_level="AUTOCOMMIT").execute(sql.text(create_db_query))
           print("Database " + database + " created succesfully.")


   except Exception as ex:
       if 'DuplicateDatabase' not in str(ex):
           print("Could not create database due to the following error: \n", ex)
       else:
           print("Database " + database + " already exists.")


   print("je continue car j'ai pris l'exception")


def create_table(csv_file_path): 
   
   # Read du CSV 
   df = pd.read_csv(csv_file_path, sep=';')

   # Création table 
   colonne = df.columns
   nom_colonnes = []

   for col in colonne:
       # Set default data type based on the first few rows of data
       if pd.api.types.is_integer_dtype(df[col]):
           nom_colonnes.append(f"{col} INTEGER")
       elif pd.api.types.is_float_dtype(df[col]):
           nom_colonnes.append(f"{col} FLOAT")
       else:
           nom_colonnes.append(f"{col} VARCHAR(255)")

   # Combine column definitions into a single string
   colonne_avec_nom = ", ".join(nom_colonnes)

   # Create the table
   create_table_query = f"CREATE TABLE IF NOT EXISTS athletes ({colonne_avec_nom})"
   try:
       with new_engine.connect() as conn:
           conn.execute(sql.text(create_table_query))
           print("Table 'athletes' created successfully.")

   except Exception as ex:
       print("Could not create table due to the following error: \n", ex)

   # Insert data into the table
   try:
       df.to_sql('athletes', new_engine, if_exists='append', index=False)
       print("Data inserted successfully into the 'athletes' table.")

   except Exception as ex:
       print("Could not insert data due to the following error: \n", ex)

def drop_database(database):
   engine = get_connection(database)

   try:
       with engine.connect() as conn:
           drop_db_query = "DROP DATABASE IF EXISTS JO"
           conn.execution_options(isolation_level="AUTOCOMMIT").execute(sql.text(drop_db_query))
           print("Database 'JO' deleted successfully.")

   except Exception as ex:
       print("Could not delete database due to the following error: \n", ex)


def fill_table(csv_file_path, table_name):

   # Lire le fichier CSV
   df = pd.read_csv(csv_file_path, sep=';')  # Ajustez le séparateur si nécessaire
   print(f"Reading CSV file: {csv_file_path}")

   # Insérer les données dans la table
   try:
       with engine.connect() as conn:
           df.to_sql(table_name, conn, if_exists='append', index=False)
           print(f"Data inserted successfully into the table '{table_name}'.")

   except Exception as ex:
       print("Could not insert data due to the following error: \n", ex)



# Chemin vers ton fichier CSV
# Database credentials
user = 'postgres'
password = ''
host = '127.0.0.1'
port = 5434
database = 'cinema'
newdatabase = 'jo'
mysql_conn = None  #Création de la variable



try:
   engine = get_connection(database)
   print("Connecting...")
   with engine.connect() as mysql_conn:
       print(f"Connection to the {host} for user {user} created successfully.")
except Exception as ex:
   print("Connection could not be made due to the following error: \n", ex)


coaches = 'D:/Code/Git/Projet/DATA/coaches.csv'
create_database(newdatabase)
# Connexion à la nouvelle database 
new_engine = get_connection(database)
create_table(coaches)
# Chemin vers votre fichier CSV
table_name = 'coaches'  # Nom de la table à remplir

# Appeler la fonction pour remplir la table
fill_table(coaches, table_name)

# finally:
#     mysql_conn.close()
#     engine.dispose()
#     print(f"Disconnection to the {host} for user {user} successfull.")


