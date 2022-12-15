import sys
import pygame
from button import Button

class Menu:
    def __init__(self, surface, create_level, create_lselect, max_level):

        self.display_surface = surface
        self.background = pygame.image.load('assets/menusBackground.png').convert_alpha()

        self.buttons = pygame.sprite.Group()


        #depois tem que posicionar onde quiser
        if max_level > 0:
            self.buttons.add(Button('assets/levelButton_fade.png', 'assets/levelButton_full.png', (510,480), create_lselect))#Level Select
            self.buttons.add(Button('assets/continueButton_fade.png','assets/continueButton_full.png',(70,480), create_level, max_level)) # Continue no level mais avançado
        else:
            self.buttons.add(Button('assets/playButton_fade.png', 'assets/playButton_full.png', (70,480), create_level, 0))#Jogar
        
        self.buttons.add(Button('assets/exitButton_fade.png','assets/exitButton_full.png',(950,480), self.quit))


    def quit(self):
        pygame.quit()
        sys.exit()


    def run(self):
        self.display_surface.blit(self.background,(-42,0))
        self.buttons.draw(self.display_surface)
        self.buttons.update()
