# -*- coding: utf-8 -*-

import pygame
import sys
import os
from player import Player
from engine import keyboard_manager

from engine.vec2 import Vec2

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/'
SCREEN_SIZE = (800, 600)
W, H = SCREEN_SIZE


def path(name, type_of_resource='sprite'):
    """Return absolute path to file

    Keyword arguments:
        name -- file name
        type_of_resource - sprite, sound, ...
    """
    if type_of_resource == 'sprite':
        return BASE_DIR + 'assets/sprites/' + name

# Dicionario com todos os arquivos de midia do jogo
resource = {
    'spacecraft': path('spacecraft.png', 'sprite'),
    'bg': path('bg_001.gif', 'sprite'),
}

# inicia pygame
pygame.init()
screen = pygame.display.set_mode((W, H), 0, 32)
clock = pygame.time.Clock()
FPS = 30
background = pygame.image.load(resource['bg']).convert()

# Player
player = Player(200, 200, 71, 77, resource['spacecraft'])

c1 = (255, 0, 0)
c2 = (0, 255, 0)
c3 = (0, 0, 255)

layers = []
elapsed = 0.0
while True:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keyboard_manager.get(player)
    keys = pygame.key.get_pressed()
    # Eventos

    # < Logica
    dt = elapsed/1000.0
    
    player.update(dt, keys)
    
    elapsed = clock.tick(FPS)
    # Logica >

    # < Draw
    """Background color: cornflower (101, 156, 239)"""
    screen.fill((101, 156, 239))

    player.move(dt)
    
    screen.blit(background, Vec2.ZERO)

    Player.List.draw(screen)

    for layer in layers:
        pass

    pygame.display.flip()
    # Draw >

def test():
    # desenha formas
    pygame.draw.line(screen, c2, (0, 0), (SCREEN_SIZE[0], SCREEN_SIZE[1]), 1)
    pygame.draw.rect(screen, c1, (16, 16, 32, 32))
    pygame.draw.circle(screen, c3, (64, 64), 32, 1)
    # SpadceCraft.List.draw(screen)
