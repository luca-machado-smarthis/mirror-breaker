import pygame
from button import Button
from setting import level_maps


class LevelSelect():
    def __init__(self, surface, create_level, create_menu, max_level):

        self.display_surface = surface

        self.buttons = pygame.sprite.Group()

        self.max_level = max_level







    def create_buttons(level_achieved, create_level):
        for i in range(level_achieved+1):
            string = str(i+1)
            



    def run(self, click):
        self.buttons.draw(self.display_surface)
        self.buttons.update(click)
