import pygame

class Exit(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('assets/gateTeste.png').convert_alpha()
        #self.image_open = pygame.image.load('assets/gateOpen_teste.png').convert_alpha()
        self.rect = self.image.get_rect(bottomleft=pos)
        self.status = False #Está fechado
    
    def open_exit(self):
        #self.image = self.image_open
        self.status = True #Está aberto
    
    def update(self, x_shift):
        self.rect.x += x_shift