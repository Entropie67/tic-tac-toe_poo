# On importe les librairies nécessaires
import pygame as pg
import sys
import time
from pygame.locals import *
 

XO = 'x' # 'x' commence le jeu
 
winner = None # gagnant

draw = None # Match nul

width = 400 #largeur de la fenêtre
height = 400 # Hauteur de la fenêtre
 
# Couleur de fond
white = (255, 255, 255)
 
# Couleur des lignes
line_color = (0, 0, 0)
 
# On prépare la grille de jeu
board = [[None]*3, [None]*3, [None]*3]



