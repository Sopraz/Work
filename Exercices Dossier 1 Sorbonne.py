# Monday 9 december 2019

from math import*
# Specification de fonction 1.3.1 dossier 1 p.21
def perimetre(longeur,largeur):
    return (longeur + largeur)*2
def valeur_absolue (x):
    if x>= 0:
        print(x)
    else:
        print(-x)
# Je sais plus
def deux_egaux(x,y,z):
    return (x ==y) or (x==z) or (y==z)

def triangle_quelconque(x,y,z):
    return not deux_egaux(x,y,z)

# Exercice (2.1) : Variables et affectations (corrigé) p.55
def sante(x):
    if x == 37.5:
        return 'oklm'
    else:
        return 'Malade'

# 2.2.1 Exemple de calcul avec variable : l’aire d’un triangle Formule de Heron
def aire_triangle(a,b,c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

# Exercice 2.6 Mesures Fiables
# Question 1
def egale_eps (a,b,eps):
    return eps >abs (a -b)
# Question2
def egal_eps_hard(v1,v2,v3,eps):
    if egale_eps (v1,v2):
        if egale_epseps(v1,v3):
            if egale_eps(v2,v3):
                return 1
            else:
                return 2/3
        else:
            if egale_eps(v2,v3):
                return 2/3
            else:
                return 0

    elif egale_eps(v2,v3):
        if egale_eps(v1,v3):
            return 2/3
        else:
            return 0
    else:
        return 0
# autre possibilite
def autre_pos(v1,v2,v3,esp):
    esp1 = egale_eps(v1,v2)
    esp2 = egale_eps(v1,v3)
    esp3 = egale_eps(v2,v3)

    if (esp1 and esp2 and esp3):
        return 1
    elif (esp1 and esp2) or (esp1 and esp3) or (esp2         and esp3):
        return 2/3
    else:
        return 0
# 3.2.3 Tracer l'interpretation des boucles avec print

def somme_entiers(n):
    i = 0
    s = 0
    print("=================")
    print("A l'initialisation i = ", i)
    print("A l'initialisation s = ", s)
    while i<n:
        print("----------------")
        i = i+1
        s = i+s
        print("i est egale a :", i)
        print("s est egale a :", s)
    print("=================")
    print("le resultat est donc :",s)
    print("=================")

# 3.3.2 Calcul d’une somme ou d’un produit dossier 1 p, 77
def somme_suite_geo (bornsup):
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
# 3.3.3 Calcul du PGCD dossier 1 p. 79
def pgcd (a,b):
    y = 0
    while a%b != 0:
        y = a%b
        a = b
        b =y

    return b
# 3.3..4 Boucles Imbriquees dossier p. 81
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

# 10 December 2019


# 3.4.1 Exemple 1 : calcul des éléments d’une suite arithmétique p.83
def suite(n,k,f):
    i = 0
    u = k
    while i<n:
        u = f(u)
        i = i +1
    return u
def suite_f(x):
    return 1*x + 2
# Exercice
def somme_suite_ar(n,k,f):
    i = 0
    u = k
    while i<n:
        u = f(u)
        i = i+1
    return (n+1)*((k+u)/2)
def produi_suite_ar(n,k,f):
    i = 0
    u = k
    somme = k
    while i <n:
        u= f(u)
        i = i+1
        somme = somme *u
    return somme
def suite_geo(k,puis,premierterme):
    i = 1
    nombre = k
    while i<puis:
        nombre = nombre *k
        i = i+1
    return nombre *premierterme
# 3.4.2 Annulation d'une fnction sur un intervalle
def annulation(borninf,bornsup,f):
    i = borninf

    while i<bornsup:
        if f(i) == 0:
            return True
        i = i+1

    else:
        return False
def racine(x):
    return math.sqrt(x)
def inverse(x):
    return 1/x

# Exercice 3.1 Somme des impairs corrigés
def somme_impair_inf(n):
    i = 1
    somme = 0
    while i<=n:
        somme = somme +i
        i = i+2
    return somme
def somme_premiers_impairs(x):
    i = 1
    s = 0
    y=1
    while y<=x:
        s = s +i
        i = i+2
        y = y+1
    return s

# 3.3 Fonction mystère
def f(x,y):
    z=0
    w = x
    if x<=y:
        while w<=y:
            z = z+ w*w
            w = w+1
        return z
    else:
        return z

# Exercice (3.4) : Nombres premiers (corrigé)
def divise(n,p) :
    # if p%n == 0:
    #     return True
    # else:
    #     return False
    return p%n == 0# plus simple
def est_premier(n):
    if n>2:
        i = 2
        b = True
        while b and i<n:
            if divise(i,n) :
                b = False#b ici non necessaire
            else:
                i = i+1
        return b
    elif n == 2:
        return True
    else:
        return False
def est_premier2(n):
    if n>2:
        i = 2
        while i<n:
            if divise(i,n) :
                return False
            else:
                i = i+1
        return True
    elif n == 2:
        return True
    else:
        return False

# 4. Les boucles
def puissance(x,n): # avec boucle
    i = 1
    res = 1
    while i != n + 1 :
        res = res*x
        i = i+1
    return res
def puissance2(x,n): # la simplicité
    return x**n

# 4.1 Notion de correction
def puissance(x,n):
    i = 1
    res = 1

    while i<=n:
        res = res*x
        i = i+1

    return res

# 4.3.1 Factorisation de calcul

def aire_triangle(a,b,c):
    p = (a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**0.5

# 4.3.2 plus petit diviseur
def plus_petit_diviseur(m):
    n = 2
    d = 0
    nombre_tb = 0
    while (d==0) and n<=m:
        nombre_tb = nombre_tb +1
        if m%n ==0 and d ==0:
            d = n

        n = n+1
    print("le nombre de tour de boucle est:", nombre_tb)
    return d

def plus_PD(n):
    d = 0
    y =2
    while (d==0) and y<n:

        if n%y == 0:
            d = y
        else:
            y = y+1
    return d

# 4.4 La récursion
def factorielle(n):
    if n <= 1:
        return 1
    else:
        return n * factorielle(n - 1)


def estpalindromenouveau(ch):
    r = ''
    for i in ch:
        r= i+r

    if r == ch:
        return True
    else:
        return False

# p.156
def suprression2(car,ch):
    result = ''
    for c in ch:
        if c != car:
            result+= c
    print(result)
def inversion(s):
    ch = ''
    i = len(s)-1
    while i >= 0:
        ch = s[i] + ch
        i -= 1
    print(ch)
def entrelacement(ch1,ch2):
    r = ''
    i = 0
    if len(ch1)>=len(ch2):
        longue = ch1
        moinslongue = ch2
    else:
        longue = ch2
        moinslongue = ch1
    while i < len(moinslongue):
        r += ch1[i]+ch2[i]
        i += 1
    if len(longue) != (moinslongue):
        r +=  longue[i:]
    return r

# p.154
def liste_pair(n):
    tab =[]
    for i in range(2,n+1):
        if i%2 == 0:
            tab.append(i)
    print(tab)

# p.174
def liste_longeurs_chaines(l):
    tab = []
    for i in  l:
        tab.append(len(i))
    return tab

def liste_sommes_cumulees(l):
    tab =[]
    s = 0
    for i in l:
        s +=i
        tab.append(s)
    return tab

def interclassement(L1,L2):
    i1 = 0
    i2 = 0
    tab = []
    while (i1 <len(L1)) and (i2<len(L2)):
        if L1[i1]<=L2[i2]:
            tab.append(L1[i1])
            i1 +=1
        else:
            tab.append(L2[i2])
            i2+=1
    if i1<len(L1):
        tab+= L1[i1:]
    else:
        tab+= L2[i2:]
    return tab

def repetition(ch,nbre):
    tab = []
    for i in range(nbre):
        tab.append(ch)
    return tab
def repetition_bloc(ch,nbre):
    tab = []
    for i in range(nbre):
        tab+= ch
    return tab

def est_croissante(l):
    if len(l>1):
        for i in range(1,len(l)):
            if l[i]<l[i-1]:
                return False
        return True
    else:
        return True

def est_croissante_bis(l):
    i = 1
    Croissante = True
    while i<len(l)and Croissante:
        Croissante = l[i]>=l[i-1]
        i+=1
    return Croissante

def distance(p1,p2):
    x1, y1 = p1
    x2 ,y2 = p2
    return sqrt((x1-x2)**2+ (y1-y2)**2)
def majeure(p):
    prenom, nom, age, verite = p
    return age>= 18
























