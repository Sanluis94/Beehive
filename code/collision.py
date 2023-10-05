import pygame
from bullet import *
from enemies import *

class Collision:
    def __init__(self,screen):
        self.screen = screen
        self.bullet = Bullet(self.screen)
        self.enemy = EnemyA(self.screen)

    def collide(self):
        pass