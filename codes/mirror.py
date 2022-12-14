import pygame

class Mirror(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()                 
        self.image= pygame.image.load('assets/mirrorGlow_Test.png').convert_alpha()
        self.image_broken = pygame.image.load('assets/mirrorBroken_test.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(pos[0], pos[1] + 10))
        self.status = True #Ta inteiro

    def change_image_broken(self):
      self.image = self.image_broken
      self.status = False #Foi quebrado

    def update(self, x_shift):
      self.rect.x += x_shift
            

