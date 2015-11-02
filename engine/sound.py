import pygame
import sys
from pygame.locals import *


def stereo_pan(x, width):
    rv = float(x)/width
    lv = 1.0 - rv
    return(lv, rv)


class Sound(object):
    def __init__(self, sound_str):
        self.sound = pygame.mixer.Sound(sound_str)

    def play(self, x, width=None):
        self.channel = self.sound.play()
        
        
        if self.channel is not None:
            if x and width:
                l, r = stereo_pan(x, width)
                self.channel.set_volume(l, r)
            else:
                self.channel.set_volume(float(x))


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((100, 100), 0, 16)

    musica = Sound('assets/sound/explosion.ogg')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        key = pygame.key.get_pressed()

        if key[K_p]:
            musica.play()
        screen.fill((0, 0, 0))

        pygame.display.update()
