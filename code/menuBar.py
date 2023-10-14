import pygame
from tower import *

class MenuBar():
    def __init__(self,screen):
        self.screen = screen
        self.menu_bar = pygame.Rect(0,0,1200,100)
        self.menu_button1 = pygame.Rect(100,10,50,50)
        self.menu_button2 = pygame.Rect(200,10,50,50)
        self.menu_button3 = pygame.Rect(300,10,50,50)
        self.menu_button4 = pygame.Rect(400,10,50,50)

    def click_check(self):
        pass

    def update(self):
        
        pygame.draw.rect(self.screen,(0,32,255),self.menu_bar)
        pygame.draw.rect(self.screen,(255,0,0),self.menu_button1)
        pygame.draw.rect(self.screen,(255,0,0),self.menu_button2)
        pygame.draw.rect(self.screen,(255,0,0),self.menu_button3)
        pygame.draw.rect(self.screen,(255,0,0),self.menu_button4)

        self.click_check()