
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



# t=[]
# for k in range (0,3): 
#  t.append(destot[randint(0, 9)])
#  print (t)
#  a = str(input("Voulez vous retirez des dés ? "))
# while a == "Oui" or "oui":
#   s = int(input("Numéro du dès à retirer "))
#   t.pop(s)    


#phase 1
les10=[]
r1=[]

def somme(list):
    somme = 0
    for i in list:
        somme = somme + i
    return somme

for i in range (0,10):

    les10.append(destot[i][randint(0,5)])  



print (les10)
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

print(nosresultats)
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
    resultat1 = r1.somme
    break
else: 
 r1.append(les10)
 resultat1 = r1.somme
print (resultat1)
  





  


#comptage




# #phase 2 

# les10=[]
# r2=[]
# for i in range (0,10):

#     les10.append(destot[i][randint(0,5)])  
# print (les10)

# a = str(input("Voulez vous relancer des dès ? "))
# if a == "oui": 
#  s = int(input("Lesquels ?"))
#  while les10 != #condi:
#   del les10[s]
#   les10.append(destot[s][randint(0,5)]) 
#   print (les10)
#   if les10=condi: 
#     del les1O[#pas condi]
#     r2.append(les10)
#     resultat2 = somme.r2
#     break
# else: 
#  del les1O[#pas condi]
#  r2.append(les10)
#  resultat2 = int somme.r2
 
# print resultat2