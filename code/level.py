import pygame
from config import * 
from dijkstra import *
from tower import *
from bullet import *
from collision import *
from menuBar import *

class Level:
    def __init__(self,screen):
        self.screen = screen
        self.background = pygame.image.load("./images/levels/block_background.png")
        self.background = pygame.transform.scale(self.background,(screen_width,screen_height))
        self.running = True
        self.dijkstra = Dijkstra(self.screen)
        self.collision = Collision(self.screen)
        self.menuBar = MenuBar(self.screen)
        self.pillbox = Pillbox(self.screen)

    def level_1(self):
        while self.running:
  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.blit(self.background,(0,0))
            self.menuBar.update()
            self.pillbox.update()
            self.dijkstra.update()

            pygame.display.flip()

            clock.tick(60) 

        pygame.quit()
        
    def level_2(self):
        while self.running:
  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.blit(self.background,(0,0))
            self.menuBar.update()
            self.pillbox.update()
            self.dijkstra.update()
            
            pygame.display.flip()

            clock.tick(60) 

        pygame.quit()