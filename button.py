import pygame

class button(pygame.sprite.Sprite):
    def __init__(self, image_fade, image_full, position):
        super().__init__()
        
        self.image_full = pygame.image.load(image_full).convert_alpha()
        self.image_fade = pygame.image.load(image_fade).convert_alpha()
        self.image = image_fade

        self.rect = self.image.get_rect(center = position)
        

    def update(self):
        pass 
