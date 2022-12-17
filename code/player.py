import pygame as pg

# From files
from support import import_folder


class Player(pg.sprite.Sprite):
    def __init__(self, position, group) -> None:
        """
        This is the player class. This class will be used to create the player.
        :param: self - The object being created
        :param: position - The position of the player
        :param: group - The group the player will be added to
        :return: None
        """
        # Sprite calls
        super().__init__(group)

        # Importing the assets
        self.import_assets()
        self.status = "down_idle"
        self.frame_index = 0

        # General setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=position)

        # Movement Attributes
        self.direction = pg.math.Vector2()
        self.pos = pg.math.Vector2(self.rect.center)
        self.speed = 200

    def import_assets(self) -> None:
        """
        This method will be used to import the assets for the player.
        :param: self - The object being created
        :return: None
        """

        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                           'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [],
                           'right_hoe': [], 'left_hoe': [], 'up_hoe': [], 'down_hoe': [],
                           'right_axe': [], 'left_axe': [], 'up_axe': [], 'down_axe': [],
                           'right_water': [], 'left_water': [], 'up_water': [], 'down_water': []}

        for animation in self.animations.keys():
            full_path = '../graphics/character/' + animation
            self.animations[animation] = import_folder(full_path)

    def input(self) -> None:
        """
        This method will be used to get the input from the player.
        :param: self - The object being created
        :return: None
        """

        keys = pg.key.get_pressed()

        # Horizontal Movement
        if keys[pg.K_a]:
            self.direction.x = -1

        elif keys[pg.K_d]:
            self.direction.x = 1

        else:
            self.direction.x = 0

        # Vertical Movement
        if keys[pg.K_w]:
            self.direction.y = -1

        elif keys[pg.K_s]:
            self.direction.y = 1

        else:
            self.direction.y = 0

    def move(self, dt) -> None:
        """
        This method will be used to move the player.
        :param: self - The object being created
        :param: dt - The time since the last frame
        :return: None
        """

        # Normalizing the direction
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # Moving the player
        # X axis
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        # Y axis
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt) -> None:
        """
        This method will be used to update the player.
        :param: self - The object being created
        :param: dt - The time since the last frame
        :return: None
        """

        self.input()
        self.move(dt)
