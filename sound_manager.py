import pygame
from engine.sound import Sound
from engine.utils import path

pygame.mixer.init(frequency=44100, size=16, channels=2, buffer=4096)


resource = {
    'explosion': path('explosion.ogg', 'sound'),
    'enemy_explosion': path('explosion1.ogg', 'sound'),
    'airplane': path('airplane.ogg', 'sound'),
    'impact': path('impact.wav', 'sound'),
    'primaryw': path('primaryw.ogg', 'sound'),
}

fx = {
    'explosion': Sound(resource['explosion']),
    'enemy_explosion': Sound(resource['enemy_explosion']),
    'airplane': Sound(resource['airplane']),
    'impact': Sound(resource['impact']),
    'primaryw': Sound(resource['primaryw']),
}
