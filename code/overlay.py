import pygame as pg

# From files
from settings import OVERLAY_POSITIONS


class Overlay:
    def __init__(self, player) -> None:
        """
        This is the overlay class. This class be used to create the overlay. 
        :param: self - The object being created.
        :return: None
        """

        self.display_surface = pg.display.get_surface()
        self.player = player

        # imports
        overlay_path = "../graphics/overlay/"

        self.tools_surface = {
            tool: pg.image.load(f'{overlay_path}{tool}.png').convert_alpha()
            for tool in player.tools
        }

        self.seeds_surface = {
            seed: pg.image.load(f'{overlay_path}{seed}.png').convert_alpha()
            for seed in player.seeds
        }

    def display(self) -> None:
        """
        Displays the tool's and seed's surfaces. 
        :param: self - The object being created. 
        :return: None
        """

        # tool
        tool_surf = self.tools_surface[self.player.selected_tool]
        tool_rect = tool_surf.get_rect(midbottom=OVERLAY_POSITIONS['tool'])
        self.display_surface.blit(tool_surf, tool_rect)

        # seed
        seed_surf = self.seeds_surface[self.player.selected_seed]
        seed_rect = seed_surf.get_rect(midbottom=OVERLAY_POSITIONS['seed'])
        self.display_surface.blit(seed_surf, seed_rect)
