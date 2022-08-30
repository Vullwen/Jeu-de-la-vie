#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX#
#                                                                          #
#   _               _                  _        _        __     __         #
#  | |    ___      | | ___ _   _    __| | ___  | | __ _  \ \   / (_) ___   #
#  | |   / _ \  _  | |/ _ \ | | |  / _` |/ _ \ | |/ _` |  \ \ / /| |/ _ \  #
#  | |__|  __/ | |_| |  __/ |_| | | (_| |  __/ | | (_| |   \ V / | |  __/  #
#  |_____\___|  \___/ \___|\__,_|  \__,_|\___| |_|\__,_|    \_/  |_|\___|  #
#                                                                          #
#                                                                          #
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX#

#XXXXXXXXXXXXXXXXXXXXXXXXX#
#---------Imports---------#
#XXXXXXXXXXXXXXXXXXXXXXXXX#
from tkinter import *
import time
import random
from tkinter import messagebox
import webbrowser

#XXXXXXXXXXXXXXXXXXXXXXXXX#
#---------Fenêtre---------#
#XXXXXXXXXXXXXXXXXXXXXXXXX#

width,height= 980 ,599
window = Tk()
window.title("jeu de la vie")
window.geometry("980x647")
window.config(background = '#BA9B9B')
rectangle = Frame(window, width=width, height=height)
rectangle.pack()
dessin = Canvas(rectangle, width=width, height=height)
dessin.pack()

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX#
#----Création-de-la-cellule----#
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX#

class Cell:
    """
    Classe 'Cell' qui a pour vocation de créer les différentes cellules de la matrice
    """
    def __init__(self,i, j):
        """
        Constructeur de la classe 'Cell'
        : type i : int
        : type j : int
        """
        self.actuel = False
        self.futur = None
        self.neo_ref_matrix = (i, j)

    def finger_of_god(self):
        """
        Fonction 'finger_of_god' qui change le statut d'une cellule
        """
        self.actuel = not self.actuel

class Grille:
    """
    Classe 'Grille' qui a pour but de faire apparaitre la grille
    """
    def __init__(self,x=15,y=15,taille_cell=15):
        """
        Constructeur de la classe 'Grille'
        : type x : int
        : type y : int
        : type taille_cell : int
        """
        self.x = x
        self.y = y
        self.taille_cell = taille_cell

    def pipistrelle(self):
        """
        Fonction 'pipistrelle' qui gère la création de la matrice et son remplissement
        """
        global pedoncule
        global fichtre
        fichtre = []
        pedoncule = []
        for i in range(70):
            pedoncule.append([])
            fichtre.append([])
            for j in range(70):
                rect = dessin.create_rectangle(self.x, self.y, self.x+self.taille_cell,self.y+self.taille_cell, fill="white")
                fichtre[i].append(rect)
                pedoncule[i].append(Cell(i, j))
                self.x += self.taille_cell
            self.x = self.taille_cell
            self.y += self.taille_cell


def les_cours_dart_plastique():
    """
    Fonction 'les_cours_dart_plastique' qui affiche graphiquement les cellules
    """
    for i in pedoncule:
        for j in i:
            if j.futur != j.actuel:
                x, y = j.neo_ref_matrix

                if j.futur:
                    dessin.itemconfig(fichtre[x][y], fill="black")

                else:
                    dessin.itemconfig(fichtre[x][y], fill="white")

                j.finger_of_god()



def change_de_bio_linkedin(cell):
    """
    Fonction 'change_de_bio_linkedin' qui gère les règles du jeu de la vie
    : type cell : objet
    : return : bool
    """
    carabistouille = 0
    x, y = cell.neo_ref_matrix
    for i in (x-1, x, x+1):
        for j in (y-1, y, y+1):
            if i == x and j == y:
                continue
            if i == -1 or j == -1:
                continue
            try:
                if pedoncule[i][j].actuel:
                    carabistouille += 1
            except IndexError:
                pass
    if cell.actuel == True:
        return not( carabistouille == 2 or carabistouille == 3 )
    else:
        return carabistouille == 3


def le_menage(*args):
    """
    Permet de tuer toutes les cases
    """
    for i in range(70):
        for j in range(70):
            if pedoncule[i][j].actuel == False:
                pass
            else:
                dessin.itemconfig(fichtre[i][j], fill="white")
                pedoncule[i][j].finger_of_god()

window.bind("<space>", le_menage)

#XXXXXXXXXXXXXXXXXXXXXXXXX#
#----Gestion des clics----#
#XXXXXXXXXXXXXXXXXXXXXXXXX#

def rick_asley(event):
    """
    Fonction 'rick_asley' qui fait naitre les cellules en fonction du clique du joueur
    : type event : int
    """

    #print (event.x, event.y)
    x, y = int((event.x//15)*10), int((event.y//15)*10)
    iy = int( x / 10 ) - 1
    ix = int( y / 10 ) - 1
    if ix == -1 or iy == -1:
        raise IndexError
    if pedoncule[ix][iy].actuel:
        dessin.itemconfig(fichtre[ix][iy], fill="white")
    else:
        dessin.itemconfig(fichtre[ix][iy], fill="black")
    pedoncule[ix][iy].finger_of_god()

dessin.bind("<Button-1>", rick_asley)

#XXXXXXXXXXXXXXXXXXXXXXXXX#
#---------Boutons---------#
#XXXXXXXXXXXXXXXXXXXXXXXXX#

def zee_partii():
    """
    Fonction 'zee_partii' qui lance le code
    """
    for i in pedoncule:
        for j in i:
            if change_de_bio_linkedin(j):
                j.futur = not j.actuel

            else:
                j.futur = j.actuel
    les_cours_dart_plastique()
    if statut == 1:
        global on_off
        on_off = window.after(150, zee_partii)

#commande du bouton
statut = 0
def ClickD():
    '''
    Permet de mettre statut à 0 ou 1, en fonction de l'état du jeu (allumé/eteint).
    '''
    global statut, compteur
    if statut == 0:

        compteur = 0
        statut = 1
        print("Allumé")
        zee_partii()
    else:
        statut = 0
        print("Eteint")
        window.after_cancel(on_off)

#création du bouton play/pause
plpa = Button(window, text="Play/Pause", padx=30, pady=10, command = ClickD)
plpa.pack(side="bottom")
plpa.place(relx=0, rely=1, anchor=SW)

#création du menu de choix de préconfig
class fen_preconf:
    """
    Classe 'fen_preconf' qui s'occupe des fonctions de préconfiguration
    """
    def __init__(self):
        """
        Constructeur qui est là pour la beauté du geste
        """
        pass

    def create(self):
        """
        Fonction 'create' qui génère le menu de choix des préconfigurations
        """

        global win
        le_menage()
        win = Toplevel(window)

        preconf1 = Button(win, text="Planeur", padx=30, pady=10, command = dess_planeur)
        preconf2 = Button(win, text="101", padx=34, pady=10, command = dess_101)
        preconf3 = Button(win, text="Cthulhu", padx=34, pady=10, command = dess_cthulhu)
        preconf4 = Button(win, text="Surprise!", padx=34, pady=10, command = surprise)

        preconf1.place(relx=0.3, rely=0.2,)
        preconf2.place(relx=0.5, rely=0.2,)
        preconf3.place(relx=0.7, rely=0.2,)
        preconf4.place(relx=0.7, rely=0.2,)


        preconf1.pack()
        preconf2.pack()
        preconf3.pack()
        preconf4.pack()

    def finito(self):
        """
        Fonction qui détruit la fenètre
        """
        win.destroy()

fpc = fen_preconf()

#on génère et on applique sur la fenètre le bouton de création du menu choix
pan_conf = Button(window, text="Configurations pré-existantes", padx=30, pady=10, command = fpc.create)
pan_conf.pack(side="bottom")
pan_conf.place(relx=0.9, rely=0.966, anchor=CENTER)

#Préconfiguration
def dess_planeur():
    #ferme la fenêtre temporaire
    fpc.finito()
    #partie relou où on dessine les planeurs
    changement_preconf(17, 14)
    changement_preconf(16, 15)
    changement_preconf(16, 14)
    changement_preconf(17, 15)
    changement_preconf(16, 24)
    changement_preconf(17, 24)
    changement_preconf(18, 24)
    changement_preconf(19, 25)
    changement_preconf(15, 25)
    changement_preconf(14, 26)
    changement_preconf(14, 27)
    changement_preconf(20, 26)
    changement_preconf(20, 27)
    changement_preconf(17, 28)
    changement_preconf(15, 29)
    changement_preconf(16, 30)
    changement_preconf(17, 30)
    changement_preconf(18, 30)
    changement_preconf(19, 29)
    changement_preconf(17, 31)
    changement_preconf(16, 34)
    changement_preconf(16, 35)
    changement_preconf(15, 35)
    changement_preconf(14, 34)
    changement_preconf(14, 35)
    changement_preconf(15, 34)
    changement_preconf(15, 35)
    changement_preconf(13, 36)
    changement_preconf(17, 36)
    changement_preconf(17, 38)
    changement_preconf(18, 38)
    changement_preconf(13, 38)
    changement_preconf(12, 38)
    changement_preconf(14, 48)
    changement_preconf(14, 49)
    changement_preconf(15, 49)
    changement_preconf(15, 48)

def dess_101():
    #ferme la fenêtre temporaire
    fpc.finito()
    #partie relou où on dessine les planeurs
    changement_preconf(15, 19+4)
    changement_preconf(16, 19+4)
    changement_preconf(16, 20+4)
    changement_preconf(15, 20+4)
    changement_preconf(19, 19+4)
    changement_preconf(20, 19+4)
    changement_preconf(20, 20+4)
    changement_preconf(19, 20+4)
    changement_preconf(13, 22+4)
    changement_preconf(14, 22+4)
    changement_preconf(22, 22+4)
    changement_preconf(21, 22+4)
    changement_preconf(20, 22+4)
    changement_preconf(19, 22+4)
    changement_preconf(18, 22+4)
    changement_preconf(17, 22+4)
    changement_preconf(16, 22+4)
    changement_preconf(15, 22+4)
    changement_preconf(12, 23+4)
    changement_preconf(12, 24+4)
    changement_preconf(13, 24+4)
    changement_preconf(23, 23+4)
    changement_preconf(23, 24+4)
    changement_preconf(22, 24+4)
    changement_preconf(19, 24+4)
    changement_preconf(18, 24+4)
    changement_preconf(17, 24+4)
    changement_preconf(16, 24+4)
    changement_preconf(17, 26+4)
    changement_preconf(18, 26+4)
    changement_preconf(16, 27+4)
    changement_preconf(16, 28+4)
    changement_preconf(17, 29+4)
    changement_preconf(18, 29+4)
    changement_preconf(19, 28+4)
    changement_preconf(19, 27+4)
    changement_preconf(16, 31+4)
    changement_preconf(17, 31+4)
    changement_preconf(18, 31+4)
    changement_preconf(19, 31+4)
    changement_preconf(22, 31+4)
    changement_preconf(23, 31+4)
    changement_preconf(23, 32+4)
    changement_preconf(22, 33+4)
    changement_preconf(21, 33+4)
    changement_preconf(20, 33+4)
    changement_preconf(13, 31+4)
    changement_preconf(12, 31+4)
    changement_preconf(12, 32+4)
    changement_preconf(13, 33+4)
    changement_preconf(14, 33+4)
    changement_preconf(15, 33+4)
    changement_preconf(16, 33+4)
    changement_preconf(17, 33+4)
    changement_preconf(18, 33+4)
    changement_preconf(19, 33+4)
    changement_preconf(16, 35+4)
    changement_preconf(16, 36+4)
    changement_preconf(15, 36+4)
    changement_preconf(15, 35+4)
    changement_preconf(20, 35+4)
    changement_preconf(20, 36+4)
    changement_preconf(19, 36+4)
    changement_preconf(19, 35+4)

def dess_cthulhu():
    #ferme la fenêtre temporaire
    fpc.finito()
    #partie relou où on dessine les planeurs
    changement_preconf(14, 21+5)
    changement_preconf(15, 20+5)
    changement_preconf(16, 20+5)
    changement_preconf(17, 21+5)
    changement_preconf(17, 22+5)
    changement_preconf(16, 22+5)
    changement_preconf(15, 22+5)
    changement_preconf(14, 25+5)
    changement_preconf(15, 24+5)
    changement_preconf(16, 24+5)
    changement_preconf(17, 24+5)
    changement_preconf(18, 24+5)
    changement_preconf(19, 24+5)
    changement_preconf(20, 24+5)
    changement_preconf(20, 23+5)
    changement_preconf(21, 22+5)
    changement_preconf(22, 22+5)
    changement_preconf(22, 23+5)
    changement_preconf(23, 23+5)
    changement_preconf(24, 22+5)
    changement_preconf(25, 22+5)
    changement_preconf(26, 22+5)
    changement_preconf(26, 21+5)
    changement_preconf(26, 24+5)
    changement_preconf(26, 25+5)
    changement_preconf(25, 24+5)
    changement_preconf(24, 25+5)
    changement_preconf(23, 25+5)
    changement_preconf(22, 25+5)
    changement_preconf(22, 26+5)
    changement_preconf(21, 27+5)
    changement_preconf(20, 27+5)
    changement_preconf(20, 26+5)
    changement_preconf(15, 26+5)
    changement_preconf(16, 26+5)
    changement_preconf(17, 26+5)
    changement_preconf(18, 26+5)
    changement_preconf(19, 26+5)
    changement_preconf(15, 28+5)
    changement_preconf(16, 28+5)
    changement_preconf(17, 28+5)
    changement_preconf(17, 29+5)
    changement_preconf(16, 30+5)
    changement_preconf(15, 30+5)
    changement_preconf(14, 29+5)

def surprise():
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

def changement_preconf(x, y):
    """
    Fonction 'changement_preconf' qui rend une cellule vivante pour les préconfigurations
    : type x : int
    : type y : int
    """
    if pedoncule[x][y].actuel:
        pass
    else:
        dessin.itemconfig(fichtre[x][y], fill="black")
        pedoncule[x][y].finger_of_god()

#XXXXXXXXXXXXXXXXXXXXXXXXX#
#----Lancement-du-Code----#
#XXXXXXXXXXXXXXXXXXXXXXXXX#

def fermeture():
    """
    Fonction 'fermeture' qui envoi un petit message de confirmation avant de fermer la fenètre
    """
    if messagebox.askokcancel("Quitter", "Voulez-vous quitter?"):
        window.destroy()

window.protocol("WM_DELETE_WINDOW", fermeture)

gr = Grille()
gr.pipistrelle()
window.mainloop()