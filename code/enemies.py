import pygame
from pygame.math import Vector2
import math
from enemy_data import Enemy_data
from config import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self,screen,enemy_type,waypoints,images):
        pygame.sprite.Sprite.__init__(self)

        self.screen = screen
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.health = Enemy_data.get(enemy_type)["health"]
        self.speed = Enemy_data.get(enemy_type)["speed"]
        self.angle = 0
        self.original_image = images.get(enemy_type)
        self.image = pygame.transform.rotate(self.original_image,self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def move(self,world):
        if self.target_waypoint < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.pos
        else:
            self.kill()
            world.health -= 1
            world.missed_enemies += 1

        dist = self.movement.length()

        if dist >= (self.speed *world.game_speed):
            self.pos += self.movement.normalize() * (self.speed *world.game_speed) 
        else:
            if dist != 0:
                self.pos += self.movement.normalize() * dist
            self.target_waypoint += 1
        
        self.rect.center = self.pos

    def rotate(self):

        dist = self.target - self.pos

        self.angle = math.degrees(math.atan2(-dist[1],dist[0]))

        self.image = pygame.transform.rotate(self.original_image,self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def check_alive(self,world):
        if self.health <= 0:
            world.killed_enemies += 1
            world.money += kill_reward
            self.kill()
        

    def draw(self):
        self.screen.blit(self.image,self.rect.center)

    def update(self,world):
        self.draw()
        self.move(world)
        self.rotate()
        self.check_alive(world)