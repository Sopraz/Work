# # p.44
from tkinter import*

from math import*
import pickle
import os
import random

def Exercice56(chaine):
    for i in range (len(chaine)):
        if chaine[i] == 'e':
            return True
    return False

def Exercice57(chaine):
    occurence = 0
    for i in range (len(chaine)):
        if chaine[i] == 'e':
            occurence +=1
    return occurence

def Exercice58(chaine):
    for i in range(len(chaine)):
        print(chaine[i],end='*')

def Exercice59(chaine):
    tab = []
    a= -1
    for i in range(len(chaine)):
        print(chaine[a],end='')
        a += -1

# tex1.pack()
# bou1 = Button(fen1, text='Quitter', command = fen1.destroy)
# bou1.pack()
# fen1.mainloop()
def Exercice59bis(chaine):
    longeur = len(chaine)
    i = longeur -1
    reverse = ''
    while i>= 0:
        reverse+= chaine[i]
        i = i-1
    return reverse
def Exercice510(chaine):
    longeur = len(chaine)
    g = ''
    i = len(chaine)-1
    while i>= 0:
        g += chaine[i]
        i += -1
    if g == chaine :
        print("PALINDROME")
    else:
        print('Pas plindrome')

# # p.47
def Exercice511():
    t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
    'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
    t3 = []
    for i in range (len(t1)):
        t3.append(t2[i])
        t3.append(t1[i])
    return t3

def Exercice512():
    t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
    for i in range(len(t2)):
        print(t2[i],end=' ')

def Exercice513():
    liste = []
    n = int(input("Nombre d'elements dans la liste : "))
    for i in range(n):
        numero = int(input())
        liste.append(numero)
    g = 0
    for i in range (len(liste)):
        if liste[i] >g:
            g = liste[i]
    print ('Le plus grand element de cette liste est', g)

def Exercice514():
    liste = []
    n = int(input("Nombre d'elements dans la liste : "))
    for i in range(n):
        numero = int(input())
        liste.append(numero)
    pair = []
    impair = []
    for i in range(n):
        if liste[i]% 2 == 0:
            pair.append(liste[i])
        else:
            impair.append(liste[i])
    return pair,impair

def Exercice515():
    liste = []
    n = int(input("Nombre d'elements dans la liste : "))
    for i in range(n):
        numero =input()
        liste.append(numero)
    moinsde6 = []
    plusde6 = []
    for i in range(n):
        if len(liste[i]) >6:
            plusde6.append(liste[i])
        else:
            moinsde6.append(liste[i])
    return moinsde6, plusde6
#  p.52
def Exercice61():
    vitesse = float(input())
    vitesse2 = vitesse*1.609
    print('La vitesse en mile est', vitesse, "mile par heure et la vitesse en km est ", vitesse2, ' km par heure')

def Exercice63():
    lon = float(input('Entre la longeur : '))
    acc = float(input('Entre la largeur : '))
    periode = 2* pi * sqrt(lon/acc)
    return periode

def Exercice64():
    tab = []
    numero = 0
    while numero != '':
        numero = input('Veuillez entrer une valeur ')
        tab.append(numero)
    del tab[-1]
    return tab
# p.53
from turtle import*
''' False renvoie a la valeur 0 et True a la valeur 1
            while a    =    while a!=0
'''
# p.58
def Exercice68():
    a = int(input('Entrez la borne inferieure : '))
    b = int(input('Entrez la bonne superieure : '))
    s =  0
    i = 1
    for i in range (a,b+1):
        if i%5 == 0 and i%3 == 0:
            s += i
    return s

def Exercice68bis():
    a = int(input('Entrez la borne inferieure : '))
    b = int(input('Entrez la bonne superieure : '))
    s =  0
    i = 1
    for i in range (a,b+1):
        if i%5 == 0 or i%3 == 0:
            print(s, end=' + ')
            s += i
    return s

def Exercice69(n):
    if n%4 == 0 and n%100 !=0:
        print("L'anne", n,'est bisextile' )
    elif n%4 == 0 and n%400 == 0:
            print( "L'anne", n,'est bisextile')
    else:
        print( "L'anne", n,"n'est pas bisextile")

def Exercice610():
    nom = input('Entre ton nom : ')
    sex = input('Ton sexe (M ou F) : ')
    if sex == 'M':
        print('Chere Monsieur',nom)
    else:
        print('Cher Mademoiselle', nom)

def Exercice611():
    a = float(input('Premiere longeur : '))
    b = float(input('Deuxieme : '))
    c = float(input('Troisieme : '))
    tab = [a,b,c]
    if max(tab) > (sum(tab)/2):
        print('Aucun triangle ne peut etre construit.')
    else:
        if a==b or c==a or b==c:
            if a==b==c:
                return'Le Trianlge est equilateral.'
            print('Le triangle est isocele.')
        elif (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == b**2 + a**2):
            if a==b or a==c or b==c:
                print('Le triangle est rectangle et isocele')
            print('Le triangle est rectangle.')

        else:
            print('Le triangle est quelcquonque')

def Exercice613():
    note,max = map(int,input("entrez votre note et la note max : ").split(" "))
    s = (note/max) * 100
    if s>= 80:
        print('A')
    elif s>=60:
        print("B")
    elif s>= 50:
        print('C')
    elif s>40:
        print('D')
    else:
        print('E')

def Exercice614():
    list = ['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien',
'Alexandre-Benoît', 'Louise']
    for i in range(len(list)):
        print(list[i], len(list[i]),"caracteres")

def Exercice615():
    moyenne = 0
    nbre = 0
    note = 0
    tab = []
    while note>=0:
        note = int(input("Entre la note : "))
        if note>=0:
            tab.append(note)
            nbre +=1
            moyenne = sum(tab)/nbre
            print("la moyenne est de ",moyenne)
            print('La note maximale est',max(tab))
            print('La note minimale est',min(tab))
    print('Le programme se termine car tu a entre une note negative.')

def Exercice616():
    m = 10000
    mprime = 10000
    d = int(input("Entrez une distance superieur ou egale a 5cm : "))
    d2 = d*(10**-2)
    for loop in range (8):

        F = ((6.67e-11*10000**2) / d2**2)
        print('d = .',d2,'m : la force vaut',round(F,3),'N')
        d2 = d2*2
# p.68

def table(base):
    resultat = []
    n =1
    while n < 11:
        b = n * base
        resultat.append(b)
        n = n +1
    return resultat
# p.70
def cube(n):
    i = 1
    s = 1
    while i <= n:
        s = s*n
        i = i+1
    return s
def cubesimple(n):
    return n**3
def volumeSphere(r):
   return 4 * 3.1416 * cube(r) / 3
# r = input('Entrez la valeur du rayon : ')
# print('Le volume de cette sphère vaut', volumeSphere(float(r)))
from turtle import*
def carre(taille):
    "fonction qui dessine un carré de taille et de couleur déterminées"
    c =0
    while c <4:
        forward(taille)
        right(90)
        c = c +1
# p.74
def ligneCar(n,ca):
    for loop in range(n):
        print(ca, end=' ')
def surfCercle(r):
    return pi*r**2
def volBoite(x1,x2,x3):
    return round(x1*x2*x3,3)

# p.77
def question(quest,essais = 3,please = 'OUi ou Non, s.v.p !'):
    while essais >0:
        reponse =input(quest)
        if reponse in ('o','Oui','O','oui','OUI'):
            return 'YEEEEE'
        if reponse in ('n','N','Non','non','NON'):
            return 'Fuck you'
        print(please)
        essais = essais -1
    print('T trop biiiippp on ne peut malheureusement rien faire pour toi')

def oiseau(voltage, etat='allumé', action='danser la java'):
    print('Ce perroquet ne pourra pas', action)
    print('si vous le branchez sur', voltage, 'volts !')
    print("L'auteur de ceci est complètement", etat)

# Exercice 7.10
def IndexMaxi(liste):
    v = 0
    max = 0
    Indice = 0
    while v <len(liste):
        if liste[v]>max:
            max = liste[v]
            Indice = v
        v = v+1
    return Indice
# ou
def IndexMaxiBis(liste):
    v = max(liste)
    return liste.index(v)

# p.78
def VolBoite(x1=8,x2=10,x3=10):
    return x1*x2*x3
def VolBoiteBis(x1 = -1, x2=-1,x3=-1):
    if x1 == -1:
        return -1
    elif x2 == -1:
        return x1**3
    elif x3 == -1:
        return x1*x1*x2
    else:
        return round(x1*x2*x3,2)

def changeCar(ch,ca1,ca2,debut=0,fin = -1):
    tab = []
    if fin ==-1:
        fin = len(ch)-1
    i,nch =0,""

    for i in range(len(ch)):
        if ch[i] == ca1 and debut<=i<= fin+1:
            nch = nch +ca2
        else:
            nch = nch + ch[i]
    print(nch)

def eleMax(liste,debut=0,fin=-1):
    max = 0
    if fin ==-1:
        fin = len(liste)-1

    for i in range (debut,fin+1):
        if liste[i]>max:
            max = liste[i]
    return max

obFichier = open("Monfichier",'a')
obFichier.write('Bonjour, fichier !')
obFichier.write("Quel beau temps, aujourd'hui !")
obFichier.close()

def copieFichier(source, destination):
    "copie intégrale d'un fichier"
    fs = open(source, 'r')
    fd = open(destination, 'w')
    while 1:
        txt = fs.read(50)
        if txt =="":
            break
        fd.write(txt)
    fs.close()
    fd.close()
    return


# Impossibilite de modifier une varaible globale dans une fonction
# Sauf si on utilise la fonction globale

# p.179
def dicdecopain():
    dico = {}
    while True:
        nom = input('Entrez le nom de votre copain : ')
        age,taille = input('Entre lage et la taille du copain en les separants dun espace : ').split()
        continuez = input('Si vous voulez arreter appuyer sur j sinon appuyer sur une autre touche : ')
        dico[nom]= int(age),float(taille)
        if continuez == ('j'or 'J'):
            break
        else:
            continue
    return dico
"""
dico = {'David':(18,1.83),'Ethan':(18,1.75),'Esther':(18,1.70)}
def consultation():

    global dico
    while True:
        nom = input('Entrez le nom de votre copain : ')
        print('Nom : '+ nom+'- age : '+str(dico[nom][0])+' ans - taille :'+str(dico[nom][1])+' m')
        continuez = input('Si vous desirez une autre fiche dinformations appuyer sur j sinon appuyer sur une autre touche : ')
        if continuez == ('j'or 'J'):
            continue
        else:
            break

def echange(dico):
    dico2 = {}
    for key,val in dico.items():
        dico2[val]= key
    return dico2

texte= 'les saucisses et saucissons secs sont dans le saloir'
dc = {}
for let in texte:
    dc[let] = dc.get(let,0)+1
print(dc)

fichier = open('texteeee.txt','w')
fichier.write('Bonjour je mappelle David je vis en charente Maritime David je mappelle')
fichier.close()
fichier = open('texteeee.txt','r')
txt = fichier.read()
dico = {}
for i in txt.split():
    if i not in dico:
        dico[i] = []
        dico[i].append(txt.index(i))
    else:
        dico[i].append(txt.index(i))
print(dico)





for i in txt.split():
    if i.isalpha()==True:
        dico[i] = dico.get(i,0)+1
liste = list(dico.items())
liste.sort()
print(liste)
fichier.close()
a,h,k = 1,2,45.67
f = open('nombres','wb')
pickle.dump(a,f)
pickle.dump(h,f)
pickle.dump(k,f)
f.close()
f = open('nombres','rb')
numero1 = pickle.load(f)
numero2 = pickle.load(f)
numero3 = pickle.load(f)
f.close()
print(numero3)

def existe(fname):
    try:
        f = open(fname,'r')
        f.close()
        return 1
    except:
        return 0
filename = input("Veuillez entrer le nom du fichier : ")
if existe(filename):
    print("Ce fichier existe bel et bien.")
else:
    print("Le fichier", filename, "est introuvable.")

Exercice 9.1 a fairee!!!!!!!!!!

                        {0:d} --> formatage en decimale
                        {0:b} --> formatage en binaire
                        {0:x} --> formatage en hexadecimale

Exercice 10.33
nomjours = ['Jeudi','Vendredi','Samedi','Dimanche','Lundi','Mardi','Mercredi']
mois = ['Janvier','Fevrier','Mars','Avril','Mai','Juin','Juillet','Aout','Septembre','Octobre','Novembre','Decembre']
nombre = [31,30,31,30,31,30,31,31,30,31,30,31]
i = 0
for k,v in zip(mois,nombre):
    for loop in range(1,v+1):
        print(nomjours[i],loop,k)
        i+=1
        if i == 7:
            i =  0

import datetime
class Point:
    def __init__(self,name,birthday):
        self.full_name = name
        self.birthday = birthday
        birthday = str(birthday)
        self.year = birthday[0:4]
        self.month = birthday[4:6]
        self.day = birthday[6:]


user = Point('Mamane',20010731)
print(user.year)"""








