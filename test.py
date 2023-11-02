#On retravaille sur les conditions 

from random import *
from math import *

destot1=[]
totdes1=[]

couleur=['bleu','vert','rouge','jaune']

for k in range (0,4):

    for i in range(0,6):

        if i<=3:

            destot1.append([couleur[(i+k)%4],i+1])

        elif i>3:

            destot1.append([couleur[(i-3+k)%4],0])

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
r1 = []
resultat1 = 0

def somme_liste(liste):
    somme = 0
    for element in liste:
        somme += element
    return somme

for i in range(0, 10):
    les10.append(destot[i][randint(0, 5)])


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


les10_chiffres = [element[1] for element in les10]




#Liste pour la plus grande suite de 4 chiffres 

plus_grande_suite = []
for i in range(len(les10_chiffres) - 3):
    if les10_chiffres[i] + 1 == les10_chiffres[i + 1] and les10_chiffres[i] + 2 == les10_chiffres[i + 2] and les10_chiffres[i] + 3 == les10_chiffres[i + 3]:
        if not plus_grande_suite or len(plus_grande_suite) < 4:
            plus_grande_suite = les10_chiffres[i:i + 4]
        elif sum(plus_grande_suite) < sum(les10_chiffres[i:i + 4]):
            plus_grande_suite = les10_chiffres[i:i + 4]

print("Suite de 4 chiffres la plus grande :", plus_grande_suite)



# Liste pour brelans 
brelans_resultats = []
for element in les10_chiffres:
 if les10_chiffres.count(element) > 2 and element not in brelans_resultats:
  brelans_resultats.append(element) 

