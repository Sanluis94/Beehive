import pygame

class Pillbox:
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load("./images/towers/defence_pillbox.png")
        self.x = 200
        self.y = 300

    def x(self):
        self.x = self.x

    def y(self):
        self.y = self.y
    
    def update(self):
        self.screen.blit(self.image,(self.x,self.y))