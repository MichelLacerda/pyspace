import pygame
from pygame.locals import *
from engine.sprite import SpriteBase
from engine.vec2 import Vec2

class Player(SpriteBase):
    List = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_str):
        SpriteBase.__init__(self, x, y, width, height, image_str)
        Player.List.add(self)
        self.velx = 0
        self.speed = 150
        self.position = Vec2(x, y)
    
    def move(self, dt):
        # ray = self.rect.x + self.velx
        # if ray < 0:
        #     self.velx = 0
        # elif ray + self.width > 800:
        #     self.velx = 0

        # self.rect.x += self.velx * dt
        pass
    def update(self, dt, keys):
        key_direction = Vec2(0, 0)
        
        if keys[K_a]:
            key_direction.x = -1
        elif keys[K_d]:
            key_direction.x = +1
            
        key_direction.normalize()
        self.rect.x += key_direction.x * self.speed * dt
        