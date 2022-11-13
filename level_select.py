import pygame
from button import Button
from setting import level_maps


class LevelSelect():
    def __init__(self, surface, create_level, create_menu, max_level):

        self.display_surface = surface

        self.buttons = pygame.sprite.Group()

        self.max_level = max_level

        self.create_level_buttons(max_level, create_level)

        self.create_menu = create_menu




    def create_level_buttons(self, level_achieved, create_level):
        for i in range(level_achieved+1):
            string = str(i+1)
            self.buttons.add(Button('assets/level'+string+'Button_fade.png','assets/level'+string+'Button_full.png',(0 + i*(300),0), create_level, i))



    def run(self):
        self.buttons.draw(self.display_surface)
        self.buttons.update()
