import sys
import pygame
from level import Level
from setting import *
from menu import Menu
from level_select import LevelSelect

class Game:
    def __init__(self):
        
        self.menu = Menu(screen, self.create_level, self.create_lselect, 0)
        self.status = 'menu'
    
    def create_level(self, level):
        self.level = Level(screen, self.create_menu, level)
        self.status = 'level'

    def create_menu(self, max_level):
        print("teste")
        #ToDo

    def create_lselect(self, max_level):
        print('funciona2')
        #ToDo fazer classe level select

    def run(self):
        if self.status == 'menu':
            self.menu.run(can_click)
        else:
            self.level.run()

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
game = Game()
can_click = False

#print(screen_height)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            can_click = True
        if event.type == pygame.MOUSEBUTTONUP:
            can_click = False
    screen.fill('black')
    game.run()

    pygame.display.update()
    clock.tick(60)