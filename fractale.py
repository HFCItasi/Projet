import os
import matplotlib.pyplot as plt
import testFrac as fr
import numpy as np

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
                print (cle)
                valeurs = [departx, departy, taillex, tailley, couleur, nom_forme]
                dictionnaire_figures[cle] = valeurs
            else: 
                print("Veuillez fournir un fichier avec d'avantages d'information")
    return dictionnaire_figures

def tracer_figure(fichier_x, fichier_y):

   # Lire les coordonnées x et y depuis les fichiers

   file_x=open(fichier_x, 'r').readlines()

   file_y=open(fichier_y, 'r').readlines()





   strx=str(file_x[0])[1:-1]



   listx = strx.split(",")

   listxfloat =[]

   for x in listx:

       listxfloat.append(float(x))

   x_coords=listxfloat



   stry=str(file_y[0])[1:-1]



   listy = stry.split(",")

   listyfloat =[]

   for y in listy:

       listyfloat.append(float(y))

   y_coords=listyfloat

   # Tracer la figure

   plt.plot(x_coords, y_coords, marker='o', linestyle='-')

   plt.title('Figure tracée à partir de fichiers de coordonnées')

   plt.xlabel('Coordonnées X')

   plt.ylabel('Coordonnées Y')

   plt.grid(True)

   plt.show()


# def parcourir_dictionnaire(dictionnaire_figures):
#     for cle in dictionnaire_figures.keys():
#         valeurs = dictionnaire_figures[cle]
#         toutpoint =[]
#         if valeurs [5] == "triangle":
#             toutpoint ==  fr.trinity(6, [(0, 0), (1, 0), (0.5, np.sqrt(3)/2)])
#         elif valeurs[5] == "koch":
#             toutpoint == fr.flocon_koch(100, 10)
#         elif valeurs[5] == "Feigenbaum":
#             toutpoint == fr.fractale_feigenbaum(0,0,2, 30 ,10)
#     nom_fichier_x =  valeurs [5] +"_x.txt"
#     nom_fichier_y =  valeurs [5] +"_y.txt"
#     nom_fichier_x = open('nom_fichier_x','w')
#     nom_fichier_y = open('nom_fichier_y','w')
#     x_coords = fr.separer_points(toutpoint)[0]
#     y_coords = fr.separer_points(toutpoint)[1]
#     nom_fichier_x.write(str(x_coords))
#     nom_fichier_y.write(str(y_coords))
#     nom_fichier_x.close()
#     nom_fichier_y.close()
#     dictionnaire_figures[cle] = [nom_fichier_x, nom_fichier_y]
#     return dictionnaire_figures

def parcourir_dictionnaire(dictionnaire_figures):
    for cle, valeurs in dictionnaire_figures.items():
        toutpoint = []
        if valeurs[5] == "triangle":
            toutpoint = fr.trinity(6, [(0, 0), (1, 0), (0.5, np.sqrt(3)/2)])
        elif valeurs[5] == "koch":
            toutpoint = fr.flocon_koch(100, 10)
        elif valeurs[5] == "Feigenbaum":
            toutpoint = fr.fractale_feigenbaum(0, 0, 2, 30, 10)
        
        nom_fichier_x = valeurs[5] + "_x.txt"
        nom_fichier_y = valeurs[5] + "_y.txt"
        with open(nom_fichier_x, 'w') as fichier_x, open(nom_fichier_y, 'w') as fichier_y:
            x_coords, y_coords = fr.separer_points(toutpoint)
            fichier_x.write(str(x_coords))
            fichier_y.write(str(y_coords))
        
        # Mettre à jour les valeurs dans le dictionnaire avec les noms des fichiers
        dictionnaire_figures[cle] = [nom_fichier_x, nom_fichier_y]
    
    return dictionnaire_figures


print ("veuillez fournir le fichier d'informations")
f = str(input("Répertoire du fichier : "))
d = dictionnaire(f)
print(d)
d = parcourir_dictionnaire(d)
# Assurez-vous que les noms de fichiers correspondent aux fichiers générés
tracer_figure(Feigenbaum_x, Feigenbaum_y)


