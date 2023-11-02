import pygame
import math
from config import *
from turret_data import *

class Turret(pygame.sprite.Sprite):
    def __init__(self,screen,sprite_sheet,tile_x,tile_y):
        pygame.sprite.Sprite.__init__(self)

        self.screen = screen

        self.upgrade_level = 1
        self.range = turret_data[self.upgrade_level-1].get("range")
        self.cooldown = turret_data[self.upgrade_level-1].get("cooldown")
        self.last_shot = pygame.time.get_ticks()
        self.selected = False
        self.target = None

        self.tile_x = tile_x
        self.tile_y = tile_y

        self.x = (self.tile_x + 0.5) * tile_size
        self.y = (self.tile_y + 0.5) * tile_size

        self.sprite_sheet = sprite_sheet
        self.animation_list = self.load_images()
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

        self.angle = 90
        self.original_image = self.animation_list[self.frame_index]
        self.image = pygame.transform.rotate(self.original_image,self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)

        self.range_image = pygame.Surface((self.range * 2,self.range * 2))
        self.range_image.fill((0,0,0))
        self.range_image.set_colorkey((0,0,0))
        pygame.draw.circle(self.range_image,"grey100",(self.range,self.range),self.range)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center

    def load_images(self):
        self.size = self.sprite_sheet.get_height()
        self.animation_list = []
        for x in range(animation_steps):
            self.temp_img = self.sprite_sheet.subsurface(x * self.size,0 ,self.size, self.size)
            self.animation_list.append(self.temp_img)
        return self.animation_list

    def play_animation(self):
        self.original_image = self.animation_list[self.frame_index]

        if pygame.time.get_ticks()- self.update_time > animation_delay:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.animation_list):
                self.frame_index = 0
                self.last_shot = pygame.time.get_ticks()
                self.target = None

    def draw(self):
        self.image = pygame.transform.rotate(self.original_image,self.angle-90)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)
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
                self.angle = math.degrees(math.atan2(-self.y_dist, self.x_dist))

    def update(self,enemy_group):
       
        if self.target:
            self.play_animation()

        else:
            if pygame.time.get_ticks() - self.last_shot > self.cooldown: 
                self.pick_target(enemy_group)
