import pygame


#Création de la classe monster
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load("assets/monster2.png")
        self.image = pygame.transform.scale(self.image, (200, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 550
        self.velocity = 1

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity