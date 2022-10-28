import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, image_fade, image_full, position, action):
        super().__init__()
        
        self.image_full = pygame.image.load(image_full).convert_alpha()
        self.image_fade = pygame.image.load(image_fade).convert_alpha()
        self.image = image_fade

        self.rect = self.image.get_rect(center = position)

        self.action = action

    def collision_mice(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False

    def update(self, click):
        if self.collision_mice():
            self.image = self.image_full
            if click:
                self.action
        else:
            self.image = self.image_fade
