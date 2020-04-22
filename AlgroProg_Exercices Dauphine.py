# Saturday 14 December
import math
import random
import time
import os
# Exercice 1.23
def deux_inconnus(a,b,c,d,e,f):
    x = (f*b-c*e)/(d*b-a*e)
    y = (c - a*(f*b-c*e))/b*(d*b-a*e)
    return x,y

# Exercice 1.22
def trois_nombres(a,b,c):
    return a ==b+c or c == a+b or b == a+c
# Exercice 2.1
def puipui(x,n):
    res = 1
    i = 1
    while i<=n:
        res =res*x
        i= i+1
    return res
# Exercice 2.2
def somme():
    i = 1
    s = 0
    while i<=100:
        s = s+i
        i= i+2
    return s
# Exercice 2.3
def entier(n):
    s=0
    i= 1
    while i<n:
        if n%i == 0:
            s= s +i
        i= i+1
    if s ==1:
        return "entier", "s =",s
    else:
        return "pas entier","s =",s
# Exercice 2.4
def entier_parfait(n):
    s=0
    i= 1
    while i<n:
        if n%i == 0:
            s= s +i
        i= i+1
    if s ==n:
        return "entier parfait"
    else:
        return "entier imparfait"
# Exercice 2.6
def jsp():
    i = 1
    j= 1
    e = 1
    while j<=4:
        while e <= 5:
            print(i,end="  ")
            i = i+j
            e = e+1
        j = j+1
        i =  1
        e  =1
        print()
# Exercice 2.7
def only_god(n):
    a = 0
    j = a
    c = "valeur sont saisies dans l'ordre croissant"
    for loop in range(n):
        a = int(input('donne un nombre:'))
        if a<= j:
            c= "les valeurs ne sont pas saisies dans l'ordre croissant"
        j = a
    return c
# Exercice 2.8
def mesoo(n):
    s_impairs = 0
    s_pairs = 0
    for loop in range(n):
        nombre = int(input("donne  un nombre:"))
        if nombre%2 == 0:
            s_pairs = s_pairs + nombre
        elif nombre%2 != 0:
            s_impairs = s_impairs + nombre
    if s_pairs == s_impairs:
        return 'La sommme des nombres paires est egale à la somme des nombres impairs'
    else:
        return "La somme des nombres paires n'est pas egale a celle des nombres impairs"
# Exercice 3.1
def maximum():
    a = int(input())
    b = int(input())
    c = max(a,b)
    return c
# Exercice 3.2
def cube(n):
    return  n**3
def volume(r):
    return 4/3*math.pi*cube(r)
# Exercice 3.3
def tableMulti(base,debut,fin):
    i = debut
    print("Fragment de la table de multiplication par ",base, ":")
    while i<=fin:
        res= i*base
        print(i,"x",base,"=", res)
        i = i+1
# Exercice 3.4
def pgcd(a,b):
    res = 0
    while a%b != 0:
        res= a%b
        a = b
        b = res
    return b
# Exercice 3.11
def AleatoireAvecRepetitions(n):
    g = 0
    occ = 0
    v = 0
    while g<n:
        i = random.randint(0,1)
        v = 0
        if i == 1:
            g = g+1

        else :
            g= 0
        occ = occ+1
    a = random.randint(0,1)
    return a, occ
def Question2(n):
    somme = 0
    for loop in range (1000):
        AleatoireAvecRepetitions(n)

# #  Exercices ginette
# def estUncarre(c):
#     return c[0:len(c)//2] == c[len(c)//2:len(c)]
# def nombreCarre(c):
#     cpt = 0
#     longeur_chaine = len(c)
#     g = 0
#     i = 1
#     for loop in range (longeur_chaine) :
#         if estUncarre(c[i: i+g]) == True:
#            cpt = cpt +1
#         g = g+2
#     g = 0
#     for loop in range (longeur_chaine):
#         if estUncarre(c[i+g:len(c)-1]) == True:
#            cpt = cpt +1
#         g = g+2
#     return cpt

# def carre2(n):
#     tableau = list(str(n))
#     somme = 0
#     for i in  range (len(tableau)):
#         tableau[i]= int(tableau[i])
#         somme = somme +tableau[i]**2
#         if somme == 1:
#             return heureux
#         else:
#             somme = 0


# Sunday 15 December

# Exercice 4.1
def algo10(n):
    tab = [0]*n
    somme = 0
    for i in range (n):
        tab[i] = int(input("Entrez une note : "))
        somme = somme + tab[i]
    moyenne = somme /n
    note_au_dessus = 0
    for i in range (n):
        if tab[i] > moyenne:
            note_au_dessus += 1
    note_max = 0
    pos = 0
    for i in range (n):
        if tab[i] > note_max:
            note_max = tab[i]
            pos = i
    return moyenne, note_au_dessus,note_max, pos
# Exercice 4.2 Pas fini
def tableau (long):
    tab =[]
    for i in range (long):
        g = int(input())
        tab.append(g)
    for i in range (long):
        if tab[i] >= 0:
            print(tab[i])
def tableau2(long):
    tab =[]
    for i in range (long):
        nombre = int(input('Entre nombre : '))
        tab.append(nombre)
    print(tab)
    tab2 = []
    for i in range (long):
        if tab[i] > 0:
            tab2.append(tab[i])
    return (tab2)
def tableau3(long):
    tab =[]
    for i in range (long):
        nombre = int(input('Entre nombre : '))
        tab.append(nombre)
    print(tab)
    for i in range (long):
        if tab[i] < 0:
            del tab[i]
    return (tab)

# Exercice 4.3
def NombreAleatoire(a,b):
     return random.randint(a,b)

def TabAleaetprod (n,a,b):
    tab = []
    for i in range (n):
        tab.append(random.randint(0,5))
    return (tab)
def TabProduit(T):
    prod = 1
    for i in range (len(T)):
        prod = prod*T[i]
    return prod
# n = int(input('Nombre Tot '))
# a = int(input('Borne inf'))
# b = int(input('Born sup '))
# Tab = TabAlea(n,a,b)
# print(Tab)
# print(TabProduit(Tab))
def TabAleaetprod (n,a,b):
    tab = []
    for i in range (n):
        tab.append(random.randint(a,b))
    prod = 1
    for i in range (len(tab)):
        prod = prod*tab[i]
    print('Le tableau est : ', tab)
    print('Le produit des elements du tableau est : ', prod)

# partiel 2019
def premier(e):
    g = 'Vrai'
    i = 1
    if e >2:
        for i in range(2,e):
            if e%i == 0:
                g = 'Faux'
        i = i+1
    return g

# La roulette de Lenzer
def roulette():
    capital = int(input('Quel est votre budget initiale :'))
    while capital >0:
        mise = int(input("Combien voulez-vous misez ? "))
        if mise <0:
            print('Vous ne pouvez pas misez une somme negative : (hmar) \n')

        elif mise >capital:
            print('Vous ne pouvez entre une mise superieur a votre capital !\n')

        else:
            numero = int(input("Entrez le numero souhaitez : (entre 0 et 49 bien sur) "))
            g = random.randint(0,49)
            time.sleep(4)
            print('Le numero sortie est le',g,'\n')
            time.sleep(3)
            if numero ==g :
                gain = 3*mise
                print('Vous etes tombe sur le numero gagnant ! (votre chatte sapparente a un tunnel...)')
                time.sleep(3)

            elif g%2 == 0 and numero%2 == 0:
                gain = ceil(1.5 * mise)
                print('Vous avez choisi la bonne couleur')
                time.sleep(3)

            elif g%2 !=0 and numero% 2 != 0:
                gain = ceil(1.5* mise)
                print('Vous avez choisi la bonne couleur !')
                time.sleep(3)

            else :
                gain = 0
            capital = capital - mise + gain
            print ('Vous avez gagné', gain,'euros\n')
            if capital >0:
                print('Votre capital est donc de ',capital,'euros')
                desir = (input('Voulez vous rejouer ? (entrez oui ou non) \n'))
                if desir == 'non':
                    return 'Vous avez donc gagné', capital,'euros'

                else:
                    print('J aime les gens qui ont le gout du risque ! ')
            else:

                print ("Vous n'avez plus d'argent, vous ne pouvez donc plus jouer")
                time.sleep(2)
                print('wola mskn')
# Exercice 5.1
# Il retourne la chaine d caractere en remplacant les marques de ponctiations par des p
# Exercice5.2
def palindrome(ch):
    chnew = ''
    for loop in range(-1,-len(ch)-1,-1):
        chnew += ch[loop]
    return chnew == ch

# exercice 5.3
def split(ch):
    g = ch.split()
    for loop in range (len(g)):
        if len(g[loop])>3:
            print(g[loop],end=' ')

# Exercice 5.4
def leN(texte):
    i = 0
    a = 0
    espace2 = len(texte)-3
    for a in range (len(texte)):
        if 1<= a< len(texte)-1 :
            print(texte[a]+i*' '+texte[a]+espace2*' '+texte[a])
            i += 1
            espace2 += -1
        else:
            print(texte[a]+(len(texte)-2)*' '+ texte[a])

# Exercice 5.5
def sansespaces(s):
    print(len(s))
    for loop in range(len(s)):
        if s[loop] != ' ':
            print(s[loop],end='')
def question2(s):
    s = list(s)
    for loop in range(len(s)):
        if s[loop]== " ":
            del s[loop]
    ''.join
# Exercice 5.6
def chainecar(texte):
    texte =list(texte)
    souhait  = True
    while souhait == True:
        try:
            indice  = int(input("Choisr l'indice souhaiter : "))
        except:
            print('Vous navez pas saisi de digit')
        if indice>len(texte)-1:
            print('Rerentrez un indice correct !')
            time.sleep(0.5)
        else:
            texte[indice] = '?'
            g = input('Voulez vous continuer ?')
            if (g == 'non' or g == 'n' or g == 'nn'):
                souhait = False
    print(''.join(texte))

# Exercice 5.7
def supression(texte):
    i = 0
    a = 1
    print(texte[0],end='')
    while a < len(texte):

        if texte[a] != texte[i]:
            print(texte[a],end='')
        a+= 1
        i += 1


# Exercice 5.8
def auplusunefois(texte):
    valide = True
    for loop in range (len(texte)):
        if texte.count(texte[loop])>1:
            valide = False

    return valide
def test(n,ch1,ch2):
    if ch1.count(ch2) == n and auplusunefois(ch2):
        print('oui')
    else:
        print('non')
# Exercice 5.9
def test2(ch1,ch2):
    ch =''

    while len(ch) < len(ch1):
        ch+= ch2
    if ch != ch1 or len(ch) > len(ch1):
        print('non')
    else:
        return len(ch1) // len(ch2)

# Exercice 5.10
def leX(texte):
    espace1 = 0
    espace2 = len(texte)-2
    debut = 0
    fin = -1
    if len(texte)%2 !=0:
        while texte[debut] !=  texte[fin]:
            print(espace1*' '+texte[debut]+espace2*' '+texte[fin]+espace1*' ')
            debut+=1
            fin-=1
            espace1 +=1
            espace2 -=2
        print(espace1*' '+texte[debut] )
        while espace1 != 0:
            debut-=1
            fin+=1
            espace1 -=1
            espace2 +=2
            print(espace1*' '+texte[debut]+espace2*' '+texte[fin]+espace1*' ')

    else:
        while espace2 != 0:
            print(espace1*' '+texte[debut]+espace2*' '+texte[fin]+espace1*' ')
            debut+=1
            fin-=1
            espace1 +=1
            espace2 -=2
        print(espace1*' '+texte[debut]+espace2*' '+texte[fin]+espace1*' ')
        while espace1 >= 0:
            print(espace1*' '+texte[debut]+espace2*' '+texte[fin]+espace1*' ')

            debut-=1
            fin+=1
            espace1 -=1
            espace2 +=2

# Exercice 5.11
def jesaisplus(s1,s2):
    s2 = list(s2)
    ch = ''
    for loop in range(len(s2)):

        if s2[loop] in (s1)and len(ch)<len(s1):

            ch+= s2[loop]

    if ch == s1:
        print('OK')
    else:
        print('impossible')


# Exercice 5.12
def permuteMot(mot):
    mot = list(mot)
    tab = []
    for loop in range (len(mot)):
        tab.append(mot[loop])
    random.shuffle(tab)
    return ''.join(tab)
def permute(phrase):
    g = phrase.split(' ')
    for loop in range (len(g)):
        print(permuteMot(g[loop]),end=' ')

def permuteMotbis(mot):
    ch = ''
    ch1 = mot[1:len(mot)]
    for loop in range (1,len(ch1)-1):
        i = random.randint(0,len(ch1)-2)
        ch+= ch1[i]
        ch1 = ch1[:i] +ch1[i+1:]
    return mot[0]+ch+mot[-1]


def permutephrase(texte):
    phrase = texte.split(' ')
    ch = ''
    for i in range (len(phrase)):
        ch+= permuteMot(phrase[i])+' '
    return ch

# Exercice 5.13 A finiiiiirrrrrrrrr !!!!!!
v = " ab cda fg ab   fg cda h cda    "
liste = v.split()
im = -1
def decoupage(ch):
    mot = ''
    dico = {}
    indicemot = -1
    for indice,car in enumerate(ch):
        if car.isalpha()==True:
            mot+= car
            if indicemot<0:
                indicemot=indice
        else:
            if mot not in dico:
                dico[mot] = [indicemot]
            else:
                dico[mot].append(indicemot)
            mot = ''
            indicemot = -1
    for cle,values in dico.items():
        print(cle,end=',')
        print(values)

# Exercice 6.2
def lesnotes():
    nombre = int(input('Saisir un nombre de note : '))
    max = 0
    somme = 0
    indexmax = 0
    index = 0
    for loop in range (nombre):
        note = int(input('Entrez une note : '))
        somme += note

        if note>max:
            max = note
            indexmax = index
        index+=1

    print('La moyenne de toute les notes est', somme/nombre)
    print('la note maximale est ',max)
    print('Lindex de cette note est',indexmax)

def lesnotesenliste():
    tab =[]
    nombre = int(input('Saisir un nombre de note : '))

    for loop in range (nombre):
        note = int(input('Entrez une note : '))
        tab.append(note)

    moyenne = sum(tab)/nombre
    maximum= max(tab)
    indexmax = tab.index(max(tab))
    print('La moyenne de toute les notes est', sum(tab)/nombre)
    print('la note maximale est ',maximum)
    print('Lindex de cette note est',indexmax)


# Exercice 6.3
def LasuiteU(n):
    u0 = 1
    u1 =2
    tab = [1,2]
    i = 2
    while i <= n:
        u = 5*u1 + 10*u0
        u0 = u1
        u1 = u
        tab.append(u)
        i += 1
    print(tab)

# Exercice 6.4
def sommeliste(L1,L2):
    tab = []
    if len(L1)>len(L2):
        listemax= L1
        listemin = L2
    else:
        listemax = L2
        listemin = L1
    i = 0
    while i<len(listemax):
        if i <len(listemin):
            tab.append(L1[i]+L2[i])
        else:
            tab.append(listemax[i])
        i+= 1
    print(tab)


# Exercice 6.5
def plusieursliste():
    l = []
    nbresslistes = int(input('Combien de sous liste voulez vous ? '))
    for i in range (nbresslistes):
        nbres = map(int,input('Entre, en les separant par des espaces autant de nombres que vous voulez.').split(' '))
        g = list(nbres)
        l.append(g)
    print(l)

# Exercice 6.6
def moyenneleve(eleve,liste):
    s = 0
    nbrenote = 0
    for i in range (len(liste)):
        if liste[i][0] == eleve:
            s+= liste[i][2]
            nbrenote += 1
    return s/nbrenote

# Exercice 6.9
def multiplede7():
    nbre = int(input('Combien de multiples de 7 voulez-vous afficher ? '))
    multiple = int(input('Quel multiple choisissez vous ?'))
    nbremultiple = 0
    for i in range (1,nbre+1):
        g =i*7
        if g%3 == 0:
            nbremultiple += 1
            print(g)
        else:
            print(g,end=' ; ')
    print()
    print('Vous avez affiche {} multiple de {}'.format(nbremultiple,multiple))

# Exercice 6.1
def listenombre():
    nombre= int(input())
    tab  = []
    for loop in range(nombre):
        enteir = int(input())
        tab.append(enteir)
    print(tab)

# Exercice 6.12
def beaucoup():
    noms = []
    notes = []
    nbreed = int(input("Combien d'etudiants ya t-il ? "))
    for i in range(nbreed):
        nom  = input('Nom etudiant : ')
        note = int(input('Sa note : '))
        noms.append(nom)
        notes.append(note)

    print('La moyenne est de : ', sum(notes)/(len(notes)-1))
    for g in range (len(notes)):
        if notes[g]>= 10:
            print(noms[g], 'est admis')
        elif notes[g] >0:
            print(noms[g], 'est recalé')

# Exercice 6.13
def liredistance():
    distance = []

    for i in range(5):
        distance.append([]*5),
    print(distance)

def f(k, taille, Liste): #it's like liste.sorted()
    for j in range(k+1, taille):
        if Liste[k] > Liste[j]:
            x = Liste[k]
            Liste[k] = Liste[j]
            Liste[j] = x

# Exercice 7.7
def supp_1(L, elem):
    i=0
    while (i < len(L)):

        if (L[i] == elem) :
            L.remove(L[i])
            i-=1

        i += 1
    print(L)
# Exercice 7.8
def filtrage(l):
    i = 0
    print('liste avant filtrage',l)
    while i<len(l):
        if l[i]<0:
            l.remove(l[i])
            i-=1
        i+=1
    print('liste apres filtrage',l)
def filtrageplus(l):
    i = 0
    print('liste avant filtrage',l)
    l1 = l
    while i<len(l):
        if l[i]<0:
            l.remove(l[i])
            i-=1
        i+=1
    print('liste apres filtrage',l)
    print(l1)

# Exercice 7.9
def listeAlea(n,a,b):
    l = []
    for loop in range(n):
        l.append(random.randint(a,b))
    return l
def absent():
    s = 0
    nombre = 0
    g = listeAlea(1000,0,99)
    for i in range (100):
        if i not in g:
            s+= i
            nombre +=1

    return nombre, s/nombre


# Exercie 7.10
# Algorithme Rapide
def sommemgle(S,a,b):
    s = 0
    for i in range (a-1,b):
        s+= S[i]
    return s



def Coupemin1(S):
    min = sum(S)
    g= 0
    v= 1
    while g<len(S)-1:
        for i in range(g,len(S)-1):
            for k in range(v,len(S)):
                if sommemgle(S,i+1,k+1) < min:
                    min = sommemgle(S,i+1,k+1)

            v+= 1
            g+= 1
    return min
def coupeinul(i,S):
    min = sum(S[i-1:])
    g = i-1
    s = 0
    while g<len(S):
        for i in range(g,len(S)):
            s += S[i]
        if s<min:
            min = s
        s = 0
        g+= 1
    return min
def coupei(S):
    g = len(S)
    min = sum(S[:])
    s = 0
    while g!=0:
        for i in range(0,g):
            s+= S[i]
        if s<min:
            min = s
        s = 0
        g-=1
    return min

# def coupeMin2(S):  Trop plicomque
#     g = len(S)-1
#     i = 0
#     for i in (S[0],S[-1]):
#         coupei
#

# Exercice 7.11
def premier(mot): #peut mieux faire
    g = list(mot)
    ch = ''
    tab = []
    for i in range(len(g)):
        if g[i]!= ' ':
            ch = ch+g[i]

        else:
            tab.append(ch)
            ch = ''
    final = ''
    for loop in range(len(tab)):
        final = tab[loop]+' '+final
    return ch + ' '+ final

def seconde(mot):
    g = mot.split(' ')
    for i in range(-1,-len(g)-1,-1):
        print(g[i],end=' ')

# Exercice 7.12
def salle(E,c):
    liste = []
    for i in range (c):
        g = random.randint(0,len(E)-1)
        liste.append(E[g])
        E.remove(E[g])
    return liste
def affectation(E,S):
    final = []
    for i in range(len(S)):
        capacite = S[i]
        v = salle(E,capacite)
        final.append([v,i])
    return final

# def emargement(l):

# Exercice 8.3
def bienplaces(Secr,Test):
    bien = 0
    for i in range(len(Secr)):
        if Secr[i] == Test[i]:
            bien += 1
    return bien

def malplace(Secr,Test):
    pasbien = 0
    for i in range(len(Secr)):
        if Secr[i] != Test[i]:
            pasbien += 1
    return pasbien

def conversion(nombre):
    conv = str(nombre)
    tab = []
    for i in range (len(conv)):
        tab.append(conv[i])
    return tab

def Mastermind(chmin,chmax,longeurcode):#Pas la bonne fonction mais le jeu marche quand meme
    codesecret = []
    for i in range(longeurcode):
        g = random.randint(chmin,chmax)
        car = str(g)
        codesecret.append(car)
    nbreessais = int(input("Combien dessai voulez vous ? "))
    for i in range(nbreessais):
        saisi = int(input('Saisir un nombre a '+ str(longeurcode)+' chiffre : '))
        g = bienplaces(codesecret,conversion(saisi))
        k = malplace(codesecret,conversion(saisi))
        print('Bien places : ',(g))
        print('Mal places : ',(k))
        if conversion(saisi) == codesecret:
            return 'Bravo ! Vous avez gagne'
        elif i == nbreessais -1:
            break
        else:
            print('Il vous reste '+ str(nbreessais)+ ' essais')
    print('Vous avez depenser tout vos essais, vous avez perdu')

def genere(n,a):
    secret = []
    for loop in range(a):
        secret.append(random.randint(1,a))
    return secret
def entableau(s):
    g = str(s)
    tab = []

    for i in range(len(g)):
        tab.append(int(g[i]))
    print(tab)
def copie(source):
    tab= []
    for i in range(len(source)):
        tab.append(source[i])
    return tab
def verification(L,l):
    print("Nombre d'elements bien places : ", bienplacesbis(L,l))
    print("Nombre d'elements mal places : ", malplacesbis(L,l))
def bienplacesbis(l,L):
    bien = 0
    for i in range(len(l)):
        if l[i] in L:
            if l[i] == L[i]:
                bien+= 1
    return bien
def malplacesbis(Secr,Test):
    pasbien = 0
    for i in range(len(Secr)):
        if Secr[i] in Test:
            if Secr[i] != Test[i]:
                pasbien+= 1
    return pasbien
def Mastermindbon(n,b,nb_essai):#A comprendre plus tard avec quelqun de fort
    g = genere(1,b)
    while nb_essai != 0:
        chiffre = int(input('Saisir un nombre de 5 chiffres (entre 1 et'+ str(b) + ') : '))
        v = bienplacesbis(g,entableau(chiffre))
        k = malplacesbis(g,entableau(chiffre))
        print("Nombre d'elements bien places : ",v)
        print("Nombre d'elements mal places : ",k)
        nb_essai -= 1
        if bienplacesbis(g,entableau(chiffre)) == n:
            return 'Bravo'
        else:
            print('Il vous reste ', nb_essai,'essais.')
    return 'Vous avez perdu'

# Exercice 9.1
def suiteUlol(n):
    if n == 0:
        return 10
    else:
        return 0.2*suiteUlol(n-1)+3
def iterativite(n):
    i0 = 10
    for i in range(1,n+1):
        u = 0.2*i0+3
        i0 = u
    return i0

# Exercice 9.2 # pgcd
def mystere(a,b):
    if (a == 0 or b == 0):
        return 0
    elif a == b:
        return a
    elif a > b:
        return mystere(a-b, b)
    else:
        return mystere(a, b-a)

#

# Exercice 9.4
def produit(a,b):
    if b ==1:
        return a
    else:
        return a+(produit(a,b-1))
def sansOccu2(L,x):
    if L != []:
        if L[0] == x:
            L = sansOccu2(L[1:],x)
        else:
            L = [L[0]] + sansOccu2(L[1:],x)
    return L

# Exercice 9.6
def RemplaceOccu(x,ch,y):
    L =[]
    for i in range(len(ch)):
        L.append(ch[i])
    if L != []:
        if L[0] == x:
            L[0]=y
        else:
            L = L[0] + RemplaceOccu(x,ch[1:],y)
    return ''.join(L)

def Fibonnaciite(n):
    u0 =  1
    u1 = 1
    for i in range(n-2):
        u = u0 + u1
        u0 = u1
        u1 = u
    return u

def Fibonnacirecu(n):
    if n == 1 or n==2:
        return 1
    else:
        return Fibonnaci(n-1) + Fibonnaci(n-2)


# Exercice 9.8
def PGCDrecursivite(a,b):
    g = a%b
    if g == 0:
        return b
    a = b
    b = g
    return PGCDrecursivite(a,b)
# Exercice 9.9
def puissanceite(a,n):
    b =a
    for i in range(n-1):
        a = a*b
    return a

def puissancerecur(a,n):
    if n == 1:
        return a
    else:
        return a*puissancerecur(a,n-1)

# def puissancerecmaligne(a,n):
    if n%2 == 0:
        if n == 0:
            return 1
        else:
            return

# Exercice 9.10
def fac_recite(n):
    for i in range(1,n):
        n = n*i
    return n

def fac_recur(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n*fac_recur(n-1)
# Exercice 9.12
def sommeentier(debut,fin):
    if debut == fin:
        return fin
    else:
        return debut+ sommeentier(debut+1,fin)

# Exercice 9.15 A finiiirrrr !!!!
# def toursdhanoie(n,src,dest,inter):

# Exercice 10.4
def inverse(dico):
    dico2 = {}
    for i in dico:
        dico2[dico[i]]= i
    return dico2

def inverse2(dico):
    dico2 = {}
    for i in dico:
        if dico[i] not in dico2:
            dico2[dico[i]]= []
            dico2[dico[i]].append(i)
        elif dico[i] in dico2:
            dico2[dico[i]].append(i)
    return dico2

# def lirefichier(fichier):



# Exercice 10.5
# def calculFiboAvecTuple(A,B,n):
#     if n==B[0]:
#         return B[0]
#     elif n==B[1]:
#         return B[1]
#     else:
#         return -(A[0]*calculFiboAvecTuple(A,B,n-1)+A[1]*calculFiboAvecTuple(A,B,n-2                  )+A[1]*calculFiboAvecTuple(A,B,n-2))

# Exercice 10.6
# def comptage(ch):
#     dico = {}
#     for i in range(len(ch)):
#         dico[ch[i]] =ch.count(ch[i])
#     dico2 = sorted(dico)
#     for i in dico2:
#         print(i,dico[i])
# Exercice 10.7
def compte(ch,car):
    return ch.count(car)

def estAnagramme():
    ch1 = input('Saisir le premier mot : ')
    ch2 = input('Saisir le deuxieme : ')
    Anagramme = False
    if len(ch) == len(ch2):
        Anagramme = True
        for i in ch:
            if ch.count(i) != ch2.count(i):
                Anagramme = False
    return Anagramme

def Dicoo(ch):
    dico = {}
    for i in ch:
        dico[i] = ch.count(i)
    return dico
def estAnagramme2(ch,ch2):
    premier = Dicoo(ch)
    deuxieme = Dicoo(ch2)
    if premier == deuxieme:
        return True
    else:
        return False

def estAnagramme3(ch1,ch2):
    g = sorted(ch1.upper())
    v = sorted(ch2.upper())
    if g == v:
        return True
    else:
        return False

# Exercice 10.8
def trad(ch,dico):
    f = ch.lower()
    g = f.split(' ')
    for i in  (g):
        if i in dico:
            print(dico[i],end=' ')
        else:
            print(i,end=' ')

# notes2016 = {'Florian' : 'abs', 'Antoine' : 12, 'Clara' : 15, 'Robert' : 0, 'Agathe' : 8, 'Erwan' : 7, 'Zoé' : 20, 'Xavier' : 11, 'Didier' : 20, 'Alain' : 0, 'Hadi' : 12}

def supprimer(dico):
    for i in dico.copy():
        if dico[i] == 'abs':
            del dico[i]
    return dico

def moy(dico):
    moyenne = 0
    for i in dico:
        moyenne+= dico[i]
    return moyenne/len(dico)

def admioupo(dico):
    admis = []
    refuse = []
    for i in dico:
        if dico[i] >= 10:
            admis.append(i)
        else:
            refuse.append(i)
    print('Ceci est la liste des admis : ', admis)
    print('Ceci est la liste des refuse :',refuse)

def agrandissement(dico):
    nb = int(input('Combien de nv etudiants ?'))
    for i in range(nb):
        nom = input('Rentrez le nom : ')
        age = int(input('Retnrez lage : '))
        dico[nom] = age
    return dico

# Exercice 10.10
recette = {'oeufs': (3,),'Farine': (100,'g'),'Lait':(25,'cl'),'Beurre':(150,'g'),'Sachet de levure':(1,),'Chocolat':(200,'g'),'Sucre':(75,'g')}

def creerecette():
    recette ={}

    nbingredient = int(input('Entrez le nombre dingredient necessaire a la recette : '))
    for i in range(nbingredient):
        ingredient = input('Ingredient : ')
        quantite = int(input("Quantite de l'ingredient : "))
        unite = input('Unite de poid : ')
        recette[ingredient] = (quantite, unite)
    return recette

def afficherrecette():
    recette ={}
    nbingredient = int(input('Entrez le nombre dingredient necessaire a la recette : '))
    for i in range(nbingredient):
        ingredient = input('Ingredient : ')
        quantite = int(input("Quantite de l'ingredient : "))
        unite = input('Unite de poid : ')
        k = (quantite,unite)
        recette[ingredient] = k
    for i in recette :
        if  0 not in recette[i]:
            for g in recette[i]:
                print(g,end=' ')
            print(i,end=' ')
            print()

def afficherecette2():
    global recette
    print(recette)
    for i in recette :
        if  0 not in recette[i]:
            for g in recette[i]:
                print(g,end=' ')
            print(i,end=' ')
            print()
def recettepour(n):
    for i in recette:
        for g in recette[i]:
            g[0]= float(g[0])*(n/4)
    print(recette)
    # afficherecette2()

# Gestion de fichier
# A.3 Manipuler lse textes

# nom = input('Entre ton nom : ')
# nouveau = open('Test'+nom+'.txt','w')
# nouveau.write('Nonjour \t')
# nouveau.writelines(nom)
# nouveau.write('\nCeci est un teste decriture')
# nouveau.close()
# fichier = open('Test'+nom+'.txt','a')
# fichier.write('\nI wanna fuck womekfhsdans')
# fichier.close()
#

newone = open('Lestabes','w')
for i in range(2,31):
    for g in range(1,21):
        newone.write(str(i*g)+' ')
    newone.write('\n\n')
newone.close()

def lecture(fichier):
    f = open(fichier,'r')
    g = f.read()
    f.close()
    print(g)
def copieFichier(source,destination):
    g = open(destination,'w')
    v = open(source,'r')
    h = v.read()
    g.write(h)
    g.close()
    v.close()
#
# nouveau1 = open('premier.txt','w')
# nouveau1.write("Voici un texte cree en\n2017\na l'Universite Paris-Dauphine")
#
# nouveau1.close()
# k = open('premier.txt','r')
# khad = k.readlines()
# print(khad)
# for i in khad:
#     hj = i.split(' ')
#     for ig in hj:
#         print(ig,end='   ')
# k.close()

def copieFichierMiseAJour(source,destination):
    g = open(destination,'w')
    v = open(source,'r')
    h = v.read()
    h = h.replace('2017','2018')
    g.write(h)
    g.close()
    v.close()

# nouveau2 = open('valeurs','w')
# nouveau2.write((str(14.89)+'\n'))
# # nouveau2.write('\n')
# nouveau2.write((str(7894.6)+'\n' ))
# # nouveau2.write('\n')
# nouveau2.write((str(123.278)+'\n' ))
# nouveau2.close()
#
# nouveau2 = open('valeurs','r')
# new2 = open('copiefichiervaleurs','w')
# val = nouveau2.readlines()
# for i in val:
#     new2.write(str(round(float(i)))+'\n')
# new2.close()

# nombre = int(input('Combien detudiants ya til ? '))
# newfichier = open('NotesGr1.txt','w')
# for i in range(nombre):
#     nom, prenom = input("Entrez le nom et prenom de l'etudiant").split(' ')
#     note = int(input('Entrez la note de letudiant : '))
#     newfichier.writelines(nom+' '+prenom+'\t'+str(note)+'\n')
# newfichier.close()
# lecture('NotesGr1.txt')

def lectureFichier(nom):
    tab = []
    new = open(nom,'r')
    g = new.readlines()
    for i in g:
        i = i.strip('\n')
        tab.append(i)
    return tab
    new.close()
    # for i in range(len(nom))

def ecritureFichier(nom,liste):
    new = open(nom,'w')
    for i in liste:
        new.write(i+'\n')
    new.close()

def triFichier(nom):
    tab = lectureFichier(nom)
    nouveaufichier = open(nom+'_trie.txt','w')
    newtab = sorted(tab)
    ecritureFichier(nom+'_trie.txt',newtab)
    nouveaufichier.close()


def triFichier2(N):
    new = open('NotesAmphie_trie.txt','w')
    for i in range(1,N+1):
        g = triFichier('NotesGr'+str(i)+'.txt')
        lecture = open('NotesGr'+str(i)+'_trie.txt','r')
        v = lecture.readlines()
        for k in v:
            new.write(k)
    new.close()

def fact(n):
    if n ==1 or n ==0:
        return 1
    else:
        return n*fact(n-1)

def binome(n,p):
     return fact(n)/(fact(p)*fact(n-p))


def triangle(n):
    for i in range(n+1):
        print(round(binome(n,i)),end=' ')


















