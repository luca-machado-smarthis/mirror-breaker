import sys
import pygame
from level import Level
from setting import *

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_data=level_map, surface=screen)

print(screen_height)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)