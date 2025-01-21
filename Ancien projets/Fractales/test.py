
f = open('frac.txt')
text= f.read()

print(text)





#Fonction 1: calcul de la fractale ens

import matplotlib.pyplot as plt

def cantorenscoord(x, y, length, depth):

    if depth == 0:

        return [(x, y), (x + length, y)]



    # Calcul des coordonnées pour les deux segments

    x_left = x

    x_right = x + length

    y_next = y - 0.1  # Ajustez cette valeur pour l'espace vertical entre les lignes



    # Appels récursifs pour les deux segments

    left_segment = cantorenscoord(x_left, y_next, length / 3, depth - 1)

    right_segment = cantorenscoord(x_left + 2 * length / 3, y_next, length / 3,     depth - 1)



    # Concaténation des résultats

    return left_segment + right_segment



def fonc1():

    depth = 4  # Vous pouvez ajuster le niveau de détail en changeant cette valeur

    length = 1.0



    coordinates = cantorenscoord(0, 0, length, depth)

    print(coordinates)



if __name__ == "f1":

    main()



#Fonction 2: calcul de la fractale classique

import matplotlib.pyplot as plt

import numpy as np



def koch_snowflake(ax, order, length, x=0, y=0, angle=0):

    if order == 0:

        x_end = x + length * np.cos(np.radians(angle))

        y_end = y + length * np.sin(np.radians(angle))

        ax.plot([x, x_end], [y, y_end], color='blue')

        return x_end, y_end



    # Calcul des points pour la fractale de Koch

    x1, y1 = koch_snowflake(ax, order - 1, length / 3, x, y, angle)

    x2, y2 = koch_snowflake(ax, order - 1, length / 3, x1, y1, angle - 60)

    x3, y3 = koch_snowflake(ax, order - 1, length / 3, x2, y2, angle + 60)

    x4, y4 = koch_snowflake(ax, order - 1, length / 3, x3, y3, angle)



    return x4, y4



def main():

    order = 3  # Vous pouvez ajuster le niveau de détail en changeant cette valeur

    length = 1.0



    fig, ax = plt.subplots()

    ax.set_aspect('equal', adjustable='datalim')

    ax.axis('off')



    koch_snowflake(ax, order, length)



    plt.show()



if __name__ == "__main__":

    main()