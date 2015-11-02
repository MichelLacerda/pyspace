# -*- coding: utf-8 -*-

import os
import sys
import pygame
from pygame.locals import *
from game_objects import (Player, Enemy, Bullet)
from engine.color import Color
from engine.vec2 import Vec2
from engine.sprite import SpriteBase
import process

# import packages
sys.path.insert(0, 'path')

# inicia pygame
pygame.init()

BASE_DIR = os.path.dirname(os.path.abspath('__file__')) + '/'

display = pygame.display.Info()

# FULLSCREEN
FS = False

if len(pygame.display.list_modes(display.bitsize)) <= 2:
    SCREEN_SIZE = pygame.display.list_modes(display.bitsize)[1]
else:
    SCREEN_SIZE = (display.current_w, display.current_h)


def path(name, type_of_resource='sprite'):
    """Return absolute path to file

    Keyword arguments:
        name -- file name
        type_of_resource - sprite, sound, ...
    """
    if type_of_resource == 'sprite':
        return BASE_DIR + 'assets/sprites/' + name
    elif type_of_resource == 'sound':
        return BASE_DIR + 'assets/sound/' + name

# Dicionario com todos os arquivos de midia do jogo
resource = {
    'spacecraft': path('spacecraft.png', 'sprite'),
    'enemy00': path('ship_enemy_00.png', 'sprite'),
    'bg': path('bg_001.gif', 'sprite'),
    'fire': path('fireb.png', 'sprite'),
    'explosion': path('explosion.ogg', 'sound'),
    'sound': path('hot.ogg', 'sound')
}

process.resource = resource

if FS:
    screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN, display.bitsize)
else:
    screen = pygame.display.set_mode((800, 600), 0, display.bitsize)
clock = pygame.time.Clock()
FPS = 60
background = pygame.image.load(resource['bg']).convert()

# Player
player = Player(200, 400, resource['spacecraft'])

# Enemy 00
enemy = Enemy(10, 200, resource['enemy00'])
enemy1 = Enemy(10, 100, resource['enemy00'])
enemy2 = Enemy(10, 300, resource['enemy00'])


def stereo_pan(x, width):
    rv = float(x)/width
    lv = 1.0 - rv
    return(lv, rv)

if music_channel is not None:
    l, r = stereo_pan(100, 800)
    music_channel.set_volume(l, r)
last_key = None


while True:

    # Eventos
    key = pygame.key.get_pressed()
    # Eventos

    # < Logica
    dt = clock.tick(FPS)/1000.0

    """Background color: cornflower (101, 156, 239)"""
    screen.fill(Color.CORNFLOWER)
    screen.blit(background, Vec2.ZERO)

    Enemy.update(dt)
    Bullet.update(dt)

    process.collision(player)
    process.keyboard(player, dt, key, last_key)

    # < Draw
    # Renderiza todos os sprites
    SpriteBase.group.draw(screen)
    Bullet.List.draw(screen)
    # Draw >

    pygame.display.flip()
    elapsed = clock.tick(FPS)

    last_key = key
