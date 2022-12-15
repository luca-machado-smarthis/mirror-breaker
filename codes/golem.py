import pygame
from utils import import_folder
from math import floor
from setting import tile_size

class Golem(pygame.sprite.Sprite):
    def __init__(self, pos, direction=1, speed=1.2):
        super().__init__()
        self.animations = import_folder('assets/hazards/golem')
        self.image = pygame.image.load('assets/hazards/golem/golem1.png')
        self.rect = self.image.get_rect(bottomleft=pos) 
        self.animation_speed = 0.05
        self.speed = 1
        self.frame_index = 0
        self.direction = -1

    def animate(self):
        self.frame_index += self.animation_speed
        
        if self.frame_index > len(self.animations):
            self.frame_index = 0
        if self.direction == 1:
            self.image = pygame.transform.flip(self.animations[floor(self.frame_index)], True, False)
        else:
            self.image = self.animations[floor(self.frame_index)]

    def reverse(self):
        self.direction *= -1
    
    def update(self, x_shift):
        self.rect.x += x_shift + self.direction*self.speed
        print(x_shift + self.direction*self.speed)
        self.animate()
    

class GolemMarker(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((tile_size,tile_size))
        self.rect = self.image.get_rect(bottomleft = pos)

    def update(self,shift):
        self.rect.x += shift
    