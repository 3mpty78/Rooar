import pygame


#Définition classe du projectile
class Projectile(pygame.sprite.Sprite):

    #Définition du constructeur  de la classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 1
        self.player = player
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 125
        self.rect.y = player.rect.y + 90
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        #Faire tourner le projectile
        self.angle += 5
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle,
                                               1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        #Condition pour supprimer le projecctile hors de l'ecran
        if self.rect.x > 1080:
            self.remove()
