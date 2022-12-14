import pygame

class Spike(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('assets/hazards/spike.png').convert_alpha()
        self.rect = self.image.get_rect(bottomleft=pos)#Depois achar um jeito de botar em parede/chao/solto 
    
    def update(self, x_shift):
        self.rect.x += x_shift