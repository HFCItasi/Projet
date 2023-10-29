def carre (x):
    resultat = x**2
    return resultat 
def cube (x):
    resultat = x**3
    return resultat 
def inverse (x):
    resultat = 1/x
    return resultat 


def somme(list):
    somme = 0
    for i in list:
        somme = somme + i
    return somme


condi=[]
r1=[]
for item in nosresultats:
  if item != 3: 
    condi.append(item)
    
a = str(input("Voulez vous relancer des dès ? "))
if a == "oui": 
 s = int(input("Lesquels ?"))
 while nosresultats == condi:
  del les10[s]
  les10.append(destot[s][randint(0,5)]) 
  if les10 != condi: 
    r1.append(les10)