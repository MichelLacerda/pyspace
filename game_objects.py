import pygame
from pygame.locals import *
from engine.sprite import SpriteBase
from engine.vec2 import Vec2

from random import randint
from math import sin


class Player(SpriteBase):
    List = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_str):
        SpriteBase.__init__(self, x, y, width, height, image_str)
        Player.List.add(self)
        self.velx = 0
        self.speed = 230
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


class Enemy(SpriteBase):
    List = pygame.sprite.Group()
    def __init__(self, x, y, width, height, image_str):
        SpriteBase.__init__(self, x, y, width, height, image_str)
        Enemy.List.add(self)
        self.velx = randint(150, 180)
        self.amplitude, self.period = randint(20, 140), randint(4, 5) / 100.0
    
    def move(self, dt):
        if self.rect.x + self.width > 800 or self.rect.x < 0:
            self.image = pygame.transform.flip(self.image, True, True)
            self.velx *= -1
        
        self.rect.x += self.velx * dt
        # a * sin(bx + c) + y
        self.rect.y = self.amplitude * sin(self.period * self.rect.x) + 140
        
        print(self.velx, dt)
    
    @staticmethod
    def update(dt):
        for enemy in Enemy.List:
            enemy.move(dt)