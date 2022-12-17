import pygame as pg


class CameraGroup(pg.sprite.Group):
    def __init__(self) -> None:
        """
        This is the CameraGroup Class. his class be used to create the
        Game's Camera.
        :param: self - The object being created.
        :return: None
        """
        super().__init__()
        self.display_surface = pg.display.get_surface()

    def custom_draw(self) -> None:
        """
        Custom draw function. 
        :param: self - The object being created. 
        :return: None
        """

        for sprite in self.sprites():
            self.display_surface.blit(sprite.image, sprite.rect)
