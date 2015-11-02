import pygame
from engine.sound import Sound
from engine.utils import path

pygame.mixer.init(frequency=44100, size=16, channels=2, buffer=4096)


resource = {
    'explosion': path('explosion.ogg', 'sound')
}

fx = {
    "explosion": Sound(resource['explosion']),
}