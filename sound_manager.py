import pygame
from engine.sound import Sound
from engine.utils import path

pygame.mixer.init(frequency=44100, size=16, channels=2, buffer=4096)


resource = {
    'explosion': path('explosion.ogg', 'sound'),
    'enemy_explosion': path('explosion_e.ogg', 'sound'),
    'airplane': path('airplane.ogg', 'sound'),
    'impact': path('impact.wav', 'sound'),
    'primaryw': path('primaryw.ogg', 'sound'),
    'explosion_0': path('explosion_0.ogg', 'sound'),
    'collapse': path('collapse.ogg', 'sound'),
}

fx = {
    'explosion': Sound(resource['explosion']),
    'enemy_explosion': Sound(resource['enemy_explosion']),
    'airplane': Sound(resource['airplane']),
    'impact': Sound(resource['impact']),
    'primaryw': Sound(resource['primaryw']),
    'explosion_0': Sound(resource['explosion_0']),
}

sound_background = pygame.mixer.Sound(resource['collapse'])
channel_background = sound_background.play(-1)

if channel_background is not None:
    channel_background.set_volume(0.7)
    


