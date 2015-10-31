# -*- coding: utf-8 -*-
# teste 
import pygame
import sys
import os
from classes import (SpaceCraft, SpriteBase)
import player.keyboard_manager

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/'

def algo(algo):
    pass

def path(name, type_of_resource='sprite'):
    """Return absolute path to file

    Keyword arguments:
        name -- file name
        type_of_resource - sprite, sound, ...
    """
    if type_of_resource == 'sprite':
        return BASE_DIR + 'assets/sprites/' + name

resource = {
    'spacecraft': path('spacecraft.png', 'sprite'),
    'test': path(''),
}


SCREEN_SIZE = (640, 480)
W, H = SCREEN_SIZE
pygame.init()
screen = pygame.display.set_mode((W, H), 0, 32)

spacecraft_img = pygame.image.load(resource['spacecraft']).convert_alpha()
clock = pygame.time.Clock()
FPS = 24

spacecraft = SpaceCraft(200, 200, 71, 77, resource['spacecraft'])

c1 = (255, 0, 0)
c2 = (0, 255, 0)
c3 = (0, 0, 255)
while True:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    player.keyboard_manager.get(spacecraft)
    # Eventos

    # Logica
    time_passed = clock.tick(FPS)
    dt = time_passed / 1000.0
    # Logica

    # Draw
    """Background color: cornflower (101, 156, 239)"""
    screen.fill((101, 156, 239))

    spacecraft.move(dt)
    SpriteBase.allsprites.draw(screen)
    # SpadceCraft.List.draw(screen)

    pygame.draw.line(screen, c2, (0, 0), (SCREEN_SIZE[0], SCREEN_SIZE[1]), 1)
    pygame.draw.rect(screen, c1, (16, 16, 32, 32))
    pygame.draw.circle(screen, c3, (64, 64), 32, 1)

    pygame.display.flip()
    # Draw
