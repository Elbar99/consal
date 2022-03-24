from tkinter import *
from random import *

p = 6
n = 4

grill =  [[0 for j in range(p)] for i in range(n)]
# print(tableau)

def peut_tomber(i,j):
    if i == n-1: # tout en bas
        return False
    if grill[i+1][j]: # case juste en-dessous
        return False
    if j>0 and grill[i][j-1]: # à gauche
        return False
    if j<p-1 and grill[i][j+1]: # à droite
        return False
    return True


def faire_tomber_un_bloc(j):
    i = 0
    while peut_tomber(i,j):
        i = i + 1
        grill[i][j] = 1
    return i,j


def faire_tomber_des_blocs(k):
    for l in range(k):
        j = randint(0,p-1)
        faire_tomber_un_bloc(j)
        l+1
    return

def afficher():
    for i in range(n):
        for j in range(p):
            print(grill[i][j], end="")
        print()
    return
afficher()

#Arbres browniens)
def est_dedans(i,j):
    pass

def faire_libre(i,j):
    pass

def lancer_un_bloc():
    pass

def lancer_des_blocs(k):
    pass



