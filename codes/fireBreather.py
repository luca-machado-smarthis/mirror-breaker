import pygame
from utils import import_folder
from math import floor

class FireBreather(pygame.sprite.Sprite):
    def __init__(self, pos, orientation='r'):
        super().__init__()
        self.pos = pos
        self.orientation = orientation
        self.image = pygame.image.load('assets/hazards/fire-breather.png') if (self.orientation == 'r') else pygame.transform.flip(pygame.image.load('assets/hazards/fire-breather.png'), True, False)
        self.rect = self.image.get_rect(bottomleft=pos)
    
    def update(self, x_shift):
        self.rect.x += x_shift

class FireWall(pygame.sprite.Sprite):
    def __init__(self, pos, orientation='r'):
        super().__init__()
        self.frame_index = 0
        self.animation_speed = 0.10
        self.animations = import_folder('assets/hazards/firewall')
        self.image = pygame.transform.rotate(pygame.image.load('assets/hazards/firewall/firewall1.png'), -90).convert_alpha()
        self.orientation = orientation
        self.rect = self.image.get_rect(bottomleft=(pos[0]+50, pos[1]) if orientation=='r' else (pos[0]-100, pos[1]))
        self.cooldown = 10
        self.duration = 5
        self.timer = 0
        self.active = True
    
    def animate(self):

        self.frame_index += self.animation_speed

        if self.frame_index >= len(self.animations):
            self.frame_index = 0
        self.image = pygame.transform.rotate(self.animations[floor(self.frame_index)], -90) if (self.orientation == 'r') else pygame.transform.rotate(self.animations[floor(self.frame_index)], 90)

    def update(self, x_shift):
        self.rect.x += x_shift
        self.animate()
        if self.active: #potencial de melhora ao trocar ver depois
            self.timer += self.animation_speed
            if self.timer > self.duration:
                self.active = False
                self.timer = 0
        else:
            self.timer += self.animation_speed
            if self.timer > self.cooldown:
                self.active = True
                self.timer = 0
