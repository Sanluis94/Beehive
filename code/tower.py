import pygame
import math
from config import *

class Turret(pygame.sprite.Sprite):
    def __init__(self,screen,image,tile_x,tile_y):
        pygame.sprite.Sprite.__init__(self)

        self.screen = screen

        self.range = 90
        self.cooldown = 1500
        self.last_shot = pygame.time.get_ticks()
        self.selected = False
        self.target = None

        self.tile_x = tile_x
        self.tile_y = tile_y

        self.x = (self.tile_x + 0.5) * tile_size
        self.y = (self.tile_y + 0.5) * tile_size
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)

        self.range_image = pygame.Surface((self.range * 2,self.range * 2))
        self.range_image.fill((0,0,0))
        self.range_image.set_colorkey((0,0,0))
        pygame.draw.circle(self.range_image,"grey100",(self.range,self.range),self.range)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center

    def draw(self):
        self.screen.blit(self.image,self.rect)
        if self.selected:
            self.screen.blit(self.range_image,self.range_rect)

    def pick_target(self,enemy_group):
        self.x_dist = 0
        self.y_dist = 0

        for enemy in enemy_group:
            self.x_dist = enemy.pos[0] - self.x
            self.y_dist = enemy.pos[1] -self.y
            self.dist = math.sqrt(self.x_dist ** 2 + self.y_dist ** 2)
            if self.dist < self.range:
                self.target = enemy
                print("target selected")

    def update(self,enemy_group):

        if self.target:
            pass
        else:
            if pygame.time.get_ticks() - self.last_shot > self.cooldown:
                self.pick_target(enemy_group)
