import pygame

class Mirror(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image_whole = pygame.image.load('assets/mirrorTest.png').convert_alpha()
        #self.image_broken = pygame.image.load('assets/mirrorBroken_Test.png').convert_alpha()
        self.rect = self.image_whole.get_rect(topleft=pos)
        self.state = 'whole'

    def update(self, x_shift):
        if self.state == 'whole':
            self.image = self.image_whole
        #else:
            #self.image = self.image_broken

        self.rect.x += x_shift
            

