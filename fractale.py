f =str(input("Répertoire du fichier"))


def dictionnaire(f):
    dictionnaire_figures = {}

    with open(f, 'r') as fichier:
        for ligne in fichier:
            elements = ligne.strip().split()

            if len(elements) >= 2:
                nom_forme = elements[0]
                niveau_recursivite = elements[1]
                autres_informations = elements[2:]

                cle = f"{nom_forme}_{niveau_recursivite}"
                valeur = autres_informations  

                dictionnaire_figures[cle] = valeur
    return dictionnaire_figures







def calculer_coordonnees_fractale(nom_forme, niveau_recursivite, autres_informations):
    print(f"Calcul des coordonnées pour {nom_forme} avec niveau de récursivité {niveau_recursivite}")
    print("Autres informations:", autres_informations)
    print("\n")

def parcourir_dictionnaire(d):
    for cle in d.keys():
        # Séparer le nom de la forme et le niveau de récursivité
        nom_forme, niveau_recursivite = cle.split('_')

        # Appeler la fonction de calcul des coordonnées
        calculer_coordonnees_fractale(nom_forme, niveau_recursivite, d[cle])

# Exemple d'utilisation
dictionnaire_figures = {

}

parcourir_dictionnaire(dictionnaire_figures)
