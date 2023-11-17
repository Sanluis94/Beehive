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
        self.last_enemy_spawn = pygame.time.get_ticks()
        self.level_started = False
        self.game_over = False
        self.game_outcome = 0 #-1 = lost & 1 = win

        with open('./assets/mapa_1.tmj') as file:
            self.world_data = json.load(file)

        self.background = Map(self.world_data,self.screen)
        self.background.process_data()
        self.background.process_enemies()

        self.enemy_images = {

            "small":pygame.image.load("./assets/enemies/enemy_small.png"),
            "medium":pygame.image.load("./assets/enemies/enemy_medium.png"),
            "large":pygame.image.load("./assets/enemies/enemy_large.png")
                       
        }

        self.enemy_group = pygame.sprite.Group()
        self.turret_group = pygame.sprite.Group()

        self.pillbox_button = Button(self.screen,screen_width + 30, 140 , pygame.image.load("./assets/towers/defence_pillbox.png"),True)
        self.artillery_button = Button(self.screen,screen_width + 30, 180 , pygame.image.load("./assets/towers/defence_artillery.png"),True)
        self.mines_button = Button(self.screen,screen_width + 30, 240 , pygame.image.load("./assets/towers/defence_mines.png"),True)
        self.cancel_button = Button(self.screen,screen_width + 30, 180 , pygame.image.load("./assets/levels/cancel_button.png"),True)
        self.upgrade_button = Button(self.screen,screen_width + 100, 180 , pygame.image.load("./assets/levels/upgrade_button.png"),True)
        self.begin_button = Button(self.screen,screen_width + 100, 250 , pygame.image.load("./assets/levels/begin_button.png"),True)
        self.restart_button = Button(self.screen,310, 300 , pygame.image.load("./assets/levels/restart_button.png"),True)
        self.fast_forward_button = Button(self.screen,screen_width + 100, 250 , pygame.image.load("./assets/levels/fast_forward_button.png"),False)
        self.return_button = Button(self.screen,screen_width + 200, 0 , pygame.image.load("./assets/levels/fast_forward_button.png"),False)
        self.heart = pygame.image.load("./assets/levels/heart.png")
        self.coin = pygame.image.load("./assets/levels/coin.png")

        self.text_font = pygame.font.SysFont("Consolas",24,bold=True)
        self.large_font = pygame.font.SysFont("Consolas",36)
        
    def draw_text(self,text,font,text_col,x,y):
        img = font.render(text,True,text_col)
        self.screen.blit(img,(x,y))

    def display_data(self):

        pygame.draw.rect(self.screen,"maroon", (screen_width,0,side_panel,screen_height))
        pygame.draw.rect(self.screen,"grey0", (screen_width,0,side_panel,400),2)
        self.draw_text("Beehive",self.large_font,"yellow",screen_width,400)
        self.draw_text("LEVEL: " + str(self.background.level),self.text_font,"grey100",screen_width + 10,100)
        self.screen.blit(self.heart,(screen_width+10,35))
        self.draw_text(str(self.background.health),self.text_font,"grey100",screen_width + 50,40)
        self.screen.blit(self.coin,(screen_width+ 10, 65))
        self.draw_text(str(self.background.money),self.text_font,"grey100",screen_width + 50,70) 
    
    def create_tower(self,mouse_pos):
        self.mouse_tile_x = mouse_pos[0] // tile_size
        self.mouse_tile_y = mouse_pos[1] // tile_size
        self.mouse_tile_num = (self.mouse_tile_y * horizontal_tile_number) + self.mouse_tile_x

        if self.background.tile_map[self.mouse_tile_num] == 7:
            self.free_space = True
            for turret in self.turret_group:
                if (self.mouse_tile_x,self.mouse_tile_y) == (turret.tile_x, turret.tile_y):
                    self.free_space = False
            if self.free_space:
                self.turret = Turret(self.screen,pygame.image.load("./assets/towers/defence_pillbox.png"),self.mouse_tile_x,self.mouse_tile_y)
                self.turret_group.add(self.turret)
                self.background.money -= buy_cost
        
    def select_turret(self,mouse_pos):
        self.mouse_tile_x = mouse_pos[0] // tile_size
        self.mouse_tile_y = mouse_pos[1] // tile_size
        for turret in self.turret_group:
            if (self.mouse_tile_x,self.mouse_tile_y) == (turret.tile_x, turret.tile_y):
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
                            if self.background.money >= buy_cost:
                                self.create_tower(self.mouse_pos)
                        else:
                            self.selected_turret = self.select_turret(self.mouse_pos)

            self.background.draw()

            if self.game_over == False:
                if self.background.health <= 0:
                    self.game_over = True
                    self.game_outcome = -1
                if self.background.level > total_levels:
                    self.game_over = True
                    self.game_outcome = 1

                self.enemy_group.update(self.background)
                self.turret_group.update(self.enemy_group, self.background)
            for turret in self.turret_group:
                turret.draw()

            self.display_data()

            if self.game_over == False:
                if self.level_started == False:
                    if self.begin_button.draw():
                        self.level_started = True
                else:
                    self.background.game_speed = 1
                    if self.fast_forward_button.draw():
                        self.background.game_speed = 2
                    if pygame.time.get_ticks() - self.last_enemy_spawn > spawn_cooldown:
                        if self.background.spawned_enemies < len(self.background.enemy_list):
                            self.enemy_type = self.background.enemy_list[self.background.spawned_enemies]
                            self.enemy = Enemy(self.screen,self.enemy_type,self.background.waypoints,self.enemy_images)
                            self.enemy_group.add(self.enemy)
                            self.background.spawned_enemies += 1
                            self.last_enemy_spawn = pygame.time.get_ticks()

                if self.background.check_level_complete():
                    self.background.money += level_complete_reward
                    self.background.level += 1
                    self.level_started = False
                    self.last_enemy_spawn = pygame.time.get_ticks()
                    self.background.reset_level()
                    self.background.process_enemies()

                if self.selected_turret:
                    self.selected_turret.selected = True

                self.screen.blit(self.coin,(screen_width+ 260, 130))
                self.draw_text(str(buy_cost),self.text_font,"grey100",screen_width + 215,135)
                if self.pillbox_button.draw() or self.artillery_button.draw() or self.mines_button.draw():
                    self.placing_turrets = True
                if self.return_button.draw():
                    pass

                if self.placing_turrets:
                    self.cursor_rect = pygame.image.load("./assets/towers/defence_pillbox.png").get_rect()
                    self.cursor_pos = pygame.mouse.get_pos()
                    self.cursor_rect.center = self.cursor_pos
                    if self.cursor_pos[0] <= screen_width:
                        self.screen.blit(pygame.image.load("./assets/towers/defence_pillbox.png"), self.cursor_rect)
                    if self.cancel_button.draw():
                        self.placing_turrets = False
                if self.selected_turret:
                    if self.selected_turret.upgrade_level < turret_levels:
                        self.screen.blit(self.coin,(screen_width+ 260, 190))
                        self.draw_text(str(upgrade_cost),self.text_font,"grey100",screen_width + 215,195)
                        if self.upgrade_button.draw():
                            if self.background.money >= upgrade_cost:
                                self.selected_turret.upgrade()
            else:
                pygame.draw.rect(self.screen, "dodgerblue",(200,200,400,200),border_radius = 30)
                if self.game_outcome == -1:
                    self.draw_text("GAME OVER", self.large_font,"grey0",310,230)
                elif self.game_outcome == 1:
                    self.draw_text("YOU WIN!", self.large_font,"grey0",315,230)
                if self.restart_button.draw():
                    self.game_over = False
                    self.level_started = False
                    self.placing_turrets = False
                    self.selected_turrets = False
                    self.selected_turret = None
                    self.last_enemy_spawn = pygame.time.get_ticks()
                    self.background = Map(self.world_data,self.screen)
                    self.background.process_data()
                    self.background.process_enemies()
                    self.enemy_group.empty()
                    self.turret_group.empty()


            pygame.display.flip()

            clock.tick(60) 

        pygame.quit()
        
    def level_2(self):
        while self.running:
  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.background.draw()
            
            pygame.display.flip()

            clock.tick(60) 

        pygame.quit()