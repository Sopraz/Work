#Monday 9 December 2019

import math
import random
import os
def from_TTCtoHT(prixTTC,taux):

    HT = prixTTC / (1+ taux/100)
    return HT

def polynomiale (a,b,c,x) :
    discriminant = ((a*x**2 + b)*x**2) + c
    return discriminant

def perimetre(longeur,largeur):
    return largeur * longeur
    return longeur + largeur

def valeur_absolue (x):
    if x>= 0:
        print(x)
    else:
        print(-x)

def deux_egaux(x,y,z):
    return (x ==y) or (x==z) or (y==z)

def triangle_quelconque(x,y,z):
    return not deux_egaux(x,y,z)

def sante(x):
    if x == 37.5:
        return 'oklm'
    else:
        return 'Malade'

def suite_geo (bornsup):
    s = 0
    y = 0
    while y<= bornsup:
        s = s+ ((1/2)**y)
        y = y+1
    return s
def puissance (x,n):
    y = 1
    somme = 1
    while y <= n:
        somme = somme *x
        y = y+1
    return somme

def pgcd (a,b):
    y = 0
    while a%b != 0:
        y = a%b
        a = b
        b =y

    return b

def couple (n):
    i = 0
    j = 0
    nombre = 0
    while i <= n:
        j = 0
        while j <= n:
            if j != i:
                print("couple(",i,";",j,")")
                nombre = nombre +1
            j = j+1
        i = i +1
    return nombre


def aire_couronne(n):
    aire =  math.pi * n**2
    return aire

# Exercice 2.2 : volume d'un tetraedre
def tetraedre (a,b,c,d,e,f):
    x = a**2 + b**2 - d**2
    y = b**2 + c**2 - e**2
    z = a**2 + c**2 - f**2
    p = 4 * a**2 * b**2 * c**2
    q = a**2*y**2 + b**2*z**2+c**2*x**2
    r = x*y*z
    V = 1/12*math.sqrt(p-q+r)
    return V

# Exercice 3.4 : Nombre premiers
def nombre_premiers(n):
    if n >=2 :
        y = 2
        while y<n:
            if n%y == 0:
                return False
            else:
                y = y +1
        return True

    else:
        return False

# Exercice 3.5 : Suite de Fibonacci
def Suite_fibonnaci(n):
    f0 = 0
    f1 = 1
    y = 2
    a = 0
    while y<=n:
        a = f0 + f1
        f0 = f1
        f1 =a
        y = y +1
    return a
# Question 3 :
def fibo_diff(n):
    a = Suite_fibonnaci(n)
    b = Suite_fibonnaci(n-1)
    c = a/b
    return c
# Question 4 :
def fibro_approx(n):
    return (fibo_diff(41)**n)/math.sqrt(5)

# Exercice 3.6 : Encadrements

# Question 1 : Partie entière
def partie_entiere(n):
    i = 0
    if type(n) == float:
        while  i<n:
            i = i+1

        return i-1
    else:
        return n
# Question 2 : Encadrement large
def encadrement_large(x,ec):
    if x > ec:
        return (partie_entiere(x)+1) - ec
    else:
        return 0
# Question 3 :
def partie_entiere2(n):
    return encadrement_large(n,1)

# Exercice 3.7: Approx racine carrée
def suite_approx(x, n):
    u0 = 1
    u = 0
    i = 1
    if n>=1:
        while i<=n:
            u = (u0 +(x/u0)) /2
            u0 = u
            i = i+1
        return u
    else:
        return 1
# Question 2 :
def approx_racine_stable(x):
    u0 = 1
    u = 0
    n = 357402
    while u <n:
        u = (u0 +(x/u0)) /2
        if u == u0:
            return u
        else :
            u0 = u
# Question 3 :
def approx_racine_eps(x, e):
    u0 = 1
    u = 0
    n = 357402
    while u <n:
        u = (u0 +(x/u0)) /2
        if abs(u-u0) >=e:
            u0 = u
        else:
            return u

#Exercice 3.8 : Indicatrice d'Euler
# Question 1 :
def pgcd(a,b):
    c = a%b
    while c != 0:
        a = b
        b= c
        c = a%b
    return b
# Question 2 :
def euler(n):
    if n !=1 :
        m=1
        nombre= 0
        while m<= n-1:
            if pgcd (m,n) ==1:
                nombre = nombre + 1
            m = m+1
        return nombre
    else:
        return 1

# Exercice 3.9 : Lancers de dés (TME)
def lancer_de6():
    u = random.random()
    g = 0.166666666
    if u<g:
        return 1
    elif u<2*g:
        return 2
    elif u < 3*g:
        return 3
    elif u<4*g:
        return 4
    elif u<5*g:
        return 5
    else:
        return 6
def lancer_de62():
    return random.randint(1,6)

# Question 3 : Moyenne d'une serie de lancers
def moyenne_plusieurs_lancers(n):
    random.seed(n)
    for loop in range (n):
        lancer_de6()

# Question 4 : Fréquence d'une valeur aléatoire
def frequence_valeur(r, x):
    occurence = 0
    for loop in range (x):
        lancer_de6()
        if lancer_de6() == r:
            occurence = occurence +1
    return occurence /x
# Question 5 : Lancer dé à n faces
def lancer_deN(n):
    return random.randint(1,n)
# Bonus
def occurence_deN(face,nbFace,tirages):
    occurence = 0
    for loop in range(tirages):
        random.randint(1,nbFace)
        if random.randint(1,nbFace) == face:
            occurence = occurence +1
    return occurence/tirages

# Exercice 4.1 : Retour sur la factiorelle
# Question 1
def factorielle(x):
    i = 1
    res = 1
    while i<=x:
        res = res*i
        i = i+1
    return res

# Exercice 4.2 : Somme des cubes
def somme_Cubes(n):
    i =1
    res =0
    while i <=n:
        res = res + puissance(i,3)
        i = i+1
    return res
def somme_Cubes_rapide(n):
    s = ((n*(n+1))/2)**2
    return s

# Exercice 4.4 : Couples et intervalles
def nb_couples_intervalles(a,b):
    nb_couples = 0
    x = a
    g = x+1
    while g <=b:
        while x<g:
            nb_couples += 1
            x = x+1
        g = g+1
        x = a
    print(nb_couples)


def nb_couple_divise_trace(i,j):
    nb_couples = 0
    x = i
    g = x+1
    cpt = 0
    while cpt < j-i:
        while g <=j:
            print("couple (",x,",",g,")")
            if g%x ==0:
                nb_couples += 1
                print("---------------")
                print(x, "divise",g,"!")
                print("---------------")

            g = g+1
        x = x+1
        g = x+1
        cpt+= 1
    return nb_couples
def nb_couple_divise(i,j):
    nb_couples = 0
    x = i
    g = x+1
    cpt = 0
    while cpt < j-i:
        while g <=j:
            if g%x ==0:
                nb_couples +=1
            g = g+1
        x = x+1
        g = x+1
        cpt+= 1
    return nb_couples

def existe_couples_divise(i,j):
    nb_couples = 0
    x = i
    g = x+1
    cpt = 0
    while cpt < j-i:
        while g <=j:
            if g%x ==0:
                nb_couples +=1
            g = g+1
        x = x+1
        g = x+1
        cpt+= 1
    return nb_couples>0

def existe_couples_(i,j):
    b = True
    if nb_couple_divise(i,j)>0:
        return b
    return not b

def existe_couples_divise_rapide_trace_tour(i,j):
    b = True
    test = 1
    nb_couples = 0
    x = i
    g = x+1
    cpt = 0
    while cpt < j-i:
        while g <=j:
            if g%x ==0:
                print("nombre de couples testés : ", test)
                return b
            g = g+1
            test = test+1
        x = x+1
        g = x+1
        cpt+= 1
    print("nombre de couples testés : ",test)
    return not b
def existe_couples_divise_trace_tour(i,j):
    b = False
    test = 0
    nb_couples = 0
    x = i
    g = x+1
    cpt = 0
    while cpt < j-i:
        while g <=j:
            if g%x ==0:
               b = True
            g = g+1
            test = test+1
        x = x+1
        g = x+1
        cpt+= 1
    print("nombre de couples testés : ",test)
    return b

# Exercice 4.6:
def decalage (i,j):

    if i == 8:
        return 0
    if j == 9:
        return  1
    return i+j

def encodage (a,b):
    nombre = "1"
    texte = str(a)
    for loop in range (len(texte)):
            nombre = nombre + str(decalage(int(texte[loop]),b))

    nombre = nombre + str(b)
    finale = int(nombre)
    return finale

# Exercice 4.7 : Combinaisons
def factoriellepourla896emefois(n):
    k =1
    res= 1
    nb_ops = 0
    while k <= n:
        res = res*k
        k = k+1
        nb_ops += 1
    print("Nombre d'opération = ",nb_ops)
    return res

def combinaisons(n,k):
    return factorielle(n)/(factorielle(k)*factorielle(n-k))

# Exercice 5.2 : Fonction mystère (corrigé)
def nb_chiffre(a):
    b=0
    for c in a:
        if c >= '0' and c <= '9': b=b+1
    return b


# Exercice 5.3
def est_voyelle(c):
    b = False
    if (c == 'a') or (c == 'A') or (c == 'e') or (c == 'E') or (c == 'i') or (c == 'I') or (c == 'o') or (c == 'O') or (c == 'u') or (c == 'U') or (c == 'y') or (c == 'Y') :
        b = True
    return b

def nb_voyelles(n):
    nbre = 0
    for loop in range (len(n)):
        if est_voyelle(n[loop]):
            nbre += 1
    return nbre

def sans_voyelles(a):
    ch = ''
    for loop in range (len(a)):
        if est_voyelle(a[loop]):
            ch = ch + ''
        else:
            ch = ch + a[loop]
    print (ch)

def mot_mystere(a):
    ch = ''
    for loop in range (len(a)):
        if est_voyelle(a[loop]):
            ch = ch + "_"
        else:
            ch = ch + a[loop]
    print (ch)

def est_palindrome(a):
    s = False
    alenver = ''
    for loop in range (-1,-(len(a))-1,-1):
        alenver += a[loop]
    if alenver == a:
        s = True
    return s

def miroir(a):
    g = ''
    i = len(a)-1
    while i >=0:
        g += a[i]
        i -= 1
    print(a+g)

def suppression (c,s):
    tab = []
    tab2 = []
    for loop in range(len(s)):
        tab.append(s[loop])
    for loop in range (len(tab)):
        if tab[loop] != c :
            tab2.append(tab[loop])
    texte = "".join(tab2)
    print(texte)

def suppression_debut(c, s):
    tab = []
    i = 0
    g = 1
    for loop in range(len(s)):
        tab.append(s[loop])
    while i <= len(tab)-1:
        if tab[i] == c and g >0:
            del tab[i]
            g -=1
        i +=1
    texte = ''.join(tab)
    return texte
def suppression_derniere(c,s):
    tab = []
    i = 0
    tab2 = []
    for loop in range(len(s)):
        tab.append(s[loop])
    cpt = tab.count(c)
    while i <= len(tab)-1:
        if tab[i] == c:
            cpt -= 1
            if tab[i] == c and cpt ==0:
                del tab[i]
        i +=1
    texe = ''.join(tab)
    return texe

# def supderniereplussimple(car,ch):
#     result = ''
#     i = len(s)-1
#     while i >= 0:


# Brins d'ADN

def base_comp(n):
    if n == 'A':
        return 'T'
    if n == 'G':
        return 'C'
    if n == 'T':
        return 'A'
    if n == 'C':
        return 'G'

def brin_comp(n):
    i = len(n)-1
    chaine = ''
    while i >=0:
        chaine = chaine +base_comp(n[i])
        i -= 1
    return chaine

def test_comp(n,p):
    if len(n) == len(p):
        return n == brin_comp(p)
    else:
        return False

def test_sous_sequencearnaque(b1,b2):
    return b1 in b2

def chiffre(a):
    return ord('a') - ord('0')


def caracteres(s):
    return str(s)

# Exercice 5.8
def compression(ch):
    somme = 1
    res = ''
    i= 0
    while i < len(ch)-1:
        if ch[i] == ch[i+1]:
            somme+= 1
        else:
            if somme>1:
                res+= str(somme)+ ch[i]
            else:
                res+= ch[i]
            somme = 1
        i+=1
    if somme > 1:
        return res+str(somme)+ch[i]
    else:
        return res+ch[i]

def decompression(mot):
    res = ''
    i = 0
    while i < len(mot):
        if mot[i].isalpha()== True:
            res+= mot[i]
            i+=1
        else:
            res+= int(mot[i])*mot[i+1]
            i+= 2
    return res


def moins_lettre(c,a):
    if a.count(c)>0:
        return suppression_debut(c,a)

def anagramme(m1,m2):
    a = m1.lower()
    b = m2.lower()
    if len(a) == len(b):
        for i in b:
            a = suppression_debut(i,a)
        if len(a)== 0:
            return True
        else:
            return False

# Exercice 6.7
Comptine = ['am', 'stram', 'gram', 'pic', 'pic', 'col', 'gram']
def decoupage_simple(l,a,b):
    tab = []
    for i in range (a,b):
        tab.append(l[i])
    return tab
def decoupage_pas(l,a,b,c):
    tab = []
    for i in range (a,b,c):
        tab.append(l[i])
    return tab


# Exercice 6.9
def jonction(L,c):
    return c.join(L)

def separation(s,c):
    g = s.split(c)
    tab = []
    for i in range(len(g)):
        tab.append(g[i])
    return tab

# Exercice 7.4
def alignement(l):
    alignement = True
    for i in range(len(l)-1):
        for v in range (2):
            if l[i][v] % l[i+1][v]:
                alignement = false

# Exercice 9.3
def frequences(liste):
    dic = {}
    for i in liste:
        dic[i] = liste.count(i)
    print(dic)

# Exercice 7.5 : Base de données des étudiants

BaseUPMC = [('GARGA', 'Amel', 20231343, [12, 8, 11, 17, 9]), ('POLO', 'Marcello', 20342241, [9, 11, 19, 3]),
            ('AMANGEAI', 'Hildegard', 20244229, [15, 11, 7, 14, 12]),
            ('DENT', 'Arthur', 42424242, [8, 4, 9, 4, 12, 5]),
            ('ALEZE', 'Blaise', 30012024, [17, 15, 20, 14, 18, 16, 20]),
            ('D2', 'R2', 10100101, [10, 10, 10, 10, 10, 10])]

def note_moyenne(liste):
    if len(liste)>0:
        return sum(liste)/len(liste)
    else:
        return 0

def moyenne_generale(liste):
    somme = 0
    for i in liste:
        for g in i:
            if type(g) ==list:
                somme+=note_moyenne(g)
    return somme/len(liste)

def top_etudiant(liste):
    moyenne_max = 0
    index = 0
    for i in liste:
        for g in i:
            if type(g) ==list:
                v = note_moyenne(g)
                if v> moyenne_max:
                    moyenne_max = v
                    index = liste.index(i)

    return liste[index][:2]

def recherche_moyenne(num_etudiant, liste):
    for i in liste:
        for g in i:
            if g == num_etudiant:
                return note_moyenne(i[-1])

# Exercice 7.6 : Intersection de listes
def intersection_2_listes(liste1,liste2):
    listedef = []
    for i in liste1:
        if i in liste2 and (i not in listedef):
            listedef.append(i)
    return listedef

def intersection(L):
    listedef = []

    for i in L[0]:
        presence = True
        for loop in range(1,len(L)):
            if loop == len(L)-1 and i in L[loop] and presence == True:
                listedef.append(i)
            else:
                if i not in L[loop]:
                    presence = False

    return listedef

# Exercice 7.8: Fichiers texte et systeme de facturation
def chargement_fichier(nom_fichier):
    L1=[]
    L2=[]
    with open(nom_fichier,'r') as f:
        L1=f.readlines()

    for ligne in L1:
        if ligne!= '' and ligne[-1]== '\n':
            L2.append(ligne[:-1])
        else:
            L2.append(ligne)
    return L2

def sauvegarde_fichier(nom_fichier, Contenu):
    with open(nom_fichier,'w') as f:
        for ligne in Contenu:
            f.write(ligne)
            f.write('\n')
    return None


l = ['Papillon voltige','Dans un monde','Sans espoir.','(Kobayashi Issa)']

def decoupage_mot(str):
    return str.split()

def Lecture_produit(str):
    v = decoupage_mot(str)
    v[1] = int(v[1])
    v[2] = float(v[2])
    return tuple(v)


def lecture_commande(liste):
    liste_def = []
    for i in liste:
        g  = Lecture_produit(i)
        liste_def.append(g)
    return liste_def


def lecture_commande1(liste):
    for i in liste:
        i = Lecture_produit(i)
    return liste

def gen_facture(listeprod):
    liste = ['Produit  Prix',
 '-------  ----',]
    s= 0
    for i in listeprod:

        ch = ''

        prix = i[1]*i[2]
        s+=prix
        ch+= i[0]+'  '+str(prix)
        liste.append(ch)

    HT = 'Total_HT'+'   '+str(s)
    TVA = 'TVA_20%'+'   ' + str(0.2*s)
    TTC = 'Total_TTC'+'   '+str(0.2*s+s)
    liste.append('\n')
    liste.append(HT)
    liste.append(TVA)
    liste.append(TTC)
    return liste

def commande():
    nb = int(input('Combien darticles avez vous ? '))
    liste = []
    for loop in range(nb):
        # article = input('Entrez le nom de larticle, son prix a lunite et la quantite de larticle a lunite (approximativement) : ')
        article = input('Entrez le nom de larticle : ')
        prix = int(input('Entrez son prix a lunite : '))
        quantite = int(input('Sa quantite en nombre dunite : '))
        k = article+' '+str(prix)+' '+str(quantite)
        liste.append(k)
    sauvegarde_fichier("lamandeco.txt",liste)
    facture = gen_facture(lecture_commande(liste))
    sauvegarde_fichier('facture.txt',facture)

#  Exercice 8.4 : Crible d'Erastosthène
def liste_non_multiple(nb,liste):
    liste2 = []
    for i in liste:
        if i%nb != 0:
            liste2.append(i)
    return liste2

def eratosthene(n):
    liste = []
    for i in range(2,n):
        if nombre_premiers(i):
            liste.append(i)
    return liste

def liste_facteurs_premiers(n):
    g = eratosthene(n)
    listedef = []
    for i in g:
        if n%i == 0:
            listedef.append(i)
    return listedef

# Exercice 8.5 : Codage ROT13
def liste_caracteres(str):
    return list(str)

def chaine_de(liste):
    return ''.join(liste)

# Exercice 8.7 : Triplets numériques
def triplets(n):
    tab = []
    for i in range(1,n+1):
        for g in range(1,n+1):
            for k in range(1,n+1):
                tuple = i,g,k
                tab.append(tuple)
    return tab

def decomposition(n):
    tab =[]
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                if i+j == k:
                    tuple = i,j,k
                    tab.append(tuple)
    return tab

def encadrements(n):
    tab =[]
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                if i<=j<=k:
                    tuple = i,j,k
                    tab.append(tuple)
    return tab

# Exercice 9.1 : Differences symetrique
def diff_sym(dic1,dic2):
    tab = []
    for i in dic1:
        if i not in  dic2:
            tab.append(i)
    for g in dic2:
        if g not in dic1:
            tab.append(g)
    return sorted(set(tab))
def diff_sym2(set1,set2):
    return sorted(set1^set2)


# Exercice 9.2 : Magasin en ligne
def prix_moyen(dico):
    somme = 0
    for i in dico.values():
        somme+=i
    return somme/len(dico)
def fourchette_prix(borne1,borne2,dico):
    tab = []
    for i,v in dico.items():
        if borne1<= v<= borne2:
            tab.append(i)
    return sorted(set(tab))
def fourchettesprix2(borne1,borne2,dico):
    for k,v in dico.items():
        if borne1<=v<=borne2:
            print(k)

def prix_achats(dico1,dico2):
    somme = 0
    for k,v in dico2.items():
        if k in dico1:
            somme += dico1[k]*v
    return somme

# Exercice 9.3 : Repetitions dans les listes
def repetes(liste):
    liste2 = []
    for i in liste:
        if liste.count(i)>1:
            liste2.append(i)
    g = sorted(liste2)
    return set(g)

def sans_repetes(liste):
    liste2 = []
    for i in liste:
        if  i not in liste2:
            liste2.append(i)

    return liste2

def uniques(liste):
    s = set()
    g = sorted(liste)
    for i in g:
        if g.count(i)==1:
            s.add(i)
    return s

def frequences(liste):
    dic = {}
    for i in liste:
        dic[i] = liste.count(i)
    return dic

def repetes_fois(nb,liste):
    s = set()
    for i in liste:
        if liste.count(i)==nb:
            s.add(i)
    return s


# Exercice 9.4 : Recettes de cuisine
Dessert = {
'gateau chocolat' : {'chocolat', 'oeuf', 'farine', 'sucre', 'beurre'}, 'gateau yaourt' : {'yaourt', 'oeuf', 'farine', 'sucre'},
'crepes' : {'oeuf', 'farine', 'lait'},
'quatre-quarts' : {'oeuf', 'farine', 'beurre', 'sucre'},
'kouign amann' : {'farine', 'beurre', 'sucre'}
}
def nb_ingredients(dico,key):
    print(len(dico[key]))


def recette_avec(dico,ingredient):
    s = set()
    for i in dico.keys():
        if ingredient in dico[i]:
            s.add(i)
    return s

def tous_ingredients(dico):
    s = set()
    for i in dico.keys():
        for g in dico[i]:
            if g not in s:
                s.add(g)
    return s

def table_ingredients(dico):
    dico2 = {}
    for i in tous_ingredients(dico):
        s = set()
        for cle in dico.keys():
            if i in dico[cle]:
                s.add(cle)
        dico2[i] = s
    return dico2


def ingredient_principal(dico):
    max = 0
    v = ''
    for cle,valeurs in table_ingredients(dico).items():
        longeur = len(valeurs)
        if longeur >max:
            v = cle
            max = longeur
    return v

def recettes_sans(dico,ingredient):
    dico2 = {}
    for i in dico.keys():
        if ingredient not in dico[i]:
            dico2[i] = dico[i]
    return dico2


# Exercice 10.1 : Compréhensions en vrac

Dico = {'xx':'bli', 'yzy':'blo', 'cuicui':'toutou', 'miaou':'toutou' }
Ens = { 2.7, 4.12, 3.31, 8.29, 1.13, 12.31 }
t = ['a', 'b', 'c', 'c', 'a', 'b', 'c', 'b', 'b' ]
dic = {'b','c','a'}
Liste = [ 2, 5, 12, 31, 2, 17, 31, 42, 2 ]


# Exercice 10.3 : Multi-ensembles
def melements_list(jsp):
    ds = set()
    for i in jsp:
        ds.add(i)
    return sorted(ds)

def mdict_de_mlist(liste):
    dico = {}
    for i in liste:
        dico[i] = liste.count(i)
    return dico

def convert_dict_in_list(dico):
    tab = []
    for cle,values in dico.items():
        for loop in range(values):
            tab.append(cle)
    return tab

def minter_dict(dico1,dico2):
    dico = {}
    for key,values in dico1.items() :
        if key in dico2:
            dico[key] = min(values,dico2[key])
    return dico

def minter_list(liste1,liste2):
    liste = []
    for i in liste1 :
        if i in liste2 and i not in liste:
            for loop in  range(min(liste1.count(i),liste2.count(i))):
                liste.append(i)
    return liste

def munion_list(liste1,liste2):
    liste = liste1 + liste2
    return sorted(liste)

# Exercice 10.4 : Gestion de bibliotheques

def auteurs(base):
    for val1,val2 in base.values():
        print(val1)

def titres_empruntables(base):
    s = set()
    for keys,value2 in base.items():
        if value2[1]>0:
            s.add(keys)
    return s

def titres_auteurs(auteur,base):
    s = set()
    for i in base:
        if auteur in base[i]:
            s.add(i)
    return s

# Exercice 10.5 : Calcul de Trajets
LivresBD = {'Les misérables':('Victor Hugo', 5),
'Le dernier des Mohicans':('James F. Cooper', 0), 'Un animal doué de raison': ('Robert Merle', 6), 'Le grand Meaulnes':('Alain Fournier', 1), 'Notre-dame de Paris':('Victor Hugo', 4),
'Les comtemplations':('Victor Hugo', 0) }

def trajet_direct(base,cle1,cle2):
    if cle2 in base[cle1]:
        return True
    else:
        return False
def ajout_station(ville,correspondance,base):
    base[ville] = correspondance
    return base

def stations_atteignables(base,depart,kcorr):
    s = set()

def compte_occurrences(liste):
    k= {}
    for e in liste:
        k[e] = k.get(e,0)+1
    return k


numero = [0,1,2,3]
mots = ['zero','un','deux','trois','quatre','cinq','six','sept','huit']
g = [5,6,7,8,4,3,2]

# Exercice 10.6 : Fréquence de mots
L1 = ["et", "jamais", "je", "ne", "pleure", "et", "jamais", "je", "ne", "ris"]
# L2 : Texte
L2 = ["l'", "homme", "est", "un", "loup", "pour", "l'", "homme"]
# L3 : Texte
L3 = ["le", "loup", "est", "un", "loup", "pour", "le", "loup"]
# L4 : Texte
L4 = ["un", "homme", "vit", "une", "couleuvre"]
# L5 : Texte
L5 = ["vous", "pleurates", "ma", "mort", "helas", "trop", "peu", "certaine"]
dicoLaFontaine = {"homme": 30, "loup": 20, "agneau": 10, "cigale": 10, "fourmi": 10, "renard":10, "couleuvre": 10}
# dicoRacine : DFreq
dicoRacine = {"helas": 50, "appas": 10, "transport": 10, "mort" : 10 , "coeur": 20}
53
dicoBaudelaire = {"geant" : 15, "marcher": 15, "belle": 15, "jamais": 15, "pleure": 10, "ris": 10, "reve": 20}
Auteurs = {"Jean de la Fontaine": dicoLaFontaine, "Charles Baudelaire": dicoBaudelaire,
"Jean Racine": dicoRacine}
def occurences(L):
    dico = {}
    for i in L:
        dico[i] = dico.get(i,0)+1
    return dico

def hapax(L):
    s = set()
    for i in L:
        if L.count(i)== 1:
            s.add(i)
    return s

def frequences(L):
    dico = {}
    for i in set(L):
        dico[i] =  (L.count(i)/len(L))*100
    return dico

def union_frequences(dico1,dico2,long1,long2):
    dico = {}
    v = list(dico1)+list(dico2)
    for i in set(v):
        dico[i] = (dico1.get(i,0)*long1 + dico2.get(i,0)*long2)/(long1+long2)
    return dico

def compare(dico1,dico_auteur):
    score = 0
    for i in dico1:
        if i not in dico_auteur:
            score+= 100
        else:
            score+= abs(dico1.get(i,0)-dico_auteur.get(i,0))
    return score

def auteur(texte,auteur):
    max = 100000
    cle = ''
    for key,values in auteur.items():
        score = compare(frequences(texte),values)
        if score < max:
            max = score
            cle = key
    return cle













