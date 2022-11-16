import pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self, pos, p_d):
        super().__init__()
        self.image = pygame.image.load('assets/weapon.png').convert_alpha()
        image_copy = self.image.copy()
        self.image_reverse = pygame.transform.flip(image_copy, True, False)
        self.image_normal = self.image
        self.pos_x = pos[0] + p_d[0]*2 - 30
        self.pos_y = pos[1] + p_d[1]/2 - 5
        self.p_d = p_d
        self.rect = self.image.get_rect(midright=(self.pos_x, self.pos_y))
        self.move = 20

    


    def update(self, pos, input, direction):
        self.pos_y = pos[1] + self.p_d[1]/2 - 5
        if direction > 0:
            self.image = self.image_normal
            self.pos_x = pos[0] + self.p_d[0]*2 - 30
            self.move = 20
        elif direction < 0:
            self.image = self.image_reverse
            self.pos_x = pos[0] + 10
            self.move = -20
        else:
            if self.move < 0:
                self.pos_x = pos[0] + 10
            else:
                self.pos_x = pos[0] + self.p_d[0]*2 - 30
        if input:
            self.rect.midright=(self.pos_x + self.move, self.pos_y)
        else:
            self.rect.midright=(self.pos_x, self.pos_y)
