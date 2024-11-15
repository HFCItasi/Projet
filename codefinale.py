import pandas as pd
from sqlalchemy import create_engine, sql

# Fonction pour obtenir une connexion à la base de données
def get_connection(db_name):
    return create_engine(
        url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, db_name
        )
    )

# Fonction pour créer la base de données
def create_database(database):
    try:
        # Connexion à la base par défaut 'postgres' pour créer la nouvelle base
        engine = get_connection(database)  # Connexion à la base par défaut
        with engine.connect() as conn:
            print(f"Connection to {host} for user {user} created successfully.")
            
            # Créer la base de données si elle n'existe pas déjà
            create_db_query = f"CREATE DATABASE {database}"
            conn.execution_options(isolation_level="AUTOCOMMIT").execute(sql.text(create_db_query))
            print(f"Database {database} created successfully.")
    except Exception as ex:
        if 'DuplicateDatabase' not in str(ex):
            print(f"Could not create database due to the following error: \n {ex}")
        else:
            print(f"Database {database} already exists.")

# Fonction pour créer une table à partir d'un fichier CSV
def create_table(csv_file_path, table_name): 
    # Lire le fichier CSV
    df = pd.read_csv(csv_file_path, sep=';')
    
    # Créer la liste des colonnes avec leurs types
    colonne = df.columns
    nom_colonnes = []
    for col in colonne:
        if pd.api.types.is_integer_dtype(df[col]):
            nom_colonnes.append(f"{col} INTEGER")
        elif pd.api.types.is_float_dtype(df[col]):
            nom_colonnes.append(f"{col} FLOAT")
        else:
            nom_colonnes.append(f"{col} VARCHAR(255)")

    colonne_avec_nom = ", ".join(nom_colonnes)

    # Créer la table
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({colonne_avec_nom})"
    try:
        with new_engine.connect() as conn:
            conn.execute(sql.text(create_table_query))
            print(f"Table '{table_name}' created successfully.")
    except Exception as ex:
        print(f"Could not create table due to the following error: \n {ex}")

    # Insérer les données dans la table
    try:
        df.to_sql(table_name, new_engine, if_exists='append', index=False)
        print(f"Data inserted successfully into the '{table_name}' table.")
    except Exception as ex:
        print(f"Could not insert data due to the following error: \n {ex}")

# Fonction pour remplir une table avec des données depuis un fichier CSV
def fill_table(csv_file_path, table_name):
    df = pd.read_csv(csv_file_path, sep=';')
    print(f"Reading CSV file: {csv_file_path}")
    try:
        with new_engine.connect() as conn:
            df.to_sql(table_name, conn, if_exists='append', index=False)
            print(f"Data inserted successfully into the table '{table_name}'.")
    except Exception as ex:
        print(f"Could not insert data due to the following error: \n {ex}")

# Supprimer une base de données
def drop_database(database):
    engine = get_connection(database)
    try:
        with engine.connect() as conn:
            drop_db_query = f"DROP DATABASE IF EXISTS {database}"
            conn.execution_options(isolation_level="AUTOCOMMIT").execute(sql.text(drop_db_query))
            print(f"Database '{database}' deleted successfully.")
    except Exception as ex:
        print(f"Could not delete database due to the following error: \n {ex}")

# Informations de connexion à la base de données
user = 'postgres'
password = ''
host = '127.0.0.1'
port = 5434
database = 'cinema'
newdatabase = 'jo'

# Fichiers CSV
coach = 'C:/Users/tmarif/Downloads/coaches.csv'
athletes = 'C:/Users/tmarif/Downloads/athletes.csv'

# Créer la base de données 'jo'
create_database(newdatabase)

# Connexion à la base 'jo'
new_engine = get_connection(newdatabase)

# Créer et remplir la table 'athletes'
table_name = 'coaches'
create_table(coach, table_name)
fill_table(coach, table_name)

