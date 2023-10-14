import pygame

class EnemyA():
    def __init__(self, screen):

        self.screen = screen
        self.image = pygame.image.load("./images/enemies/enemy_small.png")
        self.x = 1000
        self.y = 300
        self.rect = self.image.get_rect(topleft = (self.x,self.y))

    def update(self):
        self.screen.blit(self.image,(self.x,self.y))

class EnemyB():
    def __init__(self, screen):

        self.screen = screen
        self.image = pygame.image.load("./images/enemies/enemy_medium.png")
        self.x = 1100
        self.y = 300
        self.rect = self.image.get_rect(topleft = (self.x,self.y))

    def update(self):
        self.screen.blit(self.image,(self.x,self.y))

class EnemyC():
    def __init__(self, screen):

        self.screen = screen
        self.image = pygame.image.load("./images/enemies/enemy_large.png")
        self.x = 900
        self.y = 300
        self.rect = self.image.get_rect(topleft = (self.x,self.y))

    def update(self):
        self.screen.blit(self.image,(self.x,self.y))