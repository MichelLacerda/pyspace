import pygame
import game_objects
from engine.vec2 import Vec2
from pygame.locals import *
sounds = None

def init(sounds):
    sounds = sounds
    

def collision(player):
    for enemy in game_objects.Enemy.List:
        collisions = pygame.sprite.spritecollide(enemy, game_objects.Bullet.List, True)
        if len(collisions) > 0:
            for c in collisions:
                enemy.health -= enemy.damage(player.heft)

def keyboard(player, dt, keys):
    key_direction = Vec2(0, 0)
    
    if keys[K_a]:
        key_direction.x = -1
    elif keys[K_d]:
        key_direction.x = +1
        
    if keys[K_SPACE]:
        L = game_objects.Bullet(player.rect.x, player.rect.y, 'assets/sprites/fireb.png')
    print(player.rect.x, player.rect.y)
    key_direction.normalize()
    player.rect.x += key_direction.x * player.speed * dt