import sys
import pygame
from level import Level
from setting import *
from menu import Menu

class Game:
    def __init__(self):
        
        self.menu = Menu(screen, self.create_level, self.create_lselect)
        self.status = 'menu'
    
    def create_level(self):
        self.level = Level(level_data=level_map, surface=screen)
        self.status = 'level'

    def create_lselect(self):
        print('funciona2')
        #ToDo fazer classe level select

    def run(self):
        if self.status == 'menu':
            self.menu.run(not(can_click))
        else:
            self.level.run()

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
game = Game()
can_click = True

#print(screen_height)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if (event.type == pygame.MOUSEBUTTONDOWN):
            can_click = False
        if event.type == pygame.MOUSEBUTTONUP:
            can_click = True
    screen.fill('black')
    game.run()

    pygame.display.update()
    clock.tick(60)