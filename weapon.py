import pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('assets/weapon.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(pos[0] - 20, pos[1] - 10))



    def update(self, pos, input):
        if input:
            self.rect = self.image.get_rect(topleft=(pos[0], pos[1] - 10))
        else:
            self.rect = self.image.get_rect(topleft=(pos[0] - 20, pos[1] - 10))
