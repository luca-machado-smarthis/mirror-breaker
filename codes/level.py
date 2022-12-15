import pygame

from player import Player
from setting import *
from tiles import Tile
from mirror import Mirror
from spike import Spike
from fireBreather import FireBreather, FireWall
from exit import Exit
from button import Button
from setting import level_maps, firebreathers_orientations
from golem import Golem, GolemMarker


class Level:
    def __init__(self, surface, create_menu, create_level, level_number):
        # Cores
        self.display_surface = surface
        self.background = pygame.image.load(
            'assets/background.jpg').convert_alpha()
        self.text_font = pygame.font.Font(None, 100)
        self.create_menu = create_menu  # Depois usar para retornar ao menu
        # Depois usar quando terminar a fase para poder ir para proxima
        self.create_level = create_level

        # Groups
        self.buttons_loss = pygame.sprite.Group()
        self.buttons_win = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()
        self.mirrors = pygame.sprite.Group()
        self.spikes = pygame.sprite.Group()
        self.fire_breathers = pygame.sprite.Group()
        self.firebreathers_orientation = firebreathers_orientations[level_number].copy(
        )
        self.firewalls = pygame.sprite.Group()
        self.golems = pygame.sprite.Group()
        self.golem_markers = pygame.sprite.Group()
        self.exit = pygame.sprite.GroupSingle()
        # sempre cria um grupo (mesmo que solitário) e depois instancia e  adiciona
        self.player = pygame.sprite.GroupSingle()

        # Integers
        self.world_shift = 0
        self.mirror_quant = 0
        self.mirror_broken = 0
        self.level_number = level_number  # Next level seria isso + 1

        # Set-up
        self.setup_level(level_maps[level_number])
        self.ad_buttons()
        self.mirror_count_surface = self.text_font.render(
            f'{self.mirror_broken}/{self.mirror_quant}', False, (0, 0, 255))
        self.time = timer_maps[level_number]
        self.start_time = pygame.time.get_ticks()
        self.status = 'run'
        pygame.mixer.music.load('assets/music/mainTheme.ogg')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

    def setup_level(self, layout):
        for row_index, row in enumerate(layout):
            row_index -= 1
            for col_index, cell in enumerate(row):
                if row_index == -1:
                    for i in range(2):
                        for j in range(2):
                            tile = Tile((col_index * tile_size + i*28,
                                        row_index * tile_size + j*28 - 56))
                            self.tiles.add(tile)
                else:
                    if cell == 'x' or cell == 'X':
                        for i in range(2):
                            for j in range(2):
                                tile = Tile(
                                    (col_index * tile_size + i*28, row_index * tile_size + j*28))
                                self.tiles.add(tile)
                    elif cell == 'P':
                        player_sprite = Player(
                            (col_index * tile_size, row_index * tile_size))
                        self.player.add(player_sprite)
                        # Tem que arranjar um jeito de começar a camera no player
                    elif cell == 'M':
                        mirror = Mirror(
                            (col_index * tile_size, (row_index-1) * tile_size))
                        self.mirrors.add(mirror)
                        self.mirror_quant += 1
                    elif cell == 'S':
                        for i in range(4):
                            spike = Spike(
                                (col_index * tile_size + i*14, (row_index+1) * tile_size))
                            self.spikes.add(spike)
                    elif cell == 'F':
                        for i in range(2):
                            for j in range(2):
                                # PORQUE TEM QUE POR +1 AQUI????
                                tilefb = Tile(
                                    (col_index * tile_size + i*28, (row_index+1) * tile_size + j*28 - 56))
                                self.tiles.add(tilefb)
                        fire_breather_sprite = FireBreather(pos=(
                            col_index * tile_size+3, (row_index+1) * tile_size-3), orientation=self.firebreathers_orientation[0])
                        self.firebreathers_orientation.pop(0)
                        self.fire_breathers.add(fire_breather_sprite)
                    elif cell == 'W':
                        for i in range(2):
                            for j in range(2):
                                # PORQUE TEM QUE POR +1 AQUI????
                                tilemk = Tile(
                                    (col_index * tile_size + i*28, (row_index+1) * tile_size + j*28 - 56))
                                self.tiles.add(tilemk)
                        marker = GolemMarker(
                            (col_index * tile_size, (row_index+1) * tile_size))
                        self.golem_markers.add(marker)
                    elif cell == 'w':
                        marker = GolemMarker(
                            (col_index * tile_size, (row_index+1) * tile_size))
                        self.golem_markers.add(marker)
                    elif cell == 'G':
                        golem = Golem(
                            (col_index * tile_size, (row_index+1) * tile_size))
                        self.golems.add(golem)
                    elif cell == 'E':
                        exit_sprite = Exit(
                            (col_index * tile_size, (row_index+1) * tile_size))
                        self.exit.add(exit_sprite)
        for fb in self.fire_breathers:
            firewall = FireWall(pos=(fb.pos), orientation=fb.orientation)
            self.firewalls.add(firewall)
        self.firebreathers_orientation = firebreathers_orientations[self.level_number].copy(
        )

    def ad_buttons(self):
        self.buttons_loss.add(Button('assets/button/retryButton_fade.png', 'assets/button/retryButton_full.png',
                              (screen_width/2 - 90, 200), self.create_level, self.level_number, False))
        self.buttons_loss.add(Button('assets/button/menuButton_fade.png', 'assets/button/menuButton_full.png',
                              (screen_width/2 - 90, 350), self.create_menu, self.level_number, False))
        self.buttons_win.add(Button('assets/button/nextLevelButton_fade.png', 'assets/button/nextLevelButton_full.png',
                             (screen_width/2 - 90, 300), self.create_level, self.level_number+1, False))
        self.buttons_win.add(Button('assets/button/menuButton_fade.png', 'assets/button/menuButton_full.png',
                             (screen_width/2 - 90, 450), self.create_menu, self.level_number+1, False))

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        if player_x < screen_width/5 and direction_x < 0:
            self.world_shift = player.stored_speed
            player.speed = 0
        elif player_x > screen_width*4/5 and direction_x > 0:
            self.world_shift = -player.stored_speed
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = player.stored_speed

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        for sprite in self.tiles.sprites():  # todo adicionar wallJUmp
            if sprite.rect.colliderect(player.rect):
                if player.direction.y < 0:  # melhor forma de ver com o que se está colidindo
                    player.rect.top = sprite.rect.bottom
                    player.reset_vertical_momentum()
                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.can_jump = True
                    player.reset_vertical_momentum()

    def input_return(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.mixer.music.pause()
            self.create_menu(self.level_number)

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        player.gravity = player.stored_gravity
        player.can_wall_jump = False
        for sprite in self.tiles.sprites():  # todo consertar walljump após saber usar temporizador
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:  # melhor forma de ver com o que se está colidindo
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
        self.time_surface = self.text_font.render(
            f'{(self.time - time_passed)/1000:.2f}', False, (0, 0, 255))
        if self.time - time_passed <= 0:
            self.status = 'loss'
        self.display_surface.blit(self.time_surface, (970, 50))

    def mirror_colission_weapon(self):
        player = self.player.sprite
        if player.attack:
            mirrors = self.mirrors.sprites()
            weapon = player.weapon.sprite
            pygame.sprite.spritecollide(weapon, self.golems, True)
            for mirror in mirrors:
                if mirror.rect.colliderect(weapon.rect) and mirror.status:
                    mirror.change_image_broken()
                    self.mirror_broken += 1
                    self.win_condition()
                    self.mirror_count_surface = self.text_font.render(
                        f'{self.mirror_broken}/{self.mirror_quant}', False, (0, 0, 255))
                    break

    def win_condition(self):
        if self.mirror_quant == self.mirror_broken:
            self.status = 'clear'
            exit = self.exit.sprite
            exit.open_exit()
            self.clear_time = True  # toDo armazenar o tempo de clear

    def next_level(self):
        if self.status == 'clear':
            player = self.player.sprite
            exit = self.exit.sprite
            if player.rect.colliderect(exit.rect):
                self.status = 'won'
                self.won_time = True  # toDo armazenar o tempo total que demorou até saida da fase

    def golem_collide(self):
        for golem in self.golems:
            if pygame.sprite.spritecollide(golem, self.golem_markers, False):
                golem.reverse()

    def death(self):
        player = self.player.sprite
        if pygame.sprite.spritecollide(player, self.spikes, False):
            self.status = 'loss'

        if pygame.sprite.spritecollide(player, self.firewalls, False):
            if self.firewalls.sprites() and self.firewalls.sprites()[0].active:
                self.status = 'loss'
        if pygame.sprite.spritecollide(player, self.golems, False):
            self.status = 'loss'

        if player.rect.top >= screen_height:
            self.status = 'loss'

    def run(self):
        self.display_surface.blit(self.background, (0, 0))
        if self.status == 'loss':
            pygame.mixer.music.pause()
            self.display_surface.blit(self.text_font.render(
                'You Lose', False, (0, 0, 255)), (450, 50))
            self.buttons_loss.draw(self.display_surface)
            self.buttons_loss.update()
        elif self.status == 'won':
            pygame.mixer.music.pause()
            self.display_surface.blit(self.text_font.render(
                'You Won', False, (0, 0, 255)), (450, 50))
            # Display do clear_time e do won_time
            self.buttons_win.draw(self.display_surface)
            self.buttons_win.update()
        else:
            self.tiles.update(self.world_shift)
            self.tiles.draw(self.display_surface)
            self.scroll_x()

            self.mirrors.update(self.world_shift)
            self.mirrors.draw(self.display_surface)

            self.spikes.update(self.world_shift)
            self.spikes.draw(self.display_surface)

            self.fire_breathers.update(self.world_shift)
            self.fire_breathers.draw(self.display_surface)

            self.golem_collide()
            self.golems.update(self.world_shift)
            self.golems.draw(self.display_surface)
            self.golem_markers.update(self.world_shift)

            self.firewalls.update(self.world_shift)
            if self.firewalls.sprites() and self.firewalls.sprites()[0].active:
                self.firewalls.draw(self.display_surface)

            self.exit.update(self.world_shift)
            self.exit.draw(self.display_surface)

            self.player_movement()
            self.player.draw(self.display_surface)
            self.player.update(self.display_surface)

            self.mirror_colission_weapon()
            self.display_timer()
            self.display_surface.blit(self.mirror_count_surface, (60, 50))
            self.death()
            self.next_level()
        self.input_return()
