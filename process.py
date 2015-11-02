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
    elif key[K_w]:
        key_direction.y = -1
    elif key[K_s]:
        key_direction.y = +1
        
    ray = player.rect.x + key_direction.x
    
    
    
    if key[K_SPACE] and key[K_SPACE] is not last_key[K_SPACE]:
        game_objects.Bullet(player.rect.x, player.rect.y,
                            'assets/sprites/fireb.png')
        game_objects.Bullet(player.rect.x+player.rect.width, player.rect.y,
                            'assets/sprites/fireb.png')
        # sounds.fx['primaryw'].play(player.rect.x, 800)

    key_direction.normalize()
    
    if ray < 0:
        player.rect.x = 0
    elif ray + player.rect.width > 800:
        player.rect.x = 800 - player.rect.width
        
            
    player.rect.x += key_direction.x * player.speed * dt
    player.rect.y += key_direction.y * player.speed * dt
