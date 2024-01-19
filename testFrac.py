import os
import matplotlib.pyplot as plt

f = open('zconfigfichier.txt')

text= f.read()

print(text)



f.close()



# #Fonction 1: calcul de la fractale ens

# import matplotlib.pyplot as plt

#

# def cantorenscoord(x, y, length, depth):

#     if depth == 0:

#         return [(x, y), (x + length, y)]

# #

# #     # Calcul des coordonnées pour les deux segments

#     x_left = x

#     x_right = x + length

#     y_next = y - 0.1  # Ajustez cette valeur pour l'espace vertical entre les lignes

#

# #     # Appels récursifs pour les deux segments

#     left_segment = cantorenscoord(x_left, y_next, length / 3, depth - 1)

#     right_segment = cantorenscoord(x_left + 2 * length / 3, y_next, length / 3,     depth - 1)

#

# #     # Concaténation des résultats

#     return left_segment + right_segment

#

# def fonc1():

#     depth = 4  # Vous pouvez ajuster le niveau de détail en changeant cette valeur

#     length = 1.0

#

#     coordinates = cantorenscoord(0, 0, length, depth)

#     print(coordinates)



# Les coordonnés:



#

# def cantor(x1, x2, y, degrecu):

#     if degrecu == 0:

#         return [x1, x2], [y, y]

#     else:

#         x_left = (2 * x1 + x2) / 3

#         x_right = (x1 + 2 * x2) / 3

#         y_new = y - 1  # Ajustez cette valeur pour le séparateur vertical

#

#         left_x, left_y = cantor(x1, x_left, y_new, degrecu - 1)

#         right_x, right_y = cantor(x_right, x2, y_new, degrecu - 1)

#

#         return


def fractalecarre(x, y, longueur_cote, niveau):

    """

    Fonction récursive pour calculer les abscisses et les ordonnées d'une fractale carrée.



    Paramètres :

    - x, y : coordonnées du coin supérieur gauche du carré.

    - longueur_cote : longueur du côté du carré.

    - niveau : niveau de la fractale.



    Retourne :

    - Liste des abscisses et des ordonnées de la fractale carrée.

    """

    if niveau == 0:

        return [(x, y), (x + longueur_cote, y), (x + longueur_cote, y - longueur_cote), (x, y - longueur_cote), (x, y)]



    nouvelle_longueur = longueur_cote / 3

    nouveaux_points = []



    for i in range(3):

        for j in range(3):

            if i == 1 and j == 1:

                continue  # Ignore le carré du milieu

            nouvel_x = x + i * nouvelle_longueur

            nouvel_y = y - j * nouvelle_longueur

            nouveaux_points.extend(fractalecarre(nouvel_x, nouvel_y, nouvelle_longueur, niveau - 1))



    return nouveaux_points







# #Fonction 2: calcul de la fractale classique

# import matplotlib.pyplot as plt

# import numpy as np

#

# def koch_snowflake(ax, order, length, x=0, y=0, angle=0):

#     if order == 0:

#         x_end = x + length * np.cos(np.radians(angle))

#         y_end = y + length * np.sin(np.radians(angle))

#         ax.plot([x, x_end], [y, y_end], color='blue')

#         return x_end, y_end

#

#     # Calcul des points pour la fractale de Koch

#     x1, y1 = koch_snowflake(ax, order - 1, length / 3, x, y, angle)

#     x2, y2 = koch_snowflake(ax, order - 1, length / 3, x1, y1, angle - 60)

#     x3, y3 = koch_snowflake(ax, order - 1, length / 3, x2, y2, angle + 60)

#     x4, y4 = koch_snowflake(ax, order - 1, length / 3, x3, y3, angle)

#

#     return x4, y4

#











#création des fichiers de lecture

cantorx = open('cantorx.txt','w')

cantory = open('cantory.txt','w')

carrex = open('carrex.txt','w')

carrey = open('carrey.txt','w')

flocon = open('flocon.txt', 'w')

carre = open ('carre.txt' , 'w')

Feigenbaum = open('Feigenbaum.txt', 'w')





# #remplissage des fichiers

# cantor.write("\n 1, 2 ,5,4 ,75464,8,7,5,45,6,")

# flocon.write("\nfloconcoord()")

# Feigenbaum.write("\nFeigenbaumcoord()")



#

# affichecantor=cantor.read()

# afficheflocon=[flocon.read()]

# affichefeigen=[Feigenbaum.read()]

#plt.plot([])

#plt.pause(0.1)

#plt.close()







#ans=input('Quelle figure désirez vous?')

#if ans=='Cantor':

# liste_pts = cantor(0, 8, 1, 6)

# print(liste_pts)

# text_x=""

# text_y=""

# for pt in liste_pts:

#     text_x += str(pt[0])+"\n"

#     text_y += str(pt[1])+"\n"

#

# cantorx.write(text_x)

# cantory.write(text_y)

# cantorx.close()

# cantory.close()

#





#fonction séparer points

def separer_points(liste_points):

    x_coords = []

    y_coords = []

    for point in liste_points:

        x= point[0]

        y=point[1]

        x_coords.append(x)

        y_coords.append(y)



    return x_coords, y_coords



toutpoint=fractalecarre(0,0,1,4)

x_carre=str(separer_points(toutpoint))

y_carre=str(separer_points(toutpoint))

carrex.write(x_carre)

carrey.write(y_carre)

carrex.close()

carrey.close()



# valeur ='eeee eezgntzo ee'

# valeur = valeur[2:-2]

# l = valeur.split(",")

# abscisse_lis=[]

# for i in range(l):

#     composante= l[i]

#     if i%2:

        #abscisse vs ordonnnees





#Fonction pour tracer nos figures

def tracer_figure(fichier_x, fichier_y):

    # Lire les coordonnées x et y depuis les fichiers

    open(fichier_x, 'r') as file_x, open(fichier_y, 'r') as file_y:

    x_coords = [float(line.strip()) for line in file_x]

    y_coords = [float(line.strip()) for line in file_y]



    # Tracer la figure

    plt.plot(x_coords, y_coords, marker='o', linestyle='-')

    plt.title('Figure tracée à partir de fichiers de coordonnées')

    plt.xlabel('Coordonnées X')

    plt.ylabel('Coordonnées Y')

    plt.grid(True)

    plt.show()

















#Suppression des fichiers

flocon.close()

Feigenbaum.close()

#os.remove('cantorx.txt')

#os.remove('cantory.txt')

#os.remove('flocon.txt')

#os.remove('Feigenbaum.txt')

#

