import os
import matplotlib.pyplot as plt

import numpy as np

import math



#Fonction 1: calcul de la fractale triangle

def trinity(order, vertices):

   if order == 0:

       return vertices

   else:
       midpoints = [

           ((vertices[0][0] + vertices[1][0]) / 2, (vertices[0][1] + vertices[1][1]) / 2),

           ((vertices[1][0] + vertices[2][0]) / 2, (vertices[1][1] + vertices[2][1]) / 2),

           ((vertices[2][0] + vertices[0][0]) / 2, (vertices[2][1] + vertices[0][1]) / 2)

       ]



       return trinity(order - 1, [vertices[0], midpoints[0], midpoints[2]]) + \
              trinity(order - 1, [midpoints[0], vertices[1], midpoints[1]]) + \
              trinity(order - 1, [midpoints[2], midpoints[1], vertices[2]])



#Fonction 2: calcul de la fractale classique

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

   # Coordonnées des sommets du triangle équilatéral

   x1, y1 = 0, 0

   x2, y2 = longueur_segment, 0

   x3, y3 = longueur_segment / 2, longueur_segment * (3 ** 0.5) / 2



   # Générer les segments de Koch pour chaque côté du triangle

   segments = []

   segments += fractale_koch(x1, y1, x2, y2, profondeur)

   segments += fractale_koch(x2, y2, x3, y3, profondeur)

   segments += fractale_koch(x3, y3, x1, y1, profondeur)



   return segments


#Fonction 3 :fractale feigenbaum

def fractale_feigenbaum(x, y, longueur, angle, profondeur):

   if profondeur == 0:

       return [(x, y)]



   # Calcul des nouvelles coordonnées

   x_nouveau = x + longueur * np.cos(angle)

   y_nouveau = y + longueur * np.sin(angle)



   # Récupération des coordonnées du point actuel

   coordonnees = [(x, y), (x_nouveau, y_nouveau)]



   # Appels récursifs pour les deux branches

   coordonnees += fractale_feigenbaum(x_nouveau, y_nouveau, longueur / 2, angle - np.radians(45), profondeur - 1)

   coordonnees += fractale_feigenbaum(x_nouveau, y_nouveau, longueur / 2, angle + np.radians(45), profondeur - 1)



   return coordonnees

#création des fichiers de lecture



# triangle_x = "trianglex.txt"

# triangle_y = "triangley.txt"



# flocon_x = 'floconx.txt'

# flocon_y = 'flocony.txt'



# feigx= 'feigeunx.txt'

# feigy= 'feigeuny.txt'





# trianglx = open(triangle_x,'w')

# triangly = open(triangle_y,'w')



# floconx = open(flocon_x, 'w')

# flocony = open(flocon_y, 'w')



# feigeunbaumx=open(feigx, 'w')

# feigeunbaumy=open(feigy, 'w')



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



# ahah=trinity(6, [(0, 0), (1, 0), (0.5, np.sqrt(3)/2)])

# x_triangle=separer_points(ahah)[0]

# y_triangle=separer_points(ahah)[1]

# trianglx.write(str(x_triangle))

# triangly.write(str(y_triangle))

# trianglx.close()

# triangly.close()





# loulou=fractale_feigenbaum(0,0,2, 30 ,10)

# x_feigeun=separer_points(loulou)[0]

# y_feigeun=separer_points(loulou)[1]

# feigeunbaumx.write(str(x_feigeun))

# feigeunbaumy.write(str(y_feigeun))

# feigeunbaumx.close()

# feigeunbaumy.close()



# popo=flocon_koch(100, 10)

# x_flocon=(separer_points(popo)[0])

# y_flocon=(separer_points(popo)[1])

# floconx.write(str(x_flocon))

# flocony.write(str(y_flocon))

# floconx.close()

# flocony.close()



#Fonction pour tracer nos figures

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















#Suppression des fichiers

#flocon.close()

#Feigenbaum.close()

#os.remove('cantorx.txt')

#os.remove('cantory.txt')

#os.remove('flocon.txt')

#os.remove('Feigenbaum.txt')


