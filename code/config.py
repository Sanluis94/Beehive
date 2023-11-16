import pygame

clock = pygame.time.Clock()

side_panel = 300
vertical_tile_number = 22
horizontal_tile_number = 30
tile_size = 32

health = 100
money = 650
total_levels = 3

screen_height = vertical_tile_number * tile_size
screen_width = horizontal_tile_number * tile_size

spawn_cooldown = 400

turret_levels = 4
buy_cost = 100
upgrade_cost = 100
kill_reward = 1
level_complete_reward = 100
animation_steps = 1
animation_delay = 15
Damage = 5