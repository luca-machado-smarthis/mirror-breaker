import pygame

from player import Player
from setting import *
from tiles import Tile
from mirror import Mirror
from spike import Spike
from exit import Exit
from setting import level_maps

class Level:
    def __init__(self, surface, create_menu, create_level, level_number):
        #Cores
        self.display_surface = surface
        self.background = pygame.image.load('assets/background.jpg').convert_alpha()
        self.text_font = pygame.font.Font(None, 75)
        self.create_menu = create_menu # Depois usar para retornar ao menu
        self.create_level = create_level # Depois usar quando terminar a fase para poder ir para proxima

        #Groups
        self.tiles = pygame.sprite.Group()
        self.mirrors = pygame.sprite.Group()
        self.spikes = pygame.sprite.Group()
        self.exit = pygame.sprite.GroupSingle()
        self.player = pygame.sprite.GroupSingle()  # sempre cria um grupo (mesmo que solitário) e depois instancia e  adiciona

        #Integers
        self.world_shift = 0
        self.mirror_quant = 0
        self.mirror_broken = 0
        self.level_number = level_number#Next level seria isso + 1

        #Set-up
        self.setup_level(level_maps[level_number])
        self.mirror_count_surface = self.text_font.render(f'{self.mirror_broken}/{self.mirror_quant}', False, 'Blue')#Tem que vir dps do setup pelo mirror_quant
        self.time = timer_maps[level_number]
        self.start_time = pygame.time.get_ticks()

        

    def setup_level(self, layout):
        for row_index, row in enumerate(layout):
            row_index -= 1
            for col_index, cell in enumerate(row):
                if row_index == -1:
                    for i in range(2):
                        for j in range(2):
                            tile = Tile((col_index * tile_size + i*28, row_index * tile_size + j*28 - 56))
                            self.tiles.add(tile)
                else:
                    if cell == 'x' or cell == 'X':
                        for i in range(2):
                            for j in range(2):
                                tile = Tile((col_index * tile_size + i*28, row_index * tile_size + j*28))
                                self.tiles.add(tile)
                    elif cell == 'P':
                        player_sprite = Player((col_index * tile_size, row_index * tile_size ))
                        self.player.add(player_sprite)
                    elif cell == 'M':
                        mirror = Mirror((col_index * tile_size, (row_index-1) * tile_size ))
                        self.mirrors.add(mirror)
                        self.mirror_quant += 1
                    elif cell == 's':
                        for i in range(4):
                            spike = Spike((col_index * tile_size + i*14, (row_index+1) * tile_size))
                            self.spikes.add(spike)
                    elif cell == 'E':
                        exit_sprite = Exit((col_index * tile_size, (row_index+1) * tile_size ))
                        self.exit.add(exit_sprite)
        


    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        if player_x < screen_width/5 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width*4/5 and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8



    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        for sprite in self.tiles.sprites():  #todo adicionar wallJUmp
            if sprite.rect.colliderect(player.rect):
                if player.direction.y < 0: # melhor forma de ver com o que se está colidindo
                    player.rect.top = sprite.rect.bottom
                    player.reset_vertical_momentum()
                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.can_jump = True
                    player.reset_vertical_momentum()
    


    def input_return(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.create_menu(self.level_number)



    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        player.gravity = 0.8
        player.can_wall_jump = False
        for sprite in self.tiles.sprites(): #todo consertar walljump após saber usar temporizador
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0: # melhor forma de ver com o que se está colidindo
                    player.rect.left = sprite.rect.right
                    self.vertical_movement_collision()
                    player.gravity = 0.3
                    player.reset_vertical_momentum()
                    player.can_wall_jump = True
                    player.wall_jump_direction = 6
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    self.vertical_movement_collision()
                    player.gravity = 0.3
                    player.reset_vertical_momentum()
                    player.can_wall_jump = True
                    player.wall_jump_direction = -6



    def player_movement(self):
        self.horizontal_movement_collision()
        self.vertical_movement_collision()

    

    def display_timer(self):
        time_passed = pygame.time.get_ticks() - self.start_time
        time_surface = self.text_font.render(f'{(self.time - time_passed)/1000:.2f}', False, 'Blue')
        self.display_surface.blit(time_surface, (1000,50))
        if self.time - time_passed <= 0:
            self.create_level(self.level_number)
        
        

    def mirror_colission_weapon(self):
        player = self.player.sprite
        if player.attack:
            mirrors = self.mirrors.sprites()
            weapon = player.weapon.sprite
            for mirror in mirrors:
                if mirror.rect.colliderect(weapon.rect) and mirror.status:
                    mirror.change_image_broken()
                    self.mirror_broken += 1
                    self.mirror_count_surface = self.text_font.render(f'{self.mirror_broken}/{self.mirror_quant}', False, 'Blue')
                    break
                    
    

    def run(self):
        self.display_surface.blit(self.background,(0,0))
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        self.mirrors.update(self.world_shift)
        self.mirrors.draw(self.display_surface)

        self.spikes.update(self.world_shift)
        self.spikes.draw(self.display_surface)

        self.exit.update(self.world_shift)
        self.exit.draw(self.display_surface)

        self.player.draw(self.display_surface)
        self.player.update(self.display_surface)
        self.player_movement()
        
        self.mirror_colission_weapon()
        self.input_return()
        self.display_timer()
        self.display_surface.blit(self.mirror_count_surface,(100,50))

