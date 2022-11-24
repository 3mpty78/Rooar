import pygame
from player import Player


#Créer classe du jeu
class Game:

    def __init__(self):
        self.player = Player()
        self.pressed = {}
