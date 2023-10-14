import pygame
from enemies import *

class Dijkstra:
    def __init__(self,screen):
        
        self.enemyA = EnemyA(screen)
        self.enemyB = EnemyB(screen)
        self.enemyC = EnemyC(screen)

    def update(self):
        
        self.enemyA.update()
        self.enemyA.x -= 3
        self.enemyB.update()
        self.enemyB.x -= 3
        self.enemyC.update()
        self.enemyC.x -= 3