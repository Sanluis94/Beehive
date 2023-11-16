import pygame
from config import *
import random
from enemy_data import Enemy_spawn_data

class Map:
    def __init__(self,data,screen):

        self.screen = screen
        self.level = 1
        self.game_speed = 1
        self.health = health
        self.money = money
        self.level_data = data
        self.tile_map = []
        self.waypoints = []
        self.enemy_list = []
        self.spawned_enemies = 0
        self.killed_enemies = 0
        self.missed_enemies = 0
        self.background = pygame.image.load("./assets/levels/block_background.png")
        self.background = pygame.transform.scale(self.background,(screen_width,screen_height))

    def process_data(self):
        for layer in self.level_data["layers"]:
            if layer["name"] == "blocos":
                self.tile_map = layer["data"]
            elif layer["name"] == "waypoints":
                for obj in layer["objects"]:
                    waypoint_data = obj["polyline"]
                    self.process_waypoints(waypoint_data)

    def process_waypoints(self,data):
        for point in data:
            temp_x = point.get("x")
            temp_y = point.get("y")
            self.waypoints.append((temp_x,temp_y))

    def process_enemies(self):
        self.enemies = Enemy_spawn_data[self.level - 1]
        for enemy_type in self.enemies:
            self.enemies_to_spawn = self.enemies[enemy_type]
            for enemy in range(self.enemies_to_spawn):
                self.enemy_list.append(enemy_type)

        random.shuffle(self.enemy_list)

    def check_level_complete(self):
        if(self.killed_enemies + self.missed_enemies) == len(self.enemy_list):
            return True

    def reset_level(self):
        self.enemy_list = []
        self.spawned_enemies = 0
        self.killed_enemies = 0
        self.missed_enemies = 0

    def draw(self):
        self.screen.blit(self.background, (0,0))
        
    