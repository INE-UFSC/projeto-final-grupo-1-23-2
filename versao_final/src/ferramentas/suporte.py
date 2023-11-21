from os import walk
import pygame

def importar_pasta(path):
    surface_list = []

    for _, __, img_files in walk(path): 
        for imagem in img_files:
            full_path = path + '/' + imagem
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list
        
