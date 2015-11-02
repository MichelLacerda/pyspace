import sys
import pygame
import game_objects
from engine.vec2 import Vec2
from pygame.locals import *
import sound_manager

sounds = sound_manager


def collision(player):
    for enemy in game_objects.Enemy.List:
        collisions = pygame.sprite.spritecollide(enemy,
                                                 game_objects.Bullet.List,
                                                 True)
        if len(collisions) > 0:
            for c in collisions:
                enemy.health -= enemy.damage(player.heft)
                sounds.fx['explosion'].play(enemy.rect.x, 800)


def keyboard(player, dt, key, last_key):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_e:
                # depois implementos outros tipos de tiro
                pass

    key_direction = Vec2(0, 0)

    if key[K_a]:
        key_direction.x = -1
    elif key[K_d]:
        key_direction.x = +1

    if key[K_SPACE] and key[K_SPACE] is not last_key[K_SPACE]:
        L = game_objects.Bullet(player.rect.x, player.rect.y,
                                'assets/sprites/fireb.png')

    key_direction.normalize()
    player.rect.x += key_direction.x * player.speed * dt
