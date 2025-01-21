import pandas as pd
from sqlalchemy import create_engine, sql, text


# Fonction pour obtenir une connexion à la base de données
def get_connection(db_name):
    return create_engine(
        url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, db_name
        )
    )

# Fonction pour créer la base de données
def create_database(newdatabase):
    """
    Prends le nom de la DB voulue et créé celle-ci
    
    :param database: Nom de la database 
    
    """
    try:
        # Connexion à la base par défaut 'postgres' pour créer la nouvelle base
        engine = get_connection(database)  # Connexion à la base par défaut
        with engine.connect() as conn:
            print(f"Connection à {host} pour {user} réalisée avec succes.")
            
            # Créer la base de données si elle n'existe pas déjà
            create_db_query = f"CREATE DATABASE {newdatabase};"
            conn.execution_options(isolation_level="AUTOCOMMIT").execute(sql.text(create_db_query))
            print(f"Database {newdatabase} cree avec succes.")
    except Exception as ex:
        if 'DuplicateDatabase' not in str(ex):
            print(f"Creation de la database à échouer suite à: \n {ex}")
        else:
            print(f"Database {newdatabase} deja existente.")

# Fonction pour créer une table à partir d'un fichier CSV
def create_table(chemin_csv, nom_table):
    """
    Crée une table de DB basée sur un fichier CSV.

    :param chemin_csv: Chemin vers le fichier CSV.
    :param nom_table: Nom de la table à créer.

    """
    try:
        # Lire le fichier CSV
        df = pd.read_csv(chemin_csv, sep=';')
        print(f" '{chemin_csv}' lu avec succes.")

        # Déduire les types de colonnes pour PostgreSQL
        nom_colonnes = []
        for col in df.columns:
            if pd.api.types.is_integer_dtype(df[col]):
                nom_colonnes.append(f'"{col}" INTEGER')
            elif pd.api.types.is_float_dtype(df[col]):
                nom_colonnes.append(f'"{col}" FLOAT')
            elif pd.api.types.is_bool_dtype(df[col]):
                nom_colonnes.append(f'"{col}" BOOLEAN')
            elif pd.api.types.is_datetime64_any_dtype(df[col]):
                nom_colonnes.append(f'"{col}" TIMESTAMP')
            else:
                nom_colonnes.append(f'"{col}" VARCHAR(255)')

        # Construire la requête SQL pour créer la table
        colonne_avec_nom = ", ".join(nom_colonnes)
        create_table_query = f"CREATE TABLE IF NOT EXISTS {nom_table} ({colonne_avec_nom});"

        # Exécuter la requête pour créer la table
        with new_engine.connect() as conn:
            conn.execute(sql.text(create_table_query))
            print(f"Table '{nom_table}' cree avec succes.")
    
    except Exception as ex:
        print(f"Creation de la table à échouer suite à: \n{ex}")



# Fonction pour remplir une table avec des données depuis un fichier CSV
def fill_table(chemin_csv, nom_table):
    """
    Remplit à partir d'un CSV une table 
    
    :param chemin_csv : Chemin d'accès au CSV 
    :nom_table : nom de la table à remplir 

    """
    df = pd.read_csv(chemin_csv, sep=';')
    print(f"Lecture du fichier CSV: {chemin_csv}")
    try:
        
        if 'current' in df.columns:
            # Convertir la colonne 'current' en entier (1 pour True, 0 pour False)
            df['current'] = df['current'].astype(bool).astype(int)

        with new_engine.connect() as conn:
            df.to_sql(nom_table, conn, if_exists='append', index=False)
            print(f"Data inseree avec succes dans '{nom_table}'.")

    except Exception as ex:
        print(f"L'insertion de la database à échouer suite à: \n {ex}")


def disconnect_from_database(engine):
    """
    Ferme le moteur de base de données SQLAlchemy.

    Args:
        engine (Engine): Objet moteur SQLAlchemy.

    Returns:
        bool: True si la déconnexion réussit, False sinon.
    """
    try:
        if engine:
            engine.dispose()
            print("Déconnexion réussie.")
            return True
        else:
            print("Aucun moteur actif à fermer.")
            return False
    except Exception as e:
        print(f"Erreur lors de la déconnexion : {e}")
        return False

# Informations de connexion à la base de données
user = 'postgres'
password = ''
host = '127.0.0.1'
port = 5434
database = 'cinema'
newdatabase = 'stations'


# Créer la base de données 'stations'
engine=get_connection(database)
create_database(newdatabase)

# Connexion à la base 'stations'
new_engine = get_connection(newdatabase)


# Créer et remplir la table 'stations' dans la base stations

stations = 'D:/Code/Projet velo/stations.csv' #Accés du fichier CSV de remplissage
nom_table = 'stations'  #Nom de la table que l'on souhaite crée 
create_table(stations, nom_table)
fill_table(stations, nom_table)


