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
coach = 'D:/Code/Git/Projet/DATA/coaches.csv'
athletes = 'C:/Users/tmarif/Downloads/athletes.csv'

# Créer la base de données 'jo'
create_database(newdatabase)

# Connexion à la base 'jo'
new_engine = get_connection(newdatabase)

# Créer et remplir la table 'coaches'
table_name = 'coaches'
create_table(coach, table_name)
fill_table(coach, table_name)

# #Installez:
# #pip install tkinter pandas pillow sqlalchemy

# import tkinter as tk
# from tkinter import messagebox, scrolledtext
# import pandas as pd
# from PIL import Image, ImageTk
# from sqlalchemy import create_engine, text

# class SQLApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Information JO")
#         self.root.geometry("1000x800")  # Fenêtre agrandie
#         self.root.configure(bg="#ffffff")  # Couleur de fond

#         # Chargement et affichage des logos
#         try:
#             # Création d'un cadre pour les logos
#             self.logo_frame = tk.Frame(root, bg="#ffffff")
#             self.logo_frame.pack(pady=10)

#             # Chargement des logos
#             self.logo1 = Image.open("Z:/informatique/info 2A/PROJET 1/logo_olympique.png")
#             self.logo1 = self.logo1.resize((300, 150))  # Redimensionnement de l'image
#             self.logo_photo1 = ImageTk.PhotoImage(self.logo1)

#             self.logo2 = Image.open("Z:/informatique/info 2A/PROJET 1/logoOM.png")
#             self.logo2 = self.logo2.resize((300, 150))  # Redimensionnement de l'image
#             self.logo_photo2 = ImageTk.PhotoImage(self.logo2)

#             # Positionnement des logos
#             self.logo_label2 = tk.Label(self.logo_frame, image=self.logo_photo2, bg="#ffffff")
#             self.logo_label2.pack(side=tk.LEFT, padx=10)

#             self.logo_label1 = tk.Label(self.logo_frame, image=self.logo_photo1, bg="#ffffff")
#             self.logo_label1.pack(side=tk.LEFT, padx=10)

#         except FileNotFoundError:
#             messagebox.showerror("Erreur", "Logo non trouvé. Veuillez vérifier le chemin.")
#             self.root.destroy()

#         # Cadre principal pour ajouter des contours
#         self.frame = tk.Frame(root, bg="#f0f0f0", bd=5, relief=tk.RAISED)
#         self.frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

#         # Zone de texte pour la requête
#         self.query_label = tk.Label(self.frame, text="Entrez votre requête SQL:", font=("Helvetica", 14), bg="#f0f0f0")
#         self.query_label.pack(pady=10)

#         self.query_text = scrolledtext.ScrolledText(self.frame, wrap=tk.WORD, height=10, font=("Helvetica", 12), bg="#ffffff", fg="#333333", insertbackground='black')
#         self.query_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

#         # Bouton pour exécuter la requête
#         self.execute_button = tk.Button(self.frame, text="Exécuter", command=self.execute_query, font=("Helvetica", 14), bg="#ffcc00", fg="black", activebackground="#e6b800")
#         self.execute_button.pack(pady=5)

#         # Zone de texte pour afficher les résultats
#         self.result_label = tk.Label(self.frame, text="Résultats:", font=("Helvetica", 14), bg="#f0f0f0")
#         self.result_label.pack(pady=10)

#         self.result_text = scrolledtext.ScrolledText(self.frame, wrap=tk.WORD, height=10, font=("Helvetica", 12), bg="#ffffff", fg="#333333", insertbackground='black')
#         self.result_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

#     def execute_query(self):
#         query = self.query_text.get("1.0", tk.END).strip()
#         if not query:
#             messagebox.showwarning("Avertissement", "Veuillez entrer une requête SQL.")
#             return

#         # Informations de connexion à la base de données
#         user = 'postgres'
#         password = ''  # Ajoutez votre mot de passe ici si nécessaire
#         host = '127.0.0.1'
#         port = 5434
#         database = 'cinema'

#         # Connexion à la base de données
#         try:
#             engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")
#             with engine.connect() as connection:
#                 # Utilisation de text() pour les requêtes textuelles
#                 result = connection.execute(text(query))
#                 df = pd.DataFrame(result.fetchall(), columns=result.keys())  # Convertir les résultats en DataFrame

#             # Affichage des résultats
#             self.result_text.delete("1.0", tk.END)  # Efface le texte précédent
#             self.result_text.insert(tk.END, df.to_string(index=False))

#         except Exception as e:
#             messagebox.showerror("Erreur", f"Erreur lors de l'exécution de la requête:\n{e}")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = SQLApp(root)
#     root.mainloop()