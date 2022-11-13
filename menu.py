import pygame
from button import Button

class Menu:
    def __init__(self, surface, create_level, create_lselect, max_level):

        self.display_surface = surface

        self.buttons = pygame.sprite.Group()

        self.max_level = max_level

        #depois tem que posicionar onde quiser
        if self.max_level > 0:
            self.buttons.add(Button('assets/levelButton_fade.png', 'assets/levelButton_full.png', (300,0), create_lselect, max_level))#Level Select
            self.buttons.add(Button('assets/continueButton_fade.png','assets/continueButton_full.png',(0,0), create_level, max_level)) # Continue no level mais avançado
        else:
            self.buttons.add(Button('assets/playButton_fade.png', 'assets/playButton_full.png', (0,0), create_level, 0))#Jogar
        
        #self.buttons.add(Button('assets/exitButton_fade.py','assets/exitButton_full.py',(0,0), function, parametro))#Sair
        


    

    def run(self):
        self.buttons.draw(self.display_surface)
        self.buttons.update()
