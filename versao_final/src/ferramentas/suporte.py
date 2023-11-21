from os import walk
from csv import reader
import pygame

def importar_pasta(path):
    surface_list = []

    for _, __, img_files in walk(path):
        img_files = [img for img in img_files if img[-3:] == 'png' or img[-3:] == 'jpg']
        for imagem in img_files:
            full_path = path + '/' + imagem
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list

def importar_csv(path):
    mapa_terreno = []
    with open(path) as mapa:
        fase = reader(mapa, delimiter= ',')
        for linha in fase:
            mapa_terreno.append(linha)
        return mapa_terreno