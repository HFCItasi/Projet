print ("veuillez fournir le fichier d'informations")
f =str(input("Répertoire du fichier : "))

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
                valeurs = [departx, departy, taillex, tailley, couleur]
                dictionnaire_figures[cle] = valeurs
            else: 
                print("Veuillez fournir un fichier avec d'avantages d'information")
    return dictionnaire_figures

 
def parcourir_dictionnaire(dictionnaire_figures):
    for cle in dictionnaire_figures.keys():
        valeurs = dictionnaire_figures[cle]
        print(valeurs)
        toutpoints =  fractalecarre(valeurs[0],valeurs[1],valeurs[3],cle[1]) # calcul_coordonnées(valeurs)
        x_carre=str(separer_points(toutpoint))
        y_carre=str(separer_points(toutpoint))
        carrex.write(x_carre)
        carrey.write(y_carre)
        carrex.close()
        carrey.close()
        fich = creation_fichiers(coords, cle)
        dictionnaire_figures[cle] = fich



d = dictionnaire(f)
print(d)



