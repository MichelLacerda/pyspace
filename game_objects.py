import pygame
from engine.sprite import SpriteBase
from engine.vec2 import Vec2

from random import randint
from math import sin, cos

import sound_manager as sounds

pygame.mixer.init(frequency=44100, size=16, channels=2, buffer=4096)

def s_pan(x, width):
    rv = float(x)/width
    lv = 1.0 - rv
    return(lv, rv)

class Player(SpriteBase):
    List = pygame.sprite.Group()

    def __init__(self, x, y, image_str):
        SpriteBase.__init__(self, x, y, image_str)
        Player.List.add(self)

        # heft(peso): poder de destruição
        self.heft = 5
        self.velx = 0
        self.speed = 300
        self.position = Vec2(x, y)
        self.airplane = pygame.mixer.Sound(sounds.resource['airplane'])
        self.airplane_channel = self.airplane.play(-1)
        

    def move(self, dt):
        # sounds.fx['airplane'].play(self.rect.x, 800)
        # ray = self.rect.x + self.velx
        # if ray < 0:
        #     self.velx = 0
        # elif ray + self.rect.width > 800:
        #     self.velx = 0

        # self.rect.x += self.velx * dt
        pass


    def update(self, dt):
        if self.airplane_channel is not None:
            l, r = s_pan(self.rect.x, 800)
            self.airplane_channel.set_volume(l, r)


class Enemy(SpriteBase):
    List = pygame.sprite.Group()

    def __init__(self, x, y, image_str):
        SpriteBase.__init__(self, x, y, image_str)
        Enemy.List.add(self)

        w, h = self.image.get_size()
        scale = 1
        self.image = pygame.transform.scale(self.image,
                                            (int(w*scale), int(h*scale)))
        self.health = 100.0

        # perda em porcentagem
        self.loss = 10

        self.velx = randint(100, 100)
        self.vely = randint(80, 120)
        self.amplitude, self.period = randint(400,440), randint(2, 5) / 100.0
        # self.amplitude, self.period = randint(20, 140), randint(4, 5) / 100.0

    def move(self, dt):
        # if self.rect.x + self.rect.width > 800 or self.rect.x < 0:
        #     self.image = pygame.transform.flip(self.image, True, True)
        #     self.velx *= -1

        # self.rect.x += self.velx * dt
        self.rect.y += self.vely * dt
        
        # http://matematicasfuncionestrigonometricas.blogspot.com.br/2011_10_01_archive.html
        # a * sin(bx + c) + y
        
        # self.rect.y = self.amplitude * sin(self.period * self.rect.x) + 140
        # self.rect.y = self.amplitude * sin(self.period * self.rect.x) + 140
        
        self.rect.x = self.amplitude * cos(self.period * (self.rect.y - self.rect.width/2)) + (400 - self.rect.width/2)

    def damage(self, heft):
        return (self.health * self.loss / 100.0) + heft

    @staticmethod
    def update(dt):
        for enemy in Enemy.List:
            if enemy.health <= 0:
                enemy.destroy(Enemy)
            else:
                enemy.move(dt)


class Bullet(SpriteBase):
    List = pygame.sprite.Group()
    n_list = []

    def __init__(self, x, y, image_str):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_str)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        try:
            l_element = Bullet.n_list[-1]
            diff = abs(self.rect.y - (l_element.rect.y + 10))

            if diff < self.rect.height:
                return
        except Exception:
            pass

        Bullet.n_list.append(self)
        Bullet.List.add(self)
        self.vely = -300.0

    @staticmethod
    def update(dt):
        for bullet in Bullet.List:
            
            if bullet.rect.y < 0:
                bullet.destroy(Bullet)
                pass
            else:
                bullet.rect.y += bullet.vely * dt

    # @classmethod
    # def destroy(self, class_name):
    #     class_name.List.remove(self)
    #     SpriteBase.group.remove(self)
    #     del self
