import pygame
from config import *

class Map:
    def __init__(self,data,screen):

        self.screen = screen
        self.level_data = data
        self.tile_map = []
        self.waypoints = []
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

    def draw(self):
        self.screen.blit(self.background, (0,0))

    def update(self):
        self.draw()
    