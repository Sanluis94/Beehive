import pygame
from config import *

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

while running:
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    pygame.display.flip()

    clock.tick(60) 

pygame.quit()