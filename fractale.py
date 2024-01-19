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
                départ = elements[2]
                taille = elements[3]
                couleur = elements[4]

                cle = f"{nom_forme} , {niveau_recursivite}" 
                valeurs = [départ, taille, couleur]
                dictionnaire_figures[cle] = valeurs
            else: 
                print("Veuillez fournir un fichier avec d'avantages d'information")
    return dictionnaire_figures

 
def parcourir_dictionnaire(dictionnaire_figures):
    for cle in dictionnaire_figures.keys():
        valeurs = dictionnaire_figures[cle]
        print(valeurs)
        coords = [[0,1]] # calcul_coordonnées(valeurs)
        fich = creation_fichiers(coords, cle)
        dictionnaire_figures[cle] = fich



d = dictionnaire(f)
print(d)



