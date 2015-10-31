import pygame


class SpriteBase(pygame.sprite.Sprite):
    """Base Class Sprite"""
    allsprites = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_str):
        """ Init params

        Keyword arguments:
            x -- position X
            y -- position Y
            width -- Horizontal dimension
            height -- Vertical dimension
            image_str -- Image file URL
        """
        pygame.sprite.Sprite.__init__(self)
        SpriteBase.allsprites.add(self)
        self.image = pygame.image.load(image_str)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height


class SpaceCraft(SpriteBase):
    List = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_str):
        SpriteBase.__init__(self, x, y, width, height, image_str)
        SpaceCraft.List.add(self)

        self.velx = 0

    def move(self, dt):
        ray = self.rect.x + self.velx
        if ray < 0:
            self.velx = 0
        elif ray + self.width > 640:
            self.velx = 0

        self.rect.x += self.velx * dt
