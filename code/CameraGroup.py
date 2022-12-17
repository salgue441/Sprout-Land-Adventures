import pygame as pg

# From files
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, LAYERS


class CameraGroup(pg.sprite.Group):
    def __init__(self) -> None:
        """
        This is the CameraGroup Class. This class will be used to create the
        Game's Camera.
        :param: self - The object being created.
        :return: None
        """
        super().__init__()
        self.display_surface = pg.display.get_surface()

        self.offset = pg.math.Vector2()

    def custom_draw(self, player) -> None:
        """
        Custom draw function. 
        :param: self - The object being created. 
        :return: None
        """

        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

        for layer in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset

                    self.display_surface.blit(sprite.image, offset_rect)
