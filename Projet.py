
from random import *
from math import *

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


les10 = []


print ("Phase 1, Objectif : Faire 2 Brelans")

for i in range(0, 10):
    les10.append(destot[i][randint(0, 5)])
    
print (les10)
les10_chiffres = [element[1] for element in les10]
les10_couleurs = [element[0] for element in les10]

a=0
b=0
c=0
d=0
e=0
f=0
g=0
  
h=0

x=0

j=0

z=0

for i in range(0,10):



    if les10[i][1]==1:

        a=a+1

    elif les10[i][1]==2:

        b=b+1

    elif les10[i][1]==3:

        c=c+1

    elif les10[i][1]==4:

        d=d+1

    elif les10[i][1]==5:

        e=e+1

    elif les10[i][1]==6:

        f=f+1

    elif les10[i][1]==7:

        g=g+1

    elif les10[i][1]==8:

        h=h+0

    elif les10[i][1]==9:

        x=x+1

    elif les10[i][1]==10:

        j=j+1

    else:

        z=z+1

nosresultats=[z,a,b,c,d,e,f,g,h,x,j]



#Analyse des dès    les triples marchent très bien, il faut faire lcas cas ou triple et que le triple ne servent pas pour la création des autres combinaisons

triple=0

quatre=0

for i in range(0,11):

    if nosresultats[i]==3 and triple==0:

        a=i

        triple=triple+1

        print("3 les mêmes")

    if nosresultats[i]==3 and i!=a:

        triple=triple+1

        print("3 les mêmes")

    if nosresultats[i]==4:

        print("4 les mêmes")

        quatre=quatre+1

suite3=0

suite4=0

suite5=0

#pas beoins de plusieurs suite

for i in range(0,9):
    if nosresultats[i]>=1 and nosresultats[i+1]>=1 and nosresultats[i+2]>=1  and nosresultats[i]<3 and nosresultats[i+1]<3 and nosresultats[i+2]<3:
        print("suite de 3")

        suite3=suite3+1

        b=i

    elif suite3>0 and nosresultats[i]>=1 and nosresultats[i+1]>=1 and nosresultats[i+2]>=1 and nosresultats[i+2+1]>=1 :

        suite4=suite4+1
  
for i in range(0, 10):
    if les10[i][1] == 1:
        a = a + 1


#phase 1 

resultat1 = 0
chiffre_resultats1 = [] 
for element in les10_chiffres:
    if les10_chiffres.count(element) > 2 and element not in chiffre_resultats1:
        chiffre_resultats1.append(element)

print (chiffre_resultats1)
 
quest = str(input("Souhaitez vous relancer des dés ? "))
if quest == "oui":  
 while len(chiffre_resultats1) <2 :
    s = int(input("Quels dés souhaitez-vous relancer ? "))
    del les10[s]
    les10.append(destot[s][randint(0, 5)])
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    g=0
    
    h=0

    x=0

    j=0

    z=0

    for i in range(0,10):



        if les10[i][1]==1:

            a=a+1

        elif les10[i][1]==2:

            b=b+1

        elif les10[i][1]==3:

            c=c+1

        elif les10[i][1]==4:

            d=d+1

        elif les10[i][1]==5:

            e=e+1

        elif les10[i][1]==6:

            f=f+1

        elif les10[i][1]==7:

            g=g+1

        elif les10[i][1]==8:

            h=h+0

        elif les10[i][1]==9:

            x=x+1

        elif les10[i][1]==10:

            j=j+1

        else:

            z=z+1

    nosresultats=[z,a,b,c,d,e,f,g,h,x,j]
    print (les10)

    triple=0

    quatre=0

    for i in range(0,11):

        if nosresultats[i]==3 and triple==0:

            a=i

            triple=triple+1

            print("3 les mêmes")

        if nosresultats[i]==3 and i!=a:

            triple=triple+1

            print("3 les mêmes")

        if nosresultats[i]==4:

            print("4 les mêmes")

            quatre=quatre+1



    suite3=0

    suite4=0

    suite5=0


    for i in range(0,9):
        if nosresultats[i]>=1 and nosresultats[i+1]>=1 and nosresultats[i+2]>=1  and nosresultats[i]<3 and nosresultats[i+1]<3 and nosresultats[i+2]<3:
            print("suite de 3")

            suite3=suite3+1

            b=i

        elif suite3>0 and nosresultats[i]>=1 and nosresultats[i+1]>=1 and nosresultats[i+2]>=1 and nosresultats[i+2+1]>=1 :

            suite4=suite4+1
    
    for i in range(0, 10):
        if les10[i][1] == 1:
            a = a + 1

    chiffre_resultats1 = [] 
    les10_chiffres = [element[1] for element in les10]

    for element in les10_chiffres:
        if les10_chiffres.count(element) > 2 and element not in chiffre_resultats1:
            chiffre_resultats1.append(element)

    print ("Suite de 3",chiffre_resultats1)
    resultat1 = 0

    if len(chiffre_resultats1) >= 2:
        resultat1 += 3*somme_liste(chiffre_resultats1)
        break
else:
 if len(chiffre_resultats1) == 1:
    resultat1 = 0
 else: 
    resultat1 += 3*somme_liste(chiffre_resultats1)

print("Fin de la phase 1 ! ")
print("Score: ", resultat1)


# #phase 2 
les10 = []
for i in range(0, 10):
    les10.append(destot[i][randint(0, 5)])

print ("Phase 2, Objectif : Realiser un brelan et une suite de 4 chiffres") 
print (les10)
les10_chiffres = [element[1] for element in les10]
les10_couleurs = [element[0] for element in les10]
resultat2 = 0
suite_resultats2 = []
brelans_resultats2 = [] 
for element in les10_chiffres:
    if les10_chiffres.count(element) > 2 and element not in brelans_resultats2:
        brelans_resultats2.append(element)
for i in range(len(les10_chiffres) - 3):
         if les10_chiffres[i] + 1 == les10_chiffres[i + 1] and les10_chiffres[i] + 2 == les10_chiffres[i + 2] and les10_chiffres[i] + 3 == les10_chiffres[i + 3] and les10_chiffres[i] not in suite_resultats2:
            suite_resultats2.extend(les10_chiffres[i:i+4])


a=0
b=0
c=0
d=0
e=0
f=0
g=0

h=0

x=0

j=0

z=0

for i in range(0,10):



    if les10[i][1]==1:

        a=a+1

    elif les10[i][1]==2:

        b=b+1

    elif les10[i][1]==3:

        c=c+1

    elif les10[i][1]==4:

        d=d+1

    elif les10[i][1]==5:

        e=e+1

    elif les10[i][1]==6:

        f=f+1

    elif les10[i][1]==7:

        g=g+1

    elif les10[i][1]==8:

        h=h+0

    elif les10[i][1]==9:

        x=x+1

    elif les10[i][1]==10:

        j=j+1

    else:

        z=z+1

nosresultats=[z,a,b,c,d,e,f,g,h,x,j]


triple=0

quatre=0

for i in range(0,11):

    if nosresultats[i]==3 and triple==0:

        a=i

        triple=triple+1

        print("3 les mêmes")

    if nosresultats[i]==3 and i!=a:

        triple=triple+1

        print("3 les mêmes")

    if nosresultats[i]==4:

        print("4 les mêmes")

        quatre=quatre+1



suite3=0

suite4=0

suite5=0


for i in range(0,9):
    if nosresultats[i]>=1 and nosresultats[i+1]>=1 and nosresultats[i+2]>=1  and nosresultats[i]<3 and nosresultats[i+1]<3 and nosresultats[i+2]<3:
        print("suite de 3")

        suite3=suite3+1

        b=i

    elif suite3>0 and nosresultats[i]>=1 and nosresultats[i+1]>=1 and nosresultats[i+2]>=1 and nosresultats[i+2+1]>=1 :

        suite4=suite4+1

for i in range(0, 10):
    if les10[i][1] == 1:
        a = a + 1

 
quest = str(input("Souhaitez vous relancer des dés ? "))
if quest == "oui":  
 while len(brelans_resultats2) <1 and len(suite_resultats2) <1 :
    s = int(input("Quels dés souhaitez-vous relancer ? "))
    del les10[s]
    les10.append(destot[s][randint(0, 5)])
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    g=0
    
    h=0

    x=0

    j=0

    z=0

    for i in range(0,10):



        if les10[i][1]==1:

            a=a+1

        elif les10[i][1]==2:

            b=b+1

        elif les10[i][1]==3:

            c=c+1

        elif les10[i][1]==4:

            d=d+1

        elif les10[i][1]==5:

            e=e+1

        elif les10[i][1]==6:

            f=f+1

        elif les10[i][1]==7:

            g=g+1

        elif les10[i][1]==8:

            h=h+0

        elif les10[i][1]==9:

            x=x+1

        elif les10[i][1]==10:

            j=j+1

        else:

            z=z+1

    nosresultats=[z,a,b,c,d,e,f,g,h,x,j]
    print (les10)

    triple=0

    quatre=0

    for i in range(0,11):

        if nosresultats[i]==3 and triple==0:

            a=i

            triple=triple+1

            print("3 les mêmes")

        if nosresultats[i]==3 and i!=a:

            triple=triple+1

            print("3 les mêmes")

        if nosresultats[i]==4:

            print("4 les mêmes")

            quatre=quatre+1



    suite3=0

    suite4=0

    suite5=0


    for i in range(0,9):
        if nosresultats[i]>=1 and nosresultats[i+1]>=1 and nosresultats[i+2]>=1  and nosresultats[i]<3 and nosresultats[i+1]<3 and nosresultats[i+2]<3:
            print("suite de 3")

            suite3=suite3+1

            b=i

        elif suite3>0 and nosresultats[i]>=1 and nosresultats[i+1]>=1 and nosresultats[i+2]>=1 and nosresultats[i+2+1]>=1 :

            suite4=suite4+1
    
    for i in range(0, 10):
        if les10[i][1] == 1:
            a = a + 1

    brelans_resultats2 = [] 
    les10_chiffres = [element[1] for element in les10]
    suite_resultats2 = []

    for element in les10_chiffres:
        if les10_chiffres.count(element) > 2 and element not in brelans_resultats2:
            brelans_resultats2.append(element)

    for i in range(len(les10_chiffres) - 3):
         if les10_chiffres[i] + 1 == les10_chiffres[i + 1] and les10_chiffres[i] + 2 == les10_chiffres[i + 2] and les10_chiffres[i] + 3 == les10_chiffres[i + 3]:
            suite_resultats2.extend(les10_chiffres[i:i+4])

    print ("Suite de 3 : ",brelans_resultats2)
    resultat2 = 0
    if len(brelans_resultats2) == 1 and len(suite_resultats2) == 1:
        resultat1 += 3*somme_liste(brelans_resultats2)
        resultat2 += somme_liste(suite_resultats2)       
        print(resultat2)
        break
else:
 if len(brelans_resultats2) == 1 and len(suite_resultats2) == 0 or len(brelans_resultats2) == 0 and len(suite_resultats2) == 1 or len(brelans_resultats2) == 0 and len(suite_resultats2) == 0:
    resultat2 = 0
 else: 
    resultat2 += 3*somme_liste(chiffre_resultats1)
    resultat2 += somme_liste(suite_resultats2) 

print ("Objectif Accomplit ! Fin de la phase 2")
print("Score de la phase: ", resultat2)    
print("Score totale : ", resultat1 + resultat2) 

#point à taffer : régler le probleme avec le resultat 2 qui vaut 0 alors que condition sont remplies, dés qui start à 1 et considérer uniquement la suite qui à les plus hautes valeurs 