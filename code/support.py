from os import walk
import pygame


def import_folder(path: str) -> list:
    """
    Imports all images from a folder and returns them as a list of surfaces.
    :param path: The path to the folder.
    :return: A list of surfaces.
    """

    surface_list = []

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list
