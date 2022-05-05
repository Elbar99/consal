from random import *
from tkinter import *
import time

n= 10 # nb de lignes
p = 12 # nb de colonnes
bord = min(n,p)//5 # distance au bord
tableau = [[0 for j in range(p)] for i in range(n)]
tableau[(n-1)//2][(p-1)//2] = 1

def voir_tableau():
    for i in range(n):
        for j in range(p):
            tableau[i][j]
        #print()
    return
#voir_tableau()

def est_libre(i,j):
    if i>0 and tableau[i-1][j]: # au dessus
        return False
    if i<n-1 and tableau[i+1][j]: # en-dessous
        return False
    if j>0 and tableau[i][j-1]: # à gauche
        return False
    if j<p-1 and tableau[i][j+1]: # à droite
        return False
    return True


def est_dedans(i,j):
    if (0 <= i < n) and (0 <= j < p):
        return True
    else:
        return False
    

def lancer_un_bloc(k):
    i = randint(0+bord,n-1-bord)
    j = randint(0+bord,p-1-bord)
    while est_dedans(i,j) and est_libre(i,j):
        dx = randint(-1,1)
        dy = randint(-1,1)
        i = i + dx
        j = j + dy
    if est_dedans(i,j):
        tableau[i][j] = 1
    return i,j
#lancer_des_blocs(5)

def faire_lancer_des_blocs(s):
    for l in range(s):
        j = randint(0+bord,p-1-bord)
        lancer_un_bloc(j)
    return

n = 100 # nb de lignes
p = 150 # nb de colonnes
bord = min(n,p)//10 # distance au bord pour lancement
echelle = 5
tableau = [[0 for j in range(p)] for i in range(n)]
tableau[(n-1)//2][(p-1)//2] = 1 # Centre
nb_blocs = 200
root = Tk()
canvas = Canvas(root, width=p*echelle, height=n*echelle, background="white")
canvas.pack(fill="both", expand=True)




def afficher_tableau():
    canvas.delete("all") # Efface tout
    for i in range(n):
        for j in range(p):
            if tableau[i][j]:
                canvas.create_rectangle(j*echelle,i*echelle,j*echelle+echelle-1,i*echelle+
                echelle-1,width=1,fill='green')
    return

run = True

def action_bloc():
    if run:
        faire_lancer_des_blocs(30)
    #lancer_un_bloc(30)
        afficher_tableau()
        
    root.after(100, action_bloc)
    
    return

def start():
   global run
   run= True
    
def stop():
   global run
   run= False

def close_window():
    root.destroy()
    
bouton_bloc = Button(root,text="Lancer des blocs", width=20, command=action_bloc)
bouton_bloc.pack(side= LEFT)
start= Button(root, text= "Start",width=20 ,command= start)
start.pack(padx= 10,side= LEFT)
button = Button(text = "Quit",width=20, command = close_window) 
button.pack(side= RIGHT)
stop= Button(root, text= "Stop",width=20, command= stop)
stop.pack(padx= 15,side= RIGHT)
 

###### act3
n = 80 # nb de lignes
p = 90 # nb de colonnes
tableau = [[0 for j in range(p)] for i in range(n)]
def voir_tableau():
    for i in range(n):
        for j in range(p):
            tableau[i][j]
            #print()
    return
#voir_tableau()
def peut_tomber(i,j):
    if i == n-1: # tout en bas
        return False
    if tableau[i+1][j]: # case juste en-dessous
        return False
    if j>0 and tableau[i][j-1]: # à gauche
        return False
    if j<p-1 and tableau[i][j+1]: # à droite
        return False
    return True
def faire_tomber_un_bloc(j):
    i = 0
    while peut_tomber(i,j):
        i = i + 1

    tableau[i][j] = 1
    return i,j
def faire_tomber_des_blocs(k):
    for l in range(k):
        j = randint(0,p-1)
        faire_tomber_un_bloc(j)
        voir_tableau()
        print()
    return
n= 80 # nb de lignes
p = 90 # nb de colonnes
tableau = [[0 for j in range(p)] for i in range(n)]
echelle = 6 # échelle
nb_blocs = 200
root = Tk()
canvas = Canvas(root, width=p*echelle, height=n*echelle, background="white")
canvas.pack(fill="both", expand=True)
#canvas.config(bg="green")
canvas.delete("all") 
def afficher_tableau():
    for i in range(n):
        for j in range(p):
            if tableau[i][j]:
                canvas.create_rectangle(j*echelle,i*echelle,j*echelle+echelle-1,i*echelle + echelle-1,width=1,fill='green')
    return

run = True

def action_bloc():
    if run:
        faire_tomber_des_blocs(30)
        afficher_tableau()
        
    root.after(1000, action_bloc)
    
    return

def start():
   global run
   run= True
    
def stop():
   global run
   run= False
    
def close_window():
    root.destroy()

bouton_bloc = Button(root,text="Afficher blocs", width=15, command=action_bloc)
bouton_bloc.pack(pady=10,side=LEFT)
start= Button(root, text= "Start",width=15, command= start)
start.pack(padx= 10, side=LEFT)
button = Button(text = "Quit",width=15 , command = close_window) 
button.pack(side=RIGHT)
stop= Button(root, text= "Stop",width=15 , command= stop)
stop.pack(padx= 15, side= RIGHT)

    
    
    
    
    
    
    
    
    
    
    
    
root.mainloop()
