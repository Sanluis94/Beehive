import pygame
import sys
sys.path.append("code")
from config import *
from menu import Menu

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
running = True
menu = Menu(screen,screen_width,screen_height)

while running:
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    menu.menu_inicial()

    pygame.display.flip()

    clock.tick(60) 

pygame.quit()