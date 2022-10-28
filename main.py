import sys
import pygame
from level import Level
from setting import *

class Game:
    def __init__(self):
        self.level = Level(level_data=level_map, surface=screen)
    
    def run(self):
        self.level.run()

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
game = Game()

#print(screen_height)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('black')
    game.run()

    pygame.display.update()
    clock.tick(60)