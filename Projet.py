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
        
        
def tiragedes(les10):
    t=input("Saisir les numéros a changer? : exemple:03158 ")
    for i in t:
        j=int(i)
        les10[j]=destot[j][randint(0, 5)]
    return les10







#phase 1 

les10 = []
print ("Phase 1, Objectif : Faire 2 Brelans")

for i in range(0, 10):
    les10.append(destot[i][randint(0, 5)])
    
print (les10)
les10_chiffres = [element[1] for element in les10]
les10_chiffres.sort()




resultat1 = 0
brelans = [] 
for element in les10_chiffres:
    if les10_chiffres.count(element) > 2 and element not in brelans:
        brelans.append(element)

print ("Brelans : ", brelans)
 
quest = str(input("Souhaitez vous relancer des dés ? "))
if quest == "oui":  
 while len(brelans) <2 or 0 in brelans:
    les10=tiragedes(les10)
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

print ("Phase 2, Objectif : Realiser un brelan et une Suite de 4 chiffres") 
print (les10)
les10_chiffres = [element[1] for element in les10]
les10_chiffres.sort()
resultat2 = 0
Suite4 = []
brelans = [] 

for element in les10_chiffres:
    if les10_chiffres.count(element) > 2 and element not in brelans:
        brelans.append(element)
        les10_chiffres.remove(element)


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
    les10=tiragedes(les10)
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
            les10_chiffres.remove(element)

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
    les10=tiragedes(les10)
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
    les10=tiragedes(les10)
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
 while len(Suite8) <8 or 0 in Suite8:
    les10=tiragedes(les10)
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
   resultat5 += 40
   print("Bonus de 40 Points !")
   print("Score totale", resultat1 + resultat2 + resultat3 + resultat4 + resultat5)
   
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
    les10=tiragedes(les10)
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
if len(carre)>1:
    print("vous avez 4 fois ces numéros", carre)
else:
    for i in range(0, 10):
        if les10[i][1] == 1:
            a = a + 1
    quest = str(input("Souhaitez vous relancer des dés ? "))
    if quest == "oui":  
        while len(carre)<2:
            les10=tiragedes(les10)
            print (les10)


            les10_chiffres = [element[1] for element in les10]
            les10_chiffres.sort()
   
            carre = []
            for element in les10_chiffres:
                if les10_chiffres.count(element) > 3 and element not in carre:
                    carre.append(element)
            if len(carre)>1:
                print("vous avez 4 fois ces numéros", carre)
   

            if len(carre) == 2:
                resultat7= resultat7 + 4*somme_liste(carre)       
                break
    else:
        if len(carre) < 2: 
            resultat7 = 0
        else: 
            resultat7 += 4*somme_liste(carre) 

print ("Objectif Accomplit ! Fin de la phase 7")
print("Score de la phase: ", resultat7)    
print("Score totale : ", resultat1 + resultat2 + resultat3 + resultat4 + resultat5+ resultat6 + resultat7) 
 

###############Phase 8###############

def test8():
    suitecouleur=''
    les10_couleurs=[c[0] for c in les10]
    for element in couleur:
        if les10_couleurs.count(element)> 6:
            score = 0
            for d in les10:
                if d[0]==element:
                    score = score + d[1]
            return True,score
    return False,0

les10 = []
for i in range(0, 10):
    les10.append(destot[i][randint(0, 5)])
print ("Phase 8, Objectif : Il faut 7 dès de la même couleur") 
print (les10)
les10_couleurs = [element[0] for element in les10]
resultat8 = 0

if test8()[0]:
    print("vous avez au moins 7 dès de même couleur")
    resultat8=test8()[1]
else:
    quest = str(input("Souhaitez vous relancer des dés ? "))
    if quest == "oui":   
        while not test8()[0]:
            les10=tiragedes(les10)
            print (les10)
        print("vous avez 7 dès de cette même couleur")
        resultat8=test8()[1]
    else:
        resultat8=0

print ("Objectif Accomplit ! Fin de la phase 8")
print("Score de la phase: ", resultat8)    
print("Score totale : ", resultat1 + resultat2 + resultat3 + resultat4 + resultat5+ resultat6 + resultat7 + resultat8) 

les10 = []
print ("Phase 8, Objectif : Il faut 7 dès de la même couleur")

#Phase 9

def test9():
    cinq=0
    deux=0
    les10_chiffres=[c[1] for c in les10]
    for element in les10_chiffres:
        if les10_chiffres.count(element)>2 and les10_chiffres.count(element)<5:
            deux=element
        elif les10_chiffres.count(element)>=5 :
            cinq=element
            score=5*cinq+2*deux
            return True,score
    return False,0

les10 = []
for i in range(0, 10):
    les10.append(destot[i][randint(0, 5)])
print ("Phase 9, Objectif : Il faut un quintuplé et une paire") 
print (les10)
resultat9 = 0

if test9()[0]:
    resultat9=test9()[1]
else:
    quest = str(input("Souhaitez vous relancer des dés ? "))
    if quest == "oui":   
        while not test9()[0]:
            les10=tiragedes(les10)
            print (les10)
            print("vous avez  un quintuplé et une paire")
            resultat9=test9()[1]
    else:
        resultat9=0

print("vous avez un quintuplé et une paire" )
print ("Objectif Accomplit ! Fin de la phase 9")
print("Score de la phase: ", resultat9)    
print("Score totale : ", resultat1 + resultat2 + resultat3 + resultat4 + resultat5+ resultat6 + resultat7 + resultat8+ resultat9) 

#Phase 10

def test10():
    cinq=0
    trois=0
    les10_chiffres=[c[1] for c in les10]
    for element in les10_chiffres:
        if les10_chiffres.count(element)>3 and les10_chiffres.count(element<5):
            trois=element
        elif les10_chiffres.count(element)>=5 :
            cinq=element
            score=5*cinq+3*trois
            return True,score
    return False,0

les10 = []
for i in range(0, 10):
    les10.append(destot[i][randint(0, 5)])
print ("Phase 10, Objectif : Il faut un quintuplé et un triplé") 
print (les10)
resultat10 = 0

if test10()[0]:
    resultat10=test10()[1]
else:
    quest = str(input("Souhaitez vous relancer des dés ? "))
    if quest == "oui":   
        while not test10()[0]:
            les10=tiragedes(les10)
            print (les10)
        print("vous avez  un quintuplé et une paire")
        resultat10=test10()[1]
    else:
        resultat10=0

print("vous avez un quintuplé et un triplé" )
print ("Objectif Accomplit ! Fin de la phase 10 et fin du jeu")
print("Score de la phase: ", resultat10)    
print("Score totale : ", resultat1 + resultat2 + resultat3 + resultat4 + resultat5+ resultat6 + resultat7 + resultat8+ resultat9+ resultat10) 
 
###############Joueur 2##########################

print ("Phase 8, Objectif : Il faut 7 dès de la même couleur") 
print (les10)
les10_chiffres = [element[1] for element in les10]
les10_chiffres.sort()
les10_couleurs = [element[0] for element in les10]
resultat28 = 0
suitecouleur=0 
 
for i in range (0,10):
   k=i
   while les10_couleurs[0]==les10_couleurs[k]:
        suitecouleur=suitecouleur+1 
        k=k+1
print("vous avez", suitecouleur, "dès de la même couleur")

quest = str(input("Souhaitez vous relancer des dés ? "))
if quest == "oui":  
 while suitecouleur <7:
    s = int(input("Quels dés souhaitez-vous relancer ? ")) -1
    del les10[s]
    les10.append(destot[randint(0, 5)][randint(0, 5)])
    a=0
    print (les10)

    
#     for i in range(0, 10):
#         if les10[i][1] == 1:
#             a = a + 1

#     les10_chiffres = [element[1] for element in les10]
#     les10_chiffres.sort()
   
suitecouleur=0 
 
for i in range (0,10):
   k=i
   while les10_couleurs[0]==les10_couleurs[k%10]:
        suitecouleur=suitecouleur+1 
        k=k+1
        lacouleur=i
print("vous avez", suitecouleur, "dès de la même couleur", les10_couleurs[lacouleur])
   
for i in range (0,10):
    resultatbis8=les10[i][lacouleur]+resultatbis8

    if suitecouleur==7:
        resultat28 = resultat28 + resultatbis8     
        break
else:
 if suitecouleur < 2: 
    resultat28 = 0
 else: 
    resultat28 += resultatbis8

print ("Objectif Accomplit ! Fin de la phase 8")
print("Score de la phase: ", resultat28)    
print("Score totale J2 : ", resultat1 + resultat2 + resultat3 + resultat4 + resultat5+ resultat6 + resultat7 + resultat28) 
print("Récap: J1 ",resultat1 + resultat2 + resultat3 + resultat4 + resultat5 + resultat6 + resultat7 + resultat8 , "J2 ", resultat21 + resultat22 + resultat23 + resultat24 + resultat25 + resultat26 + resultat27 + resultat28)



