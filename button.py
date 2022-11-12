import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, image_fade, image_full, position, action, info):
        super().__init__()
        
        self.image_full = pygame.image.load(image_full).convert_alpha()
        self.image_fade = pygame.image.load(image_fade).convert_alpha()
        self.image = self.image_fade

        self.action = action
        self.info = info

        self.rect = self.image.get_rect(topleft = position)

        self.click = True

        

    def collision_mice(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False

    def get_click(self):
        keys = pygame.mouse.get_pressed()
        return keys[0] and self.click

    def update(self):
        if self.collision_mice():
            self.image = self.image_full
            if self.get_click():
                self.click = False #So quero que posso ser clicado uma vez mesmo, todo botao que é clicado faz movimentacao de janela
                self.action(self.info)
        else:
            self.image = self.image_fade