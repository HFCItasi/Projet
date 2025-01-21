class Concession:
   budget=200000

   def __init__(self, nom, leasingmax, socios=[]):
       self.socios = socios
       self.nom= nom
       self.leasingmax= leasingmax
       self.vehicules = {}
       self.leasers = []

   def addleaser(self,leaser):
       if str(leaser) in self.leasers :
           raise ConcessionException("L'objet ajouté n'est pas un leaser valide.")
       else:
           self.leasers.append(leaser)
      
   def verifleaser(self,leaser):
       if str(leaser) in self.leasers :
           return('Vrai'+ str(leaser) + 'a bien emprunté un véhicule')
       else: 
           return(str(leaser) +'ne fait pas encore partie de nos clients')

   def ajouter_vehicule(self, vehicule):
       if isinstance(vehicule, Vehicule):
           self.vehicules.append(vehicule)
       else:
           raise ConcessionException("L'objet ajouté n'est pas un véhicule valide.")
           
   def afficher_vehicules(self):
       return [vehicule.afficher_details() for vehicule in self.vehicules]
   
   def 

   def afficher_leasers(self):
       return [leaser.nom for leaser in self.leasers]   
       
       
class Vehicule(Concession):
   """Classe de base pour tous les véhicules."""
   def __init__(self, marque, modele, annee, prix, largeur, plaque, statut=False):
       self.marque = marque
       self.modele = modele
       self.annee = annee
       self.prix = prix
       self.largeur = largeur
       self.plaque =plaque
       self.statut=statut

   def afficher_details(self):
       return f"{self.marque} {self.modele} {self.plaque} {self.statut} ({self.largeur}) ({self.annee}) - {self.prix}€"
   
   def getplaque(self):
       return self.plaque    

   def getstatut(self):
       return self.statut


class Client: 
    def __init__(self, nom, leasingmax ,socios,voiture_dispo, leaser , nouveau_client = False):
        super().__init__(leasingmax ,socios ,voiture_dispo, leaser)
        self.nom = nom
        self.new = nouveau_client
        

    def leasing(plaque):
        if plaque in self.voiture_dispo:
            self.voiture_dispo.pop()
        
    
    def vehicule_loué(self): 
    
    
            




class VehiculeClassique(Vehicule):
   """Classe pour les véhicules classiques."""
   def __init__(self, marque, modele, annee, prix, typeclass):
       super().__init__(marque, modele, annee, prix)
       self.typeclass = typeclasse
   def afficher_details(self):
       details = super().afficher_details()
       return f"{details}, Type de voiture classique : {self.self.typeclass}"


class VehiculeSpeciale(Vehicule):
   """Classe pour les véhicules spéciaux."""
   def __init__(self, marque, modele, annee, prix, type_special):
       super().__init__(marque, modele, annee, prix)
       self.type_special = type_special

   def afficher_details(self):
       details = super().afficher_details()
       return f"{details}, Type spécial : {self.type_special}"


class Leaser:
   """Classe pour les leasers."""
   def __init__(self, nom, vehicules=None):
       self.nom = nom
       self.vehicules = vehicules if vehicules is not None else []

   def ajouter_vehicule(self, vehicule):
       if isinstance(vehicule, Vehicule):
           self.vehicules.append(vehicule)
       else:
           raise ConcessionException("L'objet ajouté n'est pas un véhicule valide.")

   def afficher_vehicules(self):
       return [vehicule.afficher_details() for vehicule in self.vehicules]


      
class ConcessionException(Exception):
   """Classe d'exception personnalisée pour la concession automobile."""
   def __init__(self, message):
       super().__init__(message)

