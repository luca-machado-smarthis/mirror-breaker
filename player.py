import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill('gold')
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2(0, 0) # só para não ter qur criar 2 variáveis
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = - 16
        self.can_jump = True

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_s]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        if keys[pygame.K_SPACE] and self.can_jump:
            self.jump()
            self.can_jump = False
        # if not keys[pygame.K_SPACE]:
        #     self.can_jump = True

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def reset_vertical_momentum(self):
        self.direction.y = 0

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()