
from random import *
from math import *
import collections

def somme_liste(liste):
    somme = 0
    for element in liste:
        somme += element
    return somme

destot1=[]
totdes1=[]

couleur=['bleu','vert','rouge','jaune']

for k in range (0,4):

    for i in range(0,6):

        if i<=3:

            destot1.append([couleur[(i+1+k)%4],i+1])

        elif i>3:

            destot1.append([couleur[(i+1-3+k)%4],0])

destot2=[]

a=0

for k in range (0,6):

    for i in range(5,11):

        a=a+1

        if i<=5:

            destot2.append([couleur[(a+k)%4],i])

        elif i>5:

            destot2.append([couleur[(a-4+k)%4],i])



d1=[]

d2=[]

d3=[]

d4=[]

d5=[]

d6=[]

d7=[]

d8=[]

d9=[]

d10=[]

destot=[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]

a=-1

for j in range(0,4):

    a=a+1

    for i in range(0,6): 

        destot[j].append(destot1[i+a])



b=-1

for j in range(4,10):

    b=b+1

    for i in range(0,6):

        destot[j].append(destot2[i+b])



#phase 1 

les10 = []
print ("Phase 1, Objectif : Faire 2 Brelans")

for i in range(0, 10):
    les10.append(destot[i][randint(0, 5)])
    
print (les10)
les10_chiffres = [element[1] for element in les10]
les10_chiffres.sort()
les10_couleurs = [element[0] for element in les10]




resultat1 = 0
brelans_resultats1 = [] 
for element in les10_chiffres:
    if les10_chiffres.count(element) > 2 and element not in brelans_resultats1:
        brelans_resultats1.append(element)

print ("Brelans : ", brelans_resultats1)
 
quest = str(input("Souhaitez vous relancer des dés ? "))
if quest == "oui":  
 while len(brelans_resultats1) <2 or 0 in brelans_resultats1:
    s = int(input("Quels dés souhaitez-vous relancer ? "))
    del les10[s]
    les10.append(destot[s][randint(0, 5)])
    print (les10)

    for i in range(0, 10):
        if les10[i][1] == 1:
            a = a + 1

    brelans_resultats1 = [] 
    les10_chiffres = [element[1] for element in les10]

    for element in les10_chiffres:
        if les10_chiffres.count(element) > 2 and element not in brelans_resultats1:
            brelans_resultats1.append(element)

    print ("Brelans : ",brelans_resultats1)
    resultat1 = 0

    if len(brelans_resultats1) >= 2:
        resultat1 += 3*somme_liste(brelans_resultats1)
        break
else:
 if len(brelans_resultats1) == 1:
    resultat1 = 0
 else: 
    resultat1 += 3*somme_liste(brelans_resultats1)

print("Fin de la phase 1 ! ")
print("Score: ", resultat1)


# #phase 2 
les10 = []
for i in range(0, 10):
    les10.append(destot[i][randint(0, 5)])

print ("Phase 2, Objectif : Realiser un brelan et une suite de 4 chiffres") 
print (les10)
les10_chiffres = [element[1] for element in les10]
les10_chiffres.sort()
les10_couleurs = [element[0] for element in les10]
resultat2 = 0
suite_resultats2 = []
brelans_resultats2 = [] 

for element in les10_chiffres:
    if les10_chiffres.count(element) > 2 and element not in brelans_resultats2:
        brelans_resultats2.append(element)

les10_chiffres = sorted(collections.Counter(les10_chiffres))
for i in range(len(les10_chiffres) - 3):
    if les10_chiffres[i] + 1 == les10_chiffres[i + 1] and les10_chiffres[i] + 2 == les10_chiffres[i + 2] and les10_chiffres[i] + 3 == les10_chiffres[i + 3]:
        if not suite_resultats2 or len(suite_resultats2) < 4:
            suite_resultats2 = les10_chiffres[i:i + 4]
        elif sum(suite_resultats2) < sum(les10_chiffres[i:i + 4]):
            suite_resultats2 = les10_chiffres[i:i + 4]
            


print ("Suite de 4 : ", suite_resultats2)
print ("Brelans: ",brelans_resultats2)

for i in range(0, 10):
    if les10[i][1] == 1:
        a = a + 1
quest = str(input("Souhaitez vous relancer des dés ? "))
if quest == "oui":  
 while len(brelans_resultats2) < 1 or len(suite_resultats2) <1 or 0 in brelans_resultats2:
    s = int(input("Quels dés souhaitez-vous relancer ? "))
    del les10[s]
    les10.append(destot[s][randint(0, 5)])
    a=0
    print (les10)

    
    for i in range(0, 10):
        if les10[i][1] == 1:
            a = a + 1

    brelans_resultats2 = [] 
    les10_chiffres = [element[1] for element in les10]
    les10_chiffres.sort()
    suite_resultats2 = []

    for element in les10_chiffres:
        if les10_chiffres.count(element) > 2 and element not in brelans_resultats2:
            brelans_resultats2.append(element)

    les10_chiffres = sorted(collections.Counter(les10_chiffres))
    for i in range(len(les10_chiffres) - 3):
     if les10_chiffres[i] + 1 == les10_chiffres[i + 1] and les10_chiffres[i] + 2 == les10_chiffres[i + 2] and les10_chiffres[i] + 3 == les10_chiffres[i + 3]:
         if not suite_resultats2 or len(suite_resultats2) < 4:
            suite_resultats2 = les10_chiffres[i:i + 4]
         elif sum(suite_resultats2) < sum(les10_chiffres[i:i + 4]):
            suite_resultats2 = les10_chiffres[i:i + 4]

    print ("Suite de 4 : ", suite_resultats2)
    print ("Brelans: ",brelans_resultats2)

    if len(brelans_resultats2) == 1 and len(suite_resultats2) == 4:
        resultat2 = resultat2 + 3*somme_liste(brelans_resultats2)
        resultat2 = resultat2 + somme_liste(suite_resultats2)       
        break
else:
 if len(brelans_resultats2) == 1 and len(suite_resultats2) == 0 or len(brelans_resultats2) == 0 and len(suite_resultats2) == 4 or len(brelans_resultats2) == 0 and len(suite_resultats2) == 0:
    resultat2 = 0
 else: 
    resultat2 += 3*somme_liste(brelans_resultats1)
    resultat2 += somme_liste(suite_resultats2) 

print ("Objectif Accomplit ! Fin de la phase 2")
print("Score de la phase: ", resultat2)    
print("Score totale : ", resultat1 + resultat2) 

