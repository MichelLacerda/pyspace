import pygame
import sys


def get(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        player.velx = 5
    elif keys[pygame.K_a]:
        player.velx = -5
    else:
        player.velx = 0
