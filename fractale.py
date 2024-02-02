import os
import matplotlib.pyplot as plt
import numpy as np
import random


#Fonction 1: calcul de la fractale triangle

def trinity(recursivite, vertices):

   if recursivite == 0:

       return vertices

   else:
       midpoints = [

           ((vertices[0][0] + vertices[1][0]) / 2, (vertices[0][1] + vertices[1][1]) / 2),

           ((vertices[1][0] + vertices[2][0]) / 2, (vertices[1][1] + vertices[2][1]) / 2),

           ((vertices[2][0] + vertices[0][0]) / 2, (vertices[2][1] + vertices[0][1]) / 2)

       ]



       return trinity(recursivite - 1, [vertices[0], midpoints[0], midpoints[2]]) + \
              trinity(recursivite - 1, [midpoints[0], vertices[1], midpoints[1]]) + \
              trinity(recursivite - 1, [midpoints[2], midpoints[1], vertices[2]])


# #Fonction 2: calcul de la fractale de koch

def fractale_koch(x1, y1, x2, y2, profondeur):
    if profondeur == 0:
        return [(x1, y1), (x2, y2)]
    else:
        # Calculer les points intermédiaires
        x3 = (2 * x1 + x2) / 3
        y3 = (2 * y1 + y2) / 3
        x4 = (x1 + 2 * x2) / 3
        y4 = (y1 + 2 * y2) / 3
        x5 = (x3 + x4) / 2 + (y4 - y3) * (3 ** 0.5) / 2
        y5 = (y3 + y4) / 2 + (x3 - x4) * (3 ** 0.5) / 2

        # Appels récursifs pour les segments restants
        segments = []
        segments += fractale_koch(x1, y1, x3, y3, profondeur - 1)
        segments += fractale_koch(x3, y3, x5, y5, profondeur - 1)
        segments += fractale_koch(x5, y5, x4, y4, profondeur - 1)
        segments += fractale_koch(x4, y4, x2, y2, profondeur - 1)

        return segments

# Fonction pour générer les coordonnées du flocon de Koch
def flocon_koch(longueur_segment, profondeur):
    x1, y1 = 0, 0
    x2, y2 = longueur_segment, 0
    x3, y3 = longueur_segment / 2, longueur_segment * (3 ** 0.5) / 2
    segments = []
    segments += fractale_koch(x1, y1, x2, y2, profondeur)
    segments += fractale_koch(x2, y2, x3, y3, profondeur)
    segments += fractale_koch(x3, y3, x1, y1, profondeur)

    return segments

# def flocon_koch(level, p1=(75, 50.5), p2=(25, 50.5)):
#     if level == 0:
#         return [p1, p2]
#     else:
#         x1, y1 = p1
#         x2, y2 = p2
        
#         x3 = (2 * x1 + x2) / 3
#         y3 = (2 * y1 + y2) / 3
#         x5 = (x1 + 2 * x2) / 3
#         y5 = (y1 + 2 * y2) / 3
#         x4 = 0.5 * (x1 + x2) + (np.sqrt(3) / 6) * (y1 - y2)
#         y4 = 0.5 * (y1 + y2) + (np.sqrt(3) / 6) * (x2 - x1)

#         segments = []
#         segments.extend(flocon_koch(level - 1, p1, (x3, y3)))
#         segments.extend(flocon_koch(level - 1, (x3, y3), (x4, y4)))
#         segments.extend(flocon_koch(level - 1, (x4, y4), (x5, y5)))
#         segments.extend(flocon_koch(level - 1, (x5, y5), p2))
        
#         return segments




#Fonction 3 :fractale feigenbaum

def fractale_feigenbaum(x, y, longueur, angle, recursivite):

   if recursivite == 0:

       return [(x, y)]



   # Calcul des nouvelles coordonnées

   x_nouveau = x + longueur * np.cos(angle)

   y_nouveau = y + longueur * np.sin(angle)



   # Récupération des coordonnées du point actuel

   coordonnees = [(x, y), (x_nouveau, y_nouveau)]



   # Appels récursifs pour les deux branches

   coordonnees += fractale_feigenbaum(x_nouveau, y_nouveau, longueur / 2, angle - np.radians(45), recursivite - 1)

   coordonnees += fractale_feigenbaum(x_nouveau, y_nouveau, longueur / 2, angle + np.radians(45), recursivite - 1)



   return coordonnees

#Fonction pour tracer les figures 

def tracer_figure(fichier_x, fichier_y, couleur):
    # Lire les coordonnées x et y depuis les fichiers
    file_x = open(fichier_x, 'r').readlines()
    file_y = open(fichier_y, 'r').readlines()

    strx = str(file_x[0])[1:-1]
    listx = strx.split(",")
    listxfloat = [float(x) for x in listx]

    stry = str(file_y[0])[1:-1]
    listy = stry.split(",")
    listyfloat = [float(y) for y in listy]

    plt.clf()
    plt.plot(listxfloat, listyfloat, marker='o', linestyle='-', color=couleur)
    plt.grid(True)
    plt.show()


#Fonction qui génère le dictionnaire en fonction du txt 
   
def dictionnaire(f):
    dictionnaire_figures = {}

    with open(f, 'r') as fichier:
        for ligne in fichier:
            elements = ligne.strip().split()

            if len(elements) >= 2:
                nom_forme = elements[0]
                niveau_recursivite = elements[1]
                departx = elements[2]
                departy = elements[3]
                taillex = elements[4]
                tailley = elements[5]
                couleur = elements[6]


                cle = f"{nom_forme} , {niveau_recursivite}" 
                valeurs = [departx, departy, taillex, tailley , couleur, nom_forme, niveau_recursivite]
                dictionnaire_figures[cle] = valeurs
            else: 
                print("Veuillez fournir un fichier avec d'avantages d'information")
    return dictionnaire_figures

#Fonction qui permet de séparer les coordonnées x et y et la couleur : 

def separer_points(liste_points):
    
    x_coords = []
    y_coords = []

    for point in liste_points:
        x_coords.append(point[0])
        y_coords.append(point[1])

    return x_coords, y_coords


#Fonction qui parcours le dictionnnaire et modifie le dictionnaire en prenant comme clé le nom et la recursivité 
#et associe le fichier des coordonnées x,y et la couleur pour chaque figure 

def parcourir_dictionnaire(dictionnaire_figures):
    for cle, valeurs in dictionnaire_figures.items():
        toutpoint = []
        if valeurs[5] == "triangle":
            toutpoint = trinity(int(valeurs[6]), [(0, 0), (1, 0), (0.5, np.sqrt(3)/2)])
        elif valeurs[5] == "Koch":
            toutpoint = flocon_koch(int(valeurs[2]), int(valeurs[6]))
        elif valeurs[5] == "Feigenbaum":
            toutpoint = fractale_feigenbaum(int(valeurs[0]), int(valeurs[1]), int(valeurs[2]), 30, int(valeurs[6]))
        nom_fichier_x = valeurs[5] + "_x.txt"
        nom_fichier_y = valeurs[5] + "_y.txt"
        with open(nom_fichier_x, 'w') as fichier_x, open(nom_fichier_y, 'w') as fichier_y:
            x_coords, y_coords = separer_points(toutpoint)
            fichier_x.write(str(x_coords))
            fichier_y.write(str(y_coords))
        dictionnaire_figures[cle] = [nom_fichier_x, nom_fichier_y, valeurs[4]]
    
    return dictionnaire_figures

#Supression des fichiers créés après execution
def supprimer_fichiers(fichier_x, fichier_y):
    os.remove(fichier_x)
    os.remove(fichier_y)

#Prise du fichier txt avec les informations
print ("veuillez fournir le fichier d'informations")
f = str(input("Répertoire du fichier : "))
d = dictionnaire(f)
d = parcourir_dictionnaire(d)

#Interactions avec l'utilisateur:

print ("Veuillez choisir la figure que vous voulez afficher parmi les suivantes:")
for cle in d:
    print(cle)

while True:
    choix = input("Entrez le nom de la figure que vous voulez afficher : ")

    if choix.isdigit() and int(choix) > 0:
        niveau_recursivite = int(choix)
        figures_disponibles = [cle for cle in d if cle.endswith(str(niveau_recursivite))]
        if figures_disponibles:
            choix = random.choice(figures_disponibles)
            fichier_x, fichier_y, couleur = d[choix]
            tracer_figure(fichier_x, fichier_y, couleur)
        else:
            print("Aucune figure trouvée pour ce niveau de récursivité.")
    
    elif choix in d:
        fichier_x, fichier_y, couleur = d[choix]
        tracer_figure(fichier_x, fichier_y, couleur) 
    else:
        print("La figure n'existe pas dans le dictionnaire.")

    relance = input("Souhaitez-vous afficher une nouvelle figure ? (oui/non) : ")
    if relance.lower() != 'oui':
        break
    
