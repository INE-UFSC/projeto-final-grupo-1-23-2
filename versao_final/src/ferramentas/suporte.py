import os
import pygame


def importar_pasta(path):
    surface_list = []
    
    for file in sorted(os.listdir(path)):
        if file.endswith(".png") or file.endswith(".jpg"):
            full_path = os.path.join(path, file)
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list