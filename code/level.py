import pygame as pg

# From files
from player import Player
from overlay import Overlay


class Level:
    def __init__(self) -> None:
        """
        This is the level class. This class will be used to create the level.
        :param: self - The object being created
        :return: None
        """

        # getting the display surface
        self.screen = pg.display.get_surface()

        # sprite groups
        self.all_sprites = pg.sprite.Group()

        self.setup()
        self.overlay = Overlay(self.player)

    def setup(self) -> None:
        """
        This method will be used to setup the level.
        :param: self - The object being created
        :return: None
        """

        self.player = Player((640, 360), self.all_sprites)

    def run(self, dt) -> None:
        """
        This method will be used to run the level.
        :param: self - The object being created
        :param: dt - The time since the last frame
        :return: None
        """

        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)

        self.all_sprites.update(dt)
        self.overlay.display()
