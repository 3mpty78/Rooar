import pygame
from game import Game
from player import Player

pygame.init()

# Générer la fenêtre du jeu
pygame.display.set_caption("ROOAR")
screen = pygame.display.set_mode((1080, 720))

#Importer et charger arrière plan
background = pygame.image.load("assets/bg.jpg")

#Charger le jeu
game = Game()
#Charger le joueur
player = Player(game)

running = True

# Boucle tant que c'est vrai
while running:
    #appliquer le background
    screen.blit(background, (0, -200))
    #appliquer image du joueur
    screen.blit(player.image, player.rect)

    #Récupération des projectiles
    for projectile in player.all_projectiles:
        projectile.move()
    #Récupération des monstres
    for monster in game.all_monsters:
        monster.forward()

    #Afficher image des projectiles
    player.all_projectiles.draw(screen)
    #Afficher images monstres
    game.all_monsters.draw(screen)

    #Vérifier gauche ou droite
    if game.pressed.get(
            pygame.K_d
    ) and player.rect.x + player.rect.width < screen.get_width():
        player.move_right()
    elif game.pressed.get(pygame.K_q) and player.rect.x > 0:
        player.move_left()

    #Mise à jour de l'ecran
    pygame.display.flip()

    #Si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
        #Détecter si le joueur presse une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            #Détection touche Espace appuyée pour projectile
            if event.key == pygame.K_SPACE:
                player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
