import pygame

class Mirror(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image= pygame.image.load('assets/mirrorTest.png').convert_alpha()
        #self.image_broken = pygame.image.load('assets/mirrorBroken_Test.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(pos[0], pos[1] + 10))


    def update(self, x_shift):
        #if:
          #self.image = self.image_broken

        self.rect.x += x_shift
            

