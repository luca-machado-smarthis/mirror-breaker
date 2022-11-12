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
        self.level = Level(screen, self.create_menu, self.create_level, level)
        self.status = 'level'

    def create_menu(self, max_level):
        print("teste")
        #ToDo so serve pra caso queira voltar do level ou level_select ao menu

    def create_lselect(self, max_level):
        self.lselect = LevelSelect(screen, self.create_level, self.create_menu, max_level)
        self.status = 'level_select'

    def run(self):
        if self.status == 'menu':
            self.menu.run()
        elif self.status == 'level_select':
            self.lselect.run()
        else:
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