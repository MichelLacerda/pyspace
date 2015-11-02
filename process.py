import sys
import pygame
import game_objects
from engine.vec2 import Vec2
from pygame.locals import *
import sound_manager as sounds


def collision(player):
    
    if len(game_objects.Enemy.List) >= 1:
        for enemy in game_objects.Enemy.List:
            bullets = game_objects.Bullet.List
            collision = pygame.sprite.spritecollide(enemy, bullets, False)
            if collider(collision):
                enemy.health -= enemy.damage(player.heft)
                sounds.fx['impact'].play(enemy.rect.x, 800)


def collider(list_objects):
    for hit in list_objects:
        hit.destroy(game_objects.Bullet)
        return True
    return False 


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
        game_objects.Bullet(player.rect.x, player.rect.y,
                            'assets/sprites/fireb.png')
        sounds.fx['primaryw'].play(0.2)

    key_direction.normalize()
    player.rect.x += key_direction.x * player.speed * dt
