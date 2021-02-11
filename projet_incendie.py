#############################################
# groupe MIASHS 1
# Alae KARTOUT
# Basma BAGNAH AMADOU
# Beatriz ANTON ARTAZA
# https://github.com/bea-anton/projet_incendie.git
##############################################

##############################################
# import des librairies

import tkinter as tkinter

#############################################
# constantes

COULEUR_FOND = "gray"
LARGEUR = 1000
HAUTEUR = 1000

##############################################
# fonctions


##############################################
# programme principal

racine = tk.Tk()
racine.title("Projet incendie")
# creation des widgets
canvas = tk.Canvas(racine, bg=COULEUR_FOND, width=LARGEUR, height=HAUTEUR)
# PLACEMENT DES WIDGETS
canvas.grid(row=0)
# boucle principal
racine.mainloop()
coucocu hp
