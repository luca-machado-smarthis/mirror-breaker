import pygame
from button import Button

class Menu:
    def __init__(self, surface, create_level, create_lselect):

        self.display_surface = surface

        self.buttons = pygame.sprite.Group()

        #depois tem que posicionar onde quiser 
        self.buttons.add(Button('assets/playButton_fade.png', 'assets/playButton_full.png', (0,0), create_level))#Jogar
        self.buttons.add(Button('assets/levelButton_fade.png', 'assets/levelButton_full.png', (300,0), create_lselect))#Level Select
        #self.buttons.add(Button('arquivo_fade.py','arquivo_full.py',(0,0)))#Sair
        


    

    def run(self,click):
        self.buttons.draw(self.display_surface)
        self.buttons.update(click)
