import pygame
from utils import import_folder
from math import floor

class FireBreather(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.image = pygame.image.load('assets/hazards/fire-breather.png')
        self.rect = self.image.get_rect(bottomleft=pos)
    
    def update(self, x_shift):
        self.rect.x += x_shift

class FireWall(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.frame_index = 0
        self.animation_speed = 0.10
        self.animations = import_folder('assets/hazards/firewall')
        self.image = pygame.transform.rotate(pygame.image.load('assets/hazards/firewall/firewall1.png'), -90).convert_alpha()
        self.rect = self.image.get_rect(bottomleft=pos)
    
    def animate(self):

        self.frame_index += self.animation_speed

        if self.frame_index >= len(self.animations):
            self.frame_index = 0
        self.image = pygame.transform.rotate(self.animations[floor(self.frame_index)], -90)


    def update(self, x_shift):
        self.rect.x += x_shift
        self.animate()