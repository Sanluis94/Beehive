import pygame
from tower import *

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self,screen):
        self.screen = screen
        self.bullet = pygame.Surface((10,5))
        self.pillbox = Pillbox(self.screen)
        self.x = self.pillbox.x + 30
        self.y = self.pillbox.y + 15
        self.rect = self.bullet.get_rect(topleft = (self.x,self.y))
    
    def update(self):
        
        self.screen.blit(self.bullet,(self.rect.x,self.rect.y))
        self.rect.x += 3