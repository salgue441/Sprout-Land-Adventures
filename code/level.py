import pygame as pg

# From files
from settings import LAYERS
from player import Player
from overlay import Overlay
from CameraGroup import CameraGroup
from sprites import GenericSprite


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
        self.all_sprites = CameraGroup()

        self.setup()
        self.overlay = Overlay(self.player)

    def setup(self) -> None:
        """
        This method will be used to setup the level.
        :param: self - The object being created
        :return: None
        """

        # Player
        self.player = Player((640, 360), self.all_sprites)

        # Ground
        GenericSprite(
            position=(0, 0),
            surface=pg.image.load(
                '../graphics/world/ground.png').convert_alpha(),
            group=self.all_sprites,
            z=LAYERS['ground']
        )

    def run(self, dt) -> None:
        """
        This method will be used to run the level.
        :param: self - The object being created
        :param: dt - The time since the last frame
        :return: None
        """

        self.screen.fill((0, 0, 0))
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)

        self.overlay.display()
