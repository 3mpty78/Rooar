import pygame
from game import Game
from player import Player

pygame.init()

# Générer la fenêtre du jeu
pygame.display.set_caption("ROOAR")
screen = pygame.display.set_mode((1080, 720))

#Importer et charger arrière plan
background = pygame.image.load("assets/bg.jpg")

#Charger le joueur
player = Player()

#Charger le jeu
game = Game()

running = True

# Boucle tant que c'est vrai
while running:

    #appliquer le background
    screen.blit(background, (0, -200))

    #appliquer image du joueur
    screen.blit(player.image, player.rect)

    #vérifier gauche ou droite
    if game.pressed.get(
            pygame.K_d
    ) and player.rect.x + player.rect.width < screen.get_width():
        player.move_right()
    elif game.pressed.get(pygame.K_q) and player.rect.x > 0:
        player.move_left()

    #Mettre à jour l'édcran
    pygame.display.flip()

    # si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")

        #Détecter si un joueur lâche une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
