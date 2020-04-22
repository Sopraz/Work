import math
import time
import os
import random
import numpy as np


"""class CompteBancaire():
    def __init__(self,nom = 'Dupont',solde = 1000):
        self.name = nom
        self.desol = solde
    def depot(self,somme):
        self.desol =  somme + self.desol
    def retrait(self,somme1):
        self.desol = self.desol - somme1
    def affiche(self):
        print('Le solde du compte bancaire de {} est de {} euros'.format(self.name,self.desol))

class Domino():
    def __init__(self,face_A = 0, face_B = 0):
        self.fA = face_A
        self.face_B = face_B
    def affiche_points(self):
        print('face A : {}  face B : {}'.format(self.fA, self.face_B))
    def valeur(self):
        return self.fA + self.face_B

class Point:
    def __init__(self,name,birthday):
        self.full_name = name
        self.birthday = birthday
        birthday = str(birthday)
        self.year = birthday[0:4]
        self.month = birthday[4:6]
        self.day = birthday[6:]

class Voiture():
    def __init__(self,marque = 'Ford',couleur = 'rouge',pilote = 'personne',vitesse = 0):
        self.mar = marque
        self.cour = couleur
        self.pilo = pilote
        self.vites = vitesse
    def choix_conducteur(self,nom):
        self.pilo = nom
    def accelerer(self,taux,duree):
        if self.pilo == 'personne':
            print('Cette voiture na pas de conducteur !')
        else:
            self.vites += taux*duree
    def affiche_tout(self):
        print('{} {} piloté par {}, vitesse = {}'.format(self.mar,self.cour,self.pilo,self.vites))

class Satellite():
    def __init__(self,nom,masse = 100,vitesse = 0):
        self.masse,self.nom,self.vitesse = masse,nom,vitesse
    def impulsion(self,force,duree):
        self.vitesse+= (force*duree)/self.masse
    def energie(self):
        return self.masse *self.vitesse**2/2
    def affiche_vitesse(self):
        print('vitesse du satellite {} = {} m/s'.format(self.nom,self.vitesse))

s1 = Satellite('Zoé', masse =250, vitesse =10)

s1.impulsion(500, 15)
s1.affiche_vitesse()
print("énergie =", s1.energie())
s1.impulsion(500, 15)
s1.affiche_vitesse()
print("nouvelle énergie =", s1.energie())


class Mammifere (object):
    caract1 = "il allaite ses petits ;"
class Carnivore (Mammifere):
    caract2 = 'Il se nourrit de la chair de ses proies ;'
class Chien(Carnivore):
    caract3 = 'son cri sappelle aboiement'
mirza = Chien()
print(mirza.caract1,mirza.caract2,mirza.caract3)

class Espaces(object):
    aa  =33
    def affiche(self):
        print(Espaces.aa)

david = Espaces()
david.affiche()

class Atome:
    tablea =[None,('Hydrogene',0),('helium',2),('lithium',4),('beryllium',5),('bore',6),('carbone',6),('azote',7),('oxygene',8),('fluor',10),('neon',10)]
    def __init__(self,nat):
        self.np, self.ne = nat,nat
        self.nn = Atome.table[nat][1]
    def affiche(self):
        print()
        print('Nom de lelelment: ',atome.table[self.np][0])
        print("{0} protons, {1} électrons, {2} neutrons".\format(self.np, self.ne, self.nn))

classe Ion(Atome):
    def __init__(self,nat,charge):
        Atome.__init__(self,nat)
        self.ne = self.ne - charge
        self.charge = charge
    def affiche(self)"
    Atome.affiche(self"
    print('Particule electrisee. Charge = '.self.charge)

class Cercle(object):
    # Construction dun cercle
    def __init__(self,rayon):
        self.r = rayon
    def surface(self):
        return 3.14*(self.r**2)
class Cylindre(Cercle):
    # Construction dun cylindre
    def __init__(self,rayon,hauteur):
        Cercle.__init__(self,rayon)
        self.h = hauteur
    def volume(self):
        return Cercle.surface(self)*self.h

class Cone(Cylindre):
    def __init__(self,rayon,hauteur):
        Cylindre.__init__(self,rayon,hauteur)
    def volume(self):
        return Cylindre.volume(self)/3


class JeuDeCartes(object):
    Jeu de cartes
    # attributs de classe (communs à toutes les instances) :
    couleur = ('Cœur','Carreau','Trèfle','Pique')
    valeur = (0, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'valet', 'dame', 'roi', 'as')

    def __init__(self):
        self.carte = []
        for col in range(4):
            for val in range(13):
                self.carte.append((val+2,col))

    def nom_carte(self,c):
        return '{} de {}'.format(self.valeur[c[0]],self.couleur[c[1]])

    def battre(self):
        return shuffle(self.carte)

    def tirer(self):
        if len(self.carte)>0:
            v =  self.carte[0]
            del (self.carte[0])
            return v
        else:
            return None




joueurA = JeuDeCartes()
joueurA.battre()
joueurB = JeuDeCartes()
joueurB.battre()
pointA = 0
pointB = 0
for n in range(53):
    c = joueurA.tirer()
    g = joueurB.tirer()
    if (c and g)== None:
        print('Plus de carte')

    else:
        print('carte du joueur A',joueurA.nom_carte(c))

        print('carte du joueur B',joueurB.nom_carte(g))
        if c[0]>g[0]:
            pointA+=1
            print('Joueur A gagne et a ',pointA,'point')
        elif c[0]<g[0]:
            pointB+= 1
            print('Joueur B gagne et a ',pointB,'point')
        else:
            continue
        print()
        time.sleep(1)
print('le joueur A a',pointA,'point ')
print('le joueur B a',pointB,'point ')
if pointA > pointB:
    print('Donc le joueur A a gagner')
elif pointA < pointB:
    print('Donc le joueur B a gagner')
else:
    print('No one won')





class CompteBancaire(object):
    def __init__(self,nom = 'Dupont',solde = 1000):
        self.name = nom
        self.desol = solde
    def depot(self,somme):
        self.desol =  somme + self.desol
    def retrait(self,somme1):
        self.desol = self.desol - somme1
    def affiche(self):
        print('Le solde du compte bancaire de {} est de {} euros'.format(self.name,self.desol))


class CompteEpargne(CompteBancaire):
    def __init__(self):
        CompteBancaire.__init__(self,nom = 'Dupont',solde = 1000)
        self.taux = 0.3
    def changeTaux(self,valeur):
        self.taux = valeur
    def capitalisation(self,nombreMois):
        self.mois = nombreMois
        print('Capitalisation sur ',self.mois,'mois au taux mensuel de',self.taux,'%')
        self.desol += self.taux*self.desol """

# Cour Sacha Dray
# class Sub(object):
#     def __init__(self):
#         self.visible = 'Visible'
#         self.__invisible__ = 'Yes'
#         self.__invisible = 'Erreur du coup'
#
# class Deux(Sub):
#     def __init__(self):
#         Sub.__init__(self)
#         print(self.__invisble)
#
# class Liste(object):
#     def __init__(self,liste_students):
#         self.liste = liste_students
#         self.cours = {}
#     def get_students(self):
#         return self.liste [:]
#     def add_grade(self,student,grade):
#         self.cours[student] = grade
#
# liste1 = Liste ([i for i in range(1,11)])
# for i in liste1.liste:
#     liste1.add_grade(i,100)
#
# print(liste1.cours)

def main():
    ls = [1, 2, 3]
    running_sum(ls)
    print('Running sum of [1, 2, 3] is:', ls)
def running_sum(ls):
    for i in range(1,len(ls)):
        ls[i] = ls[i-1]+ls[i]

main()







































