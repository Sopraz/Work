import random
import time


board = []
def affichePlateau(n):

    global board
    print('-------------')
    if board == []:
        for i in range(n):
            board.append([])
            for g in range(n):
                board[i].append(' _ ')
    for k in range(n):
        print('|',end='')
        for g in range(len(board[k])):
            print(board[k][g],end='')
            print('|',end='')
        print()
        print('-------------')
        print()

def coupjoueur(n,symbole):
    global board
    try:
        ligne = int(input('Entrez le numero de la ligne : '))
        colonne = int(input('Entrez le numero de la colonne : '))
        if board[ligne-1][colonne-1] == ' _ '  :
            board[ligne-1][colonne-1] = symbole
        else:
            print('choisissez une case non occupé !')
            coupjoueur(n,symbole)

    except IndexError:
        print('Choisisser deux autre numero qui rentre dnas les normes lol: ')
        coupjoueur(n,symbole)
    affichePlateau(n)

def coupOrdinateurAlea(n,symbole):
    global board
    ligne = random.randint(1,n)
    colonne = random.randint(1,n)
    if board[ligne-1][colonne-1] == ' _ ':
        board[ligne-1][colonne-1] = symbole
    else:
        return coupOrdinateurAlea(n,symbole)
    time.sleep(1)
    print("Coup joué par l'ordinateur : "+'('+str(ligne)+','+str(colonne)+')')
    affichePlateau(n)


def gagneEnLigne(n,symbole):
    global board
    i = 0
    x = 0
    for loop in range(n):
        for x in range(n):
            if board[loop][x] == symbole:
                i+=1
            else:
                i = 0

        if i == n:
            return True
        else:
            i = 0
    return False

def gagneEnColonne(n,symbole):
    global board
    i = 0
    x = 0
    for loop in range(n):
        for x in range(n):
            if board[x][loop] == symbole:
                i+=1
            else:
                i = 0

        if i == n:
            return True
        else:
            i = 0
    return False

def gagneEndiagonale(n,symbole):
    global board
    i = 0
    x = 0
    for loop in range(n):
        if board[loop][x] == symbole:
            i+=1
        else:
            i = 0
        x+= 1
    if i == n:
        return True
    i = 0
    x = n-1
    for loop in range(n):
        if board[loop][x] == symbole:
            i+=1
        else:
            i = 0
        x-= 1
    if i == n:
        return True
    return False

def ghagne(n,symbole):
    if (gagneEndiagonale(n,symbole)==True) or (gagneEnLigne(n,symbole)==True) or (gagneEnColonne(n,symbole)==True):
        return True
    return False

def partieAlea(n):
    affichePlateau(n)
    global board
    final = False
    for loop in range(n+2**(n-2)):
        coupjoueur(n,' X ')
        if ghagne(n,' X ') == True:
            return 'Vous avez gagne'
        else:
            coupOrdinateurAlea(n,' O ')
            if ghagne(n,' O ') == True:
                return "L'ordinateur a gagne..."

    return 'Partie Nulle'

def lancement():
    case = int(input('Choisissex le nombre/chiffre de lignes/colonnes (superieur ou egal a trois bien sur) :'))
    if case >= 3:
        partieAlea(case)
    else:
        print('Vous avez entrer un nombre/chiffre inferieur a trois bouricots !')
        lancement()




lancement()














