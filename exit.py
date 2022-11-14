import pygame

class Exit(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('assets/gateTeste.png').convert_alpha()
        self.rect = self.image.get_rect(bottomleft=pos)
    
    def update(self, x_shift):
        self.rect.x += x_shift