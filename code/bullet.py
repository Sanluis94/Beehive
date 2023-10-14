import pygame
from enemies import *

class Bullet():
    
    def __init__(self,screen,x,y):
        self.screen = screen
        self.bullet = pygame.Surface((10,5))
        self.x = x
        self.y = y
        self.rect = self.bullet.get_rect(topleft = (self.x,self.y))
        self.enemyA = EnemyA(self.screen)
    
    def update(self):
        self.screen.blit(self.bullet,(self.rect.x,self.rect.y))
        self.rect.x += 5