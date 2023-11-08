
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
brelans = [] 
for element in les10_chiffres:
    if les10_chiffres.count(element) > 2 and element not in brelans:
        brelans.append(element)

print ("Brelans : ", brelans)
 
quest = str(input("Souhaitez vous relancer des dés ? "))
if quest == "oui":  
 while len(brelans) <2 or 0 in brelans:
    s = int(input("Quels dés souhaitez-vous relancer ? "))
    del les10[s]
    les10.append(destot[s][randint(0, 5)])
    print (les10)

    for i in range(0, 10):
        if les10[i][1] == 1:
            a = a + 1

    brelans = [] 
    les10_chiffres = [element[1] for element in les10]

    for element in les10_chiffres:
        if les10_chiffres.count(element) > 2 and element not in brelans:
            brelans.append(element)

    print ("Brelans : ",brelans)
    resultat1 = 0

    if len(brelans) >= 2:
        resultat1 += 3*somme_liste(brelans)
        break
else:
 if len(brelans) == 1:
    resultat1 = 0
 else: 
    resultat1 += 3*somme_liste(brelans)

print("Fin de la phase 1 ! ")
print("Score: ", resultat1)


##############################phase 2######################### 
les10 = []
for i in range(0, 10):
    les10.append(destot[i][randint(0, 5)])

print ("Phase 2, Objectif : Realiser un brelan et une Suite4 de 4 chiffres") 
print (les10)
les10_chiffres = [element[1] for element in les10]
les10_chiffres.sort()
les10_couleurs = [element[0] for element in les10]
resultat2 = 0
Suite4 = []
brelans = [] 

for element in les10_chiffres:
    if les10_chiffres.count(element) > 2 and element not in brelans:
        brelans.append(element)

les10_chiffres = sorted(collections.Counter(les10_chiffres))
for i in range(len(les10_chiffres) - 3):
    if les10_chiffres[i] + 1 == les10_chiffres[i + 1] and les10_chiffres[i] + 2 == les10_chiffres[i + 2] and les10_chiffres[i] + 3 == les10_chiffres[i + 3]:
        if not Suite4 or len(Suite4) < 4:
            Suite4 = les10_chiffres[i:i + 4]
        elif sum(Suite4) < sum(les10_chiffres[i:i + 4]):
            Suite4 = les10_chiffres[i:i + 4]
            


print ("Suite de 4 : ", Suite4)
print ("Brelans: ",brelans)

for i in range(0, 10):
    if les10[i][1] == 1:
        a = a + 1
quest = str(input("Souhaitez vous relancer des dés ? "))
if quest == "oui":  
 while len(brelans) < 1 or len(Suite4) <1 or 0 in brelans:
    s = int(input("Quels dés souhaitez-vous relancer ? "))
    del les10[s]
    les10.append(destot[s][randint(0, 5)])
    a=0
    print (les10)

    
    for i in range(0, 10):
        if les10[i][1] == 1:
            a = a + 1

    brelans = [] 
    les10_chiffres = [element[1] for element in les10]
    les10_chiffres.sort()
    Suite4 = []

    for element in les10_chiffres:
        if les10_chiffres.count(element) > 2 and element not in brelans:
            brelans.append(element)

    les10_chiffres = sorted(collections.Counter(les10_chiffres))
    for i in range(len(les10_chiffres) - 3):
     if les10_chiffres[i] + 1 == les10_chiffres[i + 1] and les10_chiffres[i] + 2 == les10_chiffres[i + 2] and les10_chiffres[i] + 3 == les10_chiffres[i + 3]:
         if not Suite4 or len(Suite4) < 4:
            Suite4 = les10_chiffres[i:i + 4]
         elif sum(Suite4) < sum(les10_chiffres[i:i + 4]):
            Suite4 = les10_chiffres[i:i + 4]

    print ("Suite de 4 : ", Suite4)
    print ("Brelans: ",brelans)

    if len(brelans) == 1 and len(Suite4) == 4:
        resultat2 = resultat2 + 3*somme_liste(brelans)
        resultat2 = resultat2 + somme_liste(Suite4)       
        break
else:
 if len(brelans) == 1 and len(Suite4) == 0 or len(brelans) == 0 and len(Suite4) == 4 or len(brelans) == 0 and len(Suite4) == 0:
    resultat2 = 0
 else: 
    resultat2 += 3*somme_liste(brelans)
    resultat2 += somme_liste(Suite4) 

print ("Objectif Accomplit ! Fin de la phase 2")
print("Score de la phase: ", resultat2)    
print("Score totale : ", resultat1 + resultat2) 



####################################################phase 3########################################

les10 = []
for i in range(0, 10):
    les10.append(destot[i][randint(0, 5)])

print ("Phase 3, Objectif : Realiser un carre et une Suite de 4 chiffres") 
print (les10)
les10_chiffres = [element[1] for element in les10]
les10_chiffres.sort()
les10_couleurs = [element[0] for element in les10]
resultat3 = 0
Suite4 = []
carre = [] 

for element in les10_chiffres:
    if les10_chiffres.count(element) > 3 and element not in carre:
        carre.append(element)

les10_chiffres = sorted(collections.Counter(les10_chiffres))
for i in range(len(les10_chiffres) - 3):
    if les10_chiffres[i] + 1 == les10_chiffres[i + 1] and les10_chiffres[i] + 2 == les10_chiffres[i + 2] and les10_chiffres[i] + 3 == les10_chiffres[i + 3]:
        if not Suite4 or len(Suite4) < 4:
            Suite4 = les10_chiffres[i:i + 4]
        elif sum(Suite4) < sum(les10_chiffres[i:i + 4]):
            Suite4 = les10_chiffres[i:i + 4]
            


print ("Suite de 4 : ", Suite4)
print ("carre: ", carre)

for i in range(0, 10):
    if les10[i][1] == 1:
        a = a + 1
quest = str(input("Souhaitez vous relancer des dés ? "))
if quest == "oui":  
 while len(carre) < 1 or len(Suite4) <1 or 0 in carre:
    s = int(input("Quels dés souhaitez-vous relancer ? "))
    del les10[s]
    les10.append(destot[s][randint(0, 5)])
    a=0
    print (les10)

    
    for i in range(0, 10):
        if les10[i][1] == 1:
            a = a + 1

    carre = [] 
    les10_chiffres = [element[1] for element in les10]
    les10_chiffres.sort()
    Suite4 = []

    for element in les10_chiffres:
        if les10_chiffres.count(element) > 3 and element not in carre:
            carre.append(element)

    les10_chiffres = sorted(collections.Counter(les10_chiffres))
    for i in range(len(les10_chiffres) - 3):
     if les10_chiffres[i] + 1 == les10_chiffres[i + 1] and les10_chiffres[i] + 2 == les10_chiffres[i + 2] and les10_chiffres[i] + 3 == les10_chiffres[i + 3]:
         if not Suite4 or len(Suite4) < 4:
            Suite4 = les10_chiffres[i:i + 4]
         elif sum(Suite4) < sum(les10_chiffres[i:i + 4]):
            Suite4 = les10_chiffres[i:i + 4]

    print ("Suite de 4 : ", Suite4)
    print ("carre: ",carre)

    if len(carre) == 1 and len(Suite4) == 4:
        resultat3 = resultat3 + 4*somme_liste(carre)
        resultat3 = resultat3 + somme_liste(Suite4)       
        break
else:
 if len(carre) == 1 and len(Suite4) == 0 or len(carre) == 0 and len(Suite4) == 4 or len(carre) == 0 and len(Suite4) == 0:
    resultat3 = 0
 else: 
    resultat3 += 4*somme_liste(carre)
    resultat3 += somme_liste(Suite4) 

print ("Objectif Accomplit ! Fin de la phase 3")
print("Score de la phase: ", resultat3)    
print("Score totale : ", resultat1 + resultat2 + resultat3) 

######################"phase4################################

les10 = []
for i in range(0, 10):
    les10.append(destot[i][randint(0, 5)])

print ("Phase 4, Objectif : Realiser une suite de 7 chiffres") 
print (les10)
les10_chiffres = [element[1] for element in les10]
les10_chiffres.sort()
les10_couleurs = [element[0] for element in les10]
resultat4 = 0
Suite7 = []


les10_chiffres = sorted(collections.Counter(les10_chiffres))
for i in range(len(les10_chiffres) - 6):
    if les10_chiffres[i] + 1 == les10_chiffres[i + 1] and les10_chiffres[i] + 2 == les10_chiffres[i + 2] and les10_chiffres[i] + 3 == les10_chiffres[i + 3] and les10_chiffres[i] + 4 == les10_chiffres[i + 4] and les10_chiffres[i] + 5 == les10_chiffres[i + 5] and les10_chiffres[i] + 6 == les10_chiffres[i + 6] :
        if not Suite7 or len(Suite7) < 7:
            Suite4 = les10_chiffres[i:i + 7]
        elif sum(Suite7) < sum(les10_chiffres[i:i + 7]):
            Suite7 = les10_chiffres[i:i + 7]
            


print ("Suite de 7 : ", Suite7)

for i in range(0, 10):
    if les10[i][1] == 1:
        a = a + 1
quest = str(input("Souhaitez vous relancer des dés ? "))
if quest == "oui":  
 while len(Suite7) <7 or 0 in Suite7:
    s = int(input("Quels dés souhaitez-vous relancer ? "))
    del les10[s]
    les10.append(destot[s][randint(0, 5)])
    a=0
    print (les10)

    
    for i in range(0, 10):
        if les10[i][1] == 1:
            a = a + 1

    les10_chiffres = [element[1] for element in les10]
    les10_chiffres.sort()
    Suite7 = []


    les10_chiffres = sorted(collections.Counter(les10_chiffres))
    for i in range(len(les10_chiffres) - 6):
     if les10_chiffres[i] + 1 == les10_chiffres[i + 1] and les10_chiffres[i] + 2 == les10_chiffres[i + 2] and les10_chiffres[i] + 3 == les10_chiffres[i + 3] and les10_chiffres[i] + 4 == les10_chiffres[i + 4] and les10_chiffres[i] + 5 == les10_chiffres[i + 5] and les10_chiffres[i] + 6 == les10_chiffres[i + 6] :
        if not Suite7 or len(Suite7) < 7:
            Suite4 = les10_chiffres[i:i + 7]
        elif sum(Suite7) < sum(les10_chiffres[i:i + 7]):
            Suite7 = les10_chiffres[i:i + 7]
            

    print ("Suite de 7 : ", Suite7)
   

    if len(Suite7) == 7:
        resultat4 = resultat4 + somme_liste(Suite7)       
        break
else:
 if len(Suite7) < 7 : 
    resultat4 = 0
 else: 
    resultat4 += somme_liste(Suite7) 

print ("Objectif Accomplit ! Fin de la phase 4")
print("Score de la phase: ", resultat4)    
print("Score totale : ", resultat1 + resultat2 + resultat3 + resultat4) 



###############Phase 5###############

les10 = []
for i in range(0, 10):
    les10.append(destot[i][randint(0, 5)])

print ("Phase 5, Objectif : Realiser une suite de 8 chiffres") 
print (les10)
les10_chiffres = [element[1] for element in les10]
les10_chiffres.sort()
les10_couleurs = [element[0] for element in les10]
resultat5 = 0
Suite8 = []


les10_chiffres = sorted(collections.Counter(les10_chiffres))
for i in range(len(les10_chiffres) - 7):
    if les10_chiffres[i] + 1 == les10_chiffres[i + 1] and les10_chiffres[i] + 2 == les10_chiffres[i + 2] and les10_chiffres[i] + 3 == les10_chiffres[i + 3] and les10_chiffres[i] + 4 == les10_chiffres[i + 4] and les10_chiffres[i] + 5 == les10_chiffres[i + 5] and les10_chiffres[i] + 6 == les10_chiffres[i + 6] and les10_chiffres[i] + 7 == les10_chiffres[i + 7] :
        if not Suite8 or len(Suite8) < 8:
            Suite8 = les10_chiffres[i:i + 8]
        elif sum(Suite8) < sum(les10_chiffres[i:i + 8]):
            Suite8 = les10_chiffres[i:i + 8]
            


print ("Suite de 8 : ", Suite8)

for i in range(0, 10):
    if les10[i][1] == 1:
        a = a + 1
quest = str(input("Souhaitez vous relancer des dés ? "))
if quest == "oui":  
 while len(Suite7) <8 or 0 in Suite8:
    s = int(input("Quels dés souhaitez-vous relancer ? "))
    del les10[s]
    les10.append(destot[s][randint(0, 5)])
    a=0
    print (les10)

    
    for i in range(0, 10):
        if les10[i][1] == 1:
            a = a + 1

    les10_chiffres = [element[1] for element in les10]
    les10_chiffres.sort()
    Suite8 = []


les10_chiffres = sorted(collections.Counter(les10_chiffres))
for i in range(len(les10_chiffres) - 7):
    if les10_chiffres[i] + 1 == les10_chiffres[i + 1] and les10_chiffres[i] + 2 == les10_chiffres[i + 2] and les10_chiffres[i] + 3 == les10_chiffres[i + 3] and les10_chiffres[i] + 4 == les10_chiffres[i + 4] and les10_chiffres[i] + 5 == les10_chiffres[i + 5] and les10_chiffres[i] + 6 == les10_chiffres[i + 6] and les10_chiffres[i] + 7 == les10_chiffres[i + 7] :
        if not Suite8 or len(Suite8) < 8:
            Suite8 = les10_chiffres[i:i + 8]
        elif sum(Suite8) < sum(les10_chiffres[i:i + 8]):
            Suite8 = les10_chiffres[i:i + 8]
            

    print ("Suite de 8 : ", Suite8)
   

    if len(Suite8) == 8:
        resultat5 = resultat5 + somme_liste(Suite8)       
        break
else:
 if len(Suite8) < 8 : 
    resultat5 = 0
 else: 
    resultat5 += somme_liste(Suite8) 

print ("Objectif Accomplit ! Fin de la phase 5")
print("Score de la phase: ", resultat5)    
print("Score totale : ", resultat1 + resultat2 + resultat3 + resultat4 + resultat5) 

if resultat1 + resultat2 + resultat3 + resultat4 + resultat5 >= 221 :
   print("Bonus de 40 Points !")
   print("Score totale", resultat1 + resultat2 + resultat3 + resultat4 + resultat5 + 40)
   
###############Phase 6###############

les10 = []
for i in range(0, 10):
    les10.append(destot[i][randint(0, 5)])

print ("Phase 6, Objectif : Realiser une suite de 9 chiffres") 
print (les10)
les10_chiffres = [element[1] for element in les10]
les10_chiffres.sort()
les10_couleurs = [element[0] for element in les10]
resultat6 = 0
Suite9 = []


les10_chiffres = sorted(collections.Counter(les10_chiffres))
for i in range(len(les10_chiffres) -8):
    if les10_chiffres[i] + 1 == les10_chiffres[i + 1] and les10_chiffres[i] + 2 == les10_chiffres[i + 2] and les10_chiffres[i] + 3 == les10_chiffres[i + 3] and les10_chiffres[i] + 4 == les10_chiffres[i + 4] and les10_chiffres[i] + 5 == les10_chiffres[i + 5] and les10_chiffres[i] + 6 == les10_chiffres[i + 6] and les10_chiffres[i] + 7 == les10_chiffres[i + 7] and les10_chiffres[i] + 8 == les10_chiffres[i + 8] :
        if not Suite9 or len(Suite9) < 9:
            Suite9 = les10_chiffres[i:i + 9]
        elif sum(Suite9) < sum(les10_chiffres[i:i + 9]):
            Suite9 = les10_chiffres[i:i + 9]
            


print ("Suite de 9 : ", Suite9)

for i in range(0, 10):
    if les10[i][1] == 1:
        a = a + 1
quest = str(input("Souhaitez vous relancer des dés ? "))
if quest == "oui":  
 while len(Suite9) <9 or 0 in Suite9:
    s = int(input("Quels dés souhaitez-vous relancer ? "))
    del les10[s]
    les10.append(destot[s][randint(0, 5)])
    a=0
    print (les10)

    
    for i in range(0, 10):
        if les10[i][1] == 1:
            a = a + 1

    les10_chiffres = [element[1] for element in les10]
    les10_chiffres.sort()
    Suite9 = []



les10_chiffres = sorted(collections.Counter(les10_chiffres))
for i in range(len(les10_chiffres) -8):
    if les10_chiffres[i] + 1 == les10_chiffres[i + 1] and les10_chiffres[i] + 2 == les10_chiffres[i + 2] and les10_chiffres[i] + 3 == les10_chiffres[i + 3] and les10_chiffres[i] + 4 == les10_chiffres[i + 4] and les10_chiffres[i] + 5 == les10_chiffres[i + 5] and les10_chiffres[i] + 6 == les10_chiffres[i + 6] and les10_chiffres[i] + 7 == les10_chiffres[i + 7] and les10_chiffres[i] + 8 == les10_chiffres[i + 8] :
        if not Suite9 or len(Suite9) < 9:
            Suite9 = les10_chiffres[i:i + 9]
        elif sum(Suite9) < sum(les10_chiffres[i:i + 9]):
            Suite9 = les10_chiffres[i:i + 9]

    print ("Suite de 9 : ", Suite9)
   

    if len(Suite9) == 9:
        resultat6 = resultat6 + somme_liste(Suite9)       
        break
else:
 if len(Suite9) < 9: 
    resultat6 = 0
 else: 
    resultat6 += somme_liste(Suite9) 

print ("Objectif Accomplit ! Fin de la phase 6")
print("Score de la phase: ", resultat6)    
print("Score totale : ", resultat1 + resultat2 + resultat3 + resultat4 + resultat5+ resultat6) 
 

###############Phase 7###############

les10 = []
for i in range(0, 10):
    les10.append(destot[i][randint(0, 5)])

print ("Phase 7, Objectif : Il faut deux carres") 
print (les10)
les10_chiffres = [element[1] for element in les10]
les10_chiffres.sort()
les10_couleurs = [element[0] for element in les10]
resultat7 = 0
 
carre = []
for element in les10_chiffres:
    if les10_chiffres.count(element) > 3 and element not in carre:
        carre.append(element)
        print("vous avez 4 fois ces numéros", carre)

for i in range(0, 10):
    if les10[i][1] == 1:
        a = a + 1
quest = str(input("Souhaitez vous relancer des dés ? "))
if quest == "oui":  
 while len(carre) <2:
    s = int(input("Quels dés souhaitez-vous relancer ? "))
    del les10[s]
    les10.append(destot[s][randint(0, 5)])
    a=0
    print (les10)

    
    for i in range(0, 10):
        if les10[i][1] == 1:
            a = a + 1

    les10_chiffres = [element[1] for element in les10]
    les10_chiffres.sort()
   
carre = []
for element in les10_chiffres:
    if les10_chiffres.count(element) > 3 and element not in carre:
        carre.append(element)
    print("vous avez 4 fois ces numéros", carre)
   

    if len(carre) == 2:
        resultat6 = resultat6 + somme_liste(Suite9)       
        break
else:
 if len(carre) < 2: 
    resultat7 = 0
 else: 
    resultat7 += 4*somme_liste(carre) 

print ("Objectif Accomplit ! Fin de la phase 7")
print("Score de la phase: ", resultat7)    
print("Score totale : ", resultat1 + resultat2 + resultat3 + resultat4 + resultat5+ resultat6 + resultat7) 
 
 


