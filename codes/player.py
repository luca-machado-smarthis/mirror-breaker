import pygame
from weapon import Weapon
from utils import import_folder
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        #self.image = self.animations['idle'][self.frame_index].convert_alpha()
        self.image = pygame.image.load('assets/character/idle/idle1.png').convert_alpha()
        self.state = 'idle'
        self.orientation = 'right'

        self.rect = self.image.get_rect(topleft=pos)
        # self.image_normal = self.image
        # self.image_reverse = pygame.transform.flip(self.image.copy(), True, False)

        self.direction = pygame.math.Vector2(0, 0) # só para não ter qur criar 2 variáveis
        self.speed = 6
        self.gravity = 0.8
        self.jump_speed = - 16
        self.can_jump = True
        self.can_wall_jump = False
        self.wall_jump_direction = 0

        self.weapon = pygame.sprite.GroupSingle()
        self.weapon.add(Weapon(pos, (self.image.get_width(),self.image.get_height())))
        self.attack = False
        self.click = True
        self.timing = 600
        self.time = 0

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
            self.orientation = 'right'
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            self.orientation = 'left'
        else:
            self.direction.x = 0
        if keys[pygame.K_SPACE]:
            if self.can_jump:
                self.jump()
                self.can_jump = False
            elif self.can_wall_jump:
                self.wall_jump()
        # if not keys[pygame.K_SPACE]:
        #     self.can_jump = True
        if not(self.attack) and keys[pygame.K_q] and self.click:
            self.attack = True
            self.click = False

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def reset_vertical_momentum(self):
        self.direction.y = 0

    def jump(self):
        self.direction.y = self.jump_speed

    def wall_jump(self):
        self.direction.x = self.wall_jump_direction
        self.direction.y = self.jump_speed * self.gravity
    
    def aggresion(self, time):
        if self.attack and self.timing <= 300 :
            self.attack = False
        if not(self.click):
            self.timing += time
            if self.timing <= 0:
                self.timing = 600
                self.click = True
    
    def animate(self):

        print(self.direction.y)
        if self.direction.y < 0:
          self.state = 'jump'
        elif self.direction.y > 0.8:
            self.state = 'fall'
        elif int(self.direction.x) != 0:
            self.state = 'walk'
        else:
            self.state = 'idle'

        animation = self.animations[self.state]

        self.frame_index += self.animation_speed

        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        if self.orientation == 'right':
            self.image = animation[math.floor(self.frame_index)]
        else:
            self.image = pygame.transform.flip(animation[math.floor(self.frame_index)],True,False)


    def import_character_assets(self):
        character_path = 'assets/character/'
        self.animations = {'idle':[], 'walk':[], 'jump':[], 'fall':[]}
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def update(self,surface):
        time_passed = self.time - pygame.time.get_ticks()
        self.get_input()
        self.animate()
        self.weapon.update((self.rect.left, self.rect.top), self.attack, self.direction.x)
        self.weapon.draw(surface)
        self.aggresion(time_passed)
        self.time = pygame.time.get_ticks()
