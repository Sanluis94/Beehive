import pygame
import json
from config import * 
from tower import *
from enemies import *
from map import *
from button import *

class Level:
    def __init__(self,screen):
        self.screen = screen
        self.running = True
        self.placing_turrets = False
        self.selected_turret = None

        with open('./assets/mapa_1.tmj') as file:
            self.world_data = json.load(file)

        self.background = Map(self.world_data,self.screen)
        self.background.process_data()

        self.enemy = Enemy(self.screen,self.background.waypoints,pygame.image.load("./assets/enemies/enemy_small.png"))

        self.enemy_group = pygame.sprite.Group()
        self.turret_group = pygame.sprite.Group()

        self.enemy_group.add(self.enemy)

        self.pillbox_button = Button(self.screen,screen_width + 30, 120 , pygame.image.load("./assets/towers/defence_pillbox.png"),True)
        self.artillery_button = Button(self.screen,screen_width + 100, 120 , pygame.image.load("./assets/towers/defence_artillery.png"),True)
        self.mines_button = Button(self.screen,screen_width + 170, 120 , pygame.image.load("./assets/towers/defence_mines.png"),True)
        self.cancel_button = Button(self.screen,screen_width + 30, 180 , pygame.image.load("./assets/towers/defence_artillery.png"),True)

    def create_tower(self,mouse_pos):
        self.mouse_tile_x = mouse_pos[0] // tile_size
        self.mouse_tile_y = mouse_pos[1] // tile_size
        self.mouse_tile_num = (self.mouse_tile_y * vertical_tile_number) + self.mouse_tile_x

        if self.background.tile_map[self.mouse_tile_num ] == 7:
            self.free_space = True
            for turret in self.turret_group:
                if (self.mouse_tile_x,self.mouse_tile_y) == (self.turret.tile_x, self.turret.tile_y):
                    self.free_space = False
            if self.free_space:
                self.turret = Turret(self.screen,pygame.image.load("./assets/towers/defence_pillbox.png"),self.mouse_tile_x,self.mouse_tile_y)
                self.turret_group.add(self.turret)
        
    def select_turret(self,mouse_pos):
        self.mouse_tile_x = mouse_pos[0] // tile_size
        self.mouse_tile_y = mouse_pos[1] // tile_size
        for turret in self.turret_group:
            if (self.mouse_tile_x,self.mouse_tile_y) == (self.turret.tile_x, self.turret.tile_y):
                return turret

    def clear_selection(self):
        for turret in self.turret_group:
            turret.selected = False
    
    def level_1(self):
        while self.running:
  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mouse_pos = pygame.mouse.get_pos()
                    if self.mouse_pos[0]< screen_width and self.mouse_pos[1]<screen_height:
                        self.selected_turret = None
                        self.clear_selection()
                        if self.placing_turrets:
                            self.create_tower(self.mouse_pos)
                        else:
                            self.selected_turret = self.select_turret(self.mouse_pos)

            self.screen.fill("grey50")

            self.background.update()
            self.enemy_group.update()
            #self.turret_group.update(self.enemy_group)
            for turret in self.turret_group:
                turret.draw()

            if self.selected_turret:
                self.selected_turret.selected = True

            if self.pillbox_button.draw() or self.artillery_button.draw() or self.mines_button.draw():
                self.placing_turrets = True

            if self.placing_turrets:
                self.cursor_rect = pygame.image.load("./assets/towers/defence_pillbox.png").get_rect()
                self.cursor_pos = pygame.mouse.get_pos()
                self.cursor_rect.center = self.cursor_pos
                if self.cursor_pos[0] <= screen_width:
                    self.screen.blit(pygame.image.load("./assets/towers/defence_pillbox.png"), self.cursor_rect)
                if self.cancel_button.draw():
                    self.placing_turrets = False

            pygame.display.flip()

            clock.tick(60) 

        pygame.quit()
        
    def level_2(self):
        while self.running:
  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.background.update()
            
            pygame.display.flip()

            clock.tick(60) 

        pygame.quit()