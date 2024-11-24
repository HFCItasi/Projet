import pandas as pd
from sqlalchemy import create_engine, sql, text
import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk
from PIL import Image, ImageTk

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
newdatabase = 'jo'


#### Exemple ####

# Créer la base de données 'jo'
engine=get_connection(database)
create_database(newdatabase)

# Connexion à la base 'jo'
new_engine = get_connection(newdatabase)


# Créer et remplir la table 'coaches' dans la base JO

coach = 'D:/Code/Git/Projet/DATA JO/coaches.csv' #Accés du fichier CSV de remplissage
nom_table = 'coaches'  #Nom de la table que l'on souhaite crée 
create_table(coach, nom_table)
fill_table(coach, nom_table)



class SQLApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Database Jeux Olympiques de Paris 2024")
        self.root.geometry("1200x800")
        self.root.configure(bg="#ffffff")

        # Chargement et affichage des logos
        try:
            # Création d'un cadre pour les logos
            self.logo_frame = tk.Frame(root, bg="#ffffff")
            self.logo_frame.pack(pady=10)

            # Chargement des logos
            self.logo1 = Image.open("D:/Code/Git/Projet/DATA JO/thumbnail_logo_olympique.png") ############# Indiquer le chemin d'accès du logo telecharge######## 
            self.logo1 = self.logo1.resize((300, 150))  # Redimensionnement de l'image
            self.logo_photo1 = ImageTk.PhotoImage(self.logo1)

            self.logo2 = Image.open("D:/Code/Git/Projet/DATA JO/logoOM.png") ############# Indiquer le chemin d'accès du logo telecharge######## 
            self.logo2 = self.logo2.resize((300, 150))  # Redimensionnement de l'image
            self.logo_photo2 = ImageTk.PhotoImage(self.logo2)

            # Positionnement des logos
            self.logo_label2 = tk.Label(self.logo_frame, image=self.logo_photo2, bg="#ffffff")
            self.logo_label2.pack(side=tk.LEFT, padx=10)

            self.logo_label1 = tk.Label(self.logo_frame, image=self.logo_photo1, bg="#ffffff")
            self.logo_label1.pack(side=tk.LEFT, padx=10)

        except FileNotFoundError:
            messagebox.showerror("Erreur", "Logo non trouvé. Veuillez vérifier le chemin.")
            self.root.destroy()

        # Cadre principal
        self.frame = tk.Frame(root, bg="#f0f0f0", bd=5, relief=tk.RAISED)
        self.frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Zone de texte pour la requête
        self.query_label = tk.Label(self.frame, text="Entrez votre requête SQL :", font=("Helvetica", 14), bg="#f0f0f0")
        self.query_label.pack(pady=10)

        self.query_text = scrolledtext.ScrolledText(self.frame, wrap=tk.WORD, height=5, font=("Helvetica", 12), bg="#ffffff", fg="#333333", insertbackground="black")
        self.query_text.pack(pady=10, padx=10, fill=tk.BOTH)

        # Zone pour entrer le nom de la table
        self.table_label = tk.Label(self.frame, text="Table cible :", font=("Helvetica", 12), bg="#f0f0f0")
        self.table_label.pack(pady=5)

        self.table_entry = tk.Entry(self.frame, font=("Helvetica", 12), bg="#ffffff")
        self.table_entry.pack(pady=5, padx=10)

        # Menu déroulant pour des requêtes prédéfinies
        self.query_menu = ttk.Combobox(self.frame, state="readonly", font=("Helvetica", 12), width=80)
        self.query_menu["values"] = [
            "SELECT * FROM {table};",
            "SELECT (colonne1, colonne2) FROM {table} ORDER BY (colonne1);",
        ]
        self.query_menu.set("Requêtes prédéfinies")
        self.query_menu.pack(pady=5)
        self.query_menu.bind("<<ComboboxSelected>>", self.load_query)

        # Bouton pour exécuter la requête
        self.execute_button = tk.Button(self.frame, text="Exécuter", command=self.execute_query, font=("Helvetica", 14), bg="#ffcc00", fg="black", activebackground="#e6b800")
        self.execute_button.pack(pady=5)

        # Bouton pour effacer les résultats
        self.clear_button = tk.Button(self.frame, text="Effacer les résultats", command=self.clear_results, font=("Helvetica", 12), bg="#cccccc")
        self.clear_button.pack(pady=5)

        # Tableau pour afficher les résultats
        self.result_frame = tk.Frame(self.frame, bg="#ffffff")
        self.result_frame.pack(fill=tk.BOTH, expand=True)

        self.result_tree = ttk.Treeview(self.result_frame, columns=(), show="headings")
        self.result_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Barres de défilement
        self.scrollbar_y = ttk.Scrollbar(self.result_frame, orient=tk.VERTICAL, command=self.result_tree.yview)
        self.result_tree.configure(yscroll=self.scrollbar_y.set)
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.scrollbar_x = ttk.Scrollbar(self.result_frame, orient=tk.HORIZONTAL, command=self.result_tree.xview)
        self.result_tree.configure(xscroll=self.scrollbar_x.set)
        self.scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

    def load_query(self, event):
        """Charge une requête prédéfinie dans la zone de texte."""
        table = self.table_entry.get().strip()
        query = self.query_menu.get()
        if table:
            query = query.replace("{table}", table)
        else:
            query = "Veuillez spécifier une table dans le champ 'Table cible'."
        self.query_text.delete("1.0", tk.END)
        self.query_text.insert(tk.END, query)

    def execute_query(self):
        """Exécute la requête SQL et affiche les résultats."""
        query = self.query_text.get("1.0", tk.END).strip()
        if not query:
            messagebox.showwarning("Avertissement", "Veuillez entrer une requête SQL.")
            return

        # Informations de connexion à la base de données
        user = 'postgres'
        password = ''  # Ajoutez votre mot de passe ici si nécessaire
        host = '127.0.0.1'
        port = 5434

        try:
            engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{newdatabase}")
            with engine.connect() as connection:
                result = connection.execute(text(query))
                df = pd.DataFrame(result.fetchall(), columns=result.keys())

            # Mise à jour du tableau avec les résultats
            self.update_result_tree(df)

        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'exécution de la requête :\n{e}")

    def update_result_tree(self, df):
        """Met à jour le tableau des résultats."""
        self.result_tree.delete(*self.result_tree.get_children())  # Efface les anciennes données
        self.result_tree["columns"] = list(df.columns)
        self.result_tree["show"] = "headings"

        for col in df.columns:
            self.result_tree.heading(col, text=col)
            self.result_tree.column(col, anchor="center", width=150)  # Largeur fixe pour les colonnes

        for index, row in df.iterrows():
            self.result_tree.insert("", "end", values=list(row))

    def clear_results(self):
        """Efface les résultats affichés."""
        self.result_tree.delete(*self.result_tree.get_children())


if __name__ == "__main__":
    root = tk.Tk()
    app = SQLApp(root)
    root.mainloop()

#Déconnexion de l'utilisateur
disconect = disconnect_from_database(new_engine)
