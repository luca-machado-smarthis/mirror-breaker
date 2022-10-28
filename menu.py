import pygame
from button import Button

class Menu:
    def __init__(self, surface):
        self.display_surface = surface
        self.buttons = pygame.sprite.Group()
        self.buttons.add(Button('arquivo_fade.py','arquivo_full.py',(0,0), ))#Jogar
        #self.buttons.add(Button('arquivo_fade.py','arquivo_full.py',(0,0)))#Level Select
        #self.buttons.add(Button('arquivo_fade.py','arquivo_full.py',(0,0)))#Sair
        
    

    def run(self, mice):
        self.buttons.update(mice)
        self.buttons.draw(self.display_surface)
