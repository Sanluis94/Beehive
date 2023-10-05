import pygame
from enemies import *

class Round:
    def __init__(self,screen):
        
        self.enemy = EnemyA(screen)

    def update(self):
        
        self.enemy.update()
        self.enemy.x -= 3