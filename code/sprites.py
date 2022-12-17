import pygame as pg

# From files
from settings import LAYERS


class GenericSprite(pg.sprite.Sprite):
    def __init__(self, position, surface, group, z=LAYERS['main']) -> None:
        """
        This is the Generic Sprite Class. This class will be used to create 
        Generic Sprites. 
        :param: self - The object being created. 
        :param: position - Position of the sprite.
        :param: surface - Surface of the Sprite. 
        :param: Groups - Sprite's group
        :return: None
        """

        super().__init__(group)

        self.image = surface
        self.rect = self.image.get_rect(topleft=position)
        self.z = z
