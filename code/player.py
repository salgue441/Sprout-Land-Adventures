import pygame as pg

# From files
from support import import_folder
from Timer import GameTimer


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

        # Timers
        self.timers = {
            'tool use': GameTimer(350, self.use_tool),
            'tool switch': GameTimer(200),
            'seed use': GameTimer(350, self.use_seeds),
            'seed switch': GameTimer(200)
        }

        # Tool sets
        self.tools = ['hoe', 'axe', 'water']
        self.tool_index = 0
        self.selected_tool = self.tools[self.tool_index]

        # Seeds
        self.seeds = ['corn', 'tomato']
        self.seed_index = 0
        self.selected_seed = self.seeds[self.seed_index]

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

    def animate(self, dt) -> None:
        """ 
        Animates the player 
        :param: self - The object being created
        :param: dt - The time since the last frame
        :return: None
        """

        self.frame_index += 4 * dt

        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]

    def use_tool(self) -> None:
        """ 
        """
        pass

    def use_seeds(self) -> None:
        """
        """
        pass

    def input(self) -> None:
        """
        This method will be used to get the input from the player.
        :param: self - The object being created
        :return: None
        """

        keys = pg.key.get_pressed()

        if not self.timers['tool use'].active:
            # Horizontal Movement
            if keys[pg.K_a]:
                self.direction.x = -1
                self.status = 'left'

            elif keys[pg.K_d]:
                self.direction.x = 1
                self.status = 'right'

            else:
                self.direction.x = 0

            # Vertical Movement
            if keys[pg.K_w]:
                self.direction.y = -1
                self.status = 'up'

            elif keys[pg.K_s]:
                self.direction.y = 1
                self.status = 'down'

            else:
                self.direction.y = 0

            # Tool use
            if keys[pg.K_SPACE]:
                self.timers['tool use'].activate()
                self.direction = pg.math.Vector2()
                self.frame_index = 0

            # Chaning tools
            if keys[pg.K_q] and not self.timers['tool switch'].active:
                self.timers['tool switch'].activate()
                self.tool_index += 1

                self.tool_index = self.tool_index if self.tool_index < len(
                    self.tools) else 0

                self.selected_tool = self.tools[self.tool_index]

            # Seed Use
            if keys[pg.K_LCTRL]:
                self.timers['seed use'].activate()
                self.direction = pg.math.Vector2()
                self.frame_index = 0

            # Seed Change
            if keys[pg.K_e] and not self.timers['seed switch'].active:
                self.timers['seed switch'].activate()
                self.seed_index += 1

                self.seed_index = self.seed_index if self.seed_index < len(
                    self.seeds) else 0

                self.selected_seed = self.seeds[self.seed_index]

    def get_status(self) -> None:
        """
        Check if the player is not moving. If the player is not moving, 
        adds _idle to the status.
        :param: self - The object being created
        :return: None
        """

        if self.direction.magnitude() == 0:
            self.status = self.status.split('_')[0] + '_idle'

        if self.timers['tool use'].active:
            self.status = self.status.split('_')[0] + '_' + self.selected_tool

    def update_timers(self) -> None:
        """
        Updates the timer for the tools use property. 
        :param: self - The object being created. 
        :return: None
        """

        for timer in self.timers.values():
            timer.update()

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
        self.get_status()
        self.update_timers()

        self.move(dt)
        self.animate(dt)
