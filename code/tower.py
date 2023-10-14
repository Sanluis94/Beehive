import pygame
from bullet import *

class Pillbox:
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load("./images/towers/defence_pillbox.png")
        self.x = 200
        self.y = 275
        self.bullet = Bullet(self.screen,self.x + 30,self.y + 15)

    def place_tower(self):
        self.ev = pygame.event.get()
        for event in self.ev:
            if event.type == pygame.MOUSEBUTTONUP:
                self.x = pygame.mouse.get_pos()[0]
                self.y = pygame.mouse.get_pos()[1]

    def update(self):
        self.screen.blit(self.image,(self.x,self.y))
        self.place_tower()
        self.bullet.update()
        