import pygame
from projectile import Projectile


#créer classe du joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = 1
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("assets/player2.png")
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 500

    def launch_projectile(self):
        #créer nouvelle instance classe projectile
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        #si le joueur n'est pas en collision
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
