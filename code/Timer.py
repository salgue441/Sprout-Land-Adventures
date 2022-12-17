import pygame as pg


class GameTimer:
    def __init__(self, duration, function=None) -> None:
        """
        This is the timer class. This class is used for creating a timer. 
        :param: self - The object being created.
        :param: duration - The duration of the timer. 
        :param: function - 
        :return: None
        """

        self.duration = duration
        self.function = function

        self.start_time = 0
        self.active = False

    def activate(self) -> None:
        """
        Activates the timer. 
        :param: self - The object being created. 
        :return: None
        """

        self.active = True
        self.start_time = pg.time.get_ticks()

    def deactivate(self) -> None:
        """
        Deactivates the timer. Resets the variables to their original value.
        :param: self - The object being created. 
        :return: None
        """

        self.active = False
        self.start_time = 0

    def update(self) -> None:
        """
        Updates the timer. 
        :param: self - The object being created. 
        :return: None
        """

        current_time = pg.time.get_ticks()

        if current_time - self.start_time >= self.duration:
            self.deactivate()

            if self.function:
                self.function()
