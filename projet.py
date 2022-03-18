from tkinter import *

p = 15
n = 30

grill =  [[0 for j in range(p)] for i in range(n)]
# print(tableau)
def peut_tomber(i,j):
    if grill[n][j] != 0:
        grill[n-1][j] = 1
    if grill[i][j] != 0:
        grill[i-1][j] = 1
    if (grill[i][j-1] or grill[i][j+1]) != 0:
        grill[i][j] = 1
        

def faire_tomber_un_bloc(j):
    

def faire_tomber_des_blocs(k):
    pass


#Arbres browniens)
def est_dedans(i,j):
    pass

def faire_libre(i,j):
    pass

def lancer_un_bloc():
    pass

def lancer_des_blocs(k):
    pass



