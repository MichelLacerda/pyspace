import pygame


class SpriteBase(pygame.sprite.Sprite):
    sprites_group = pygame.sprite.Group()

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
        SpriteBase.sprites_group.add(self)

        self.image = pygame.image.load(image_str)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height