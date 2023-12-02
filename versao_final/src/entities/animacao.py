from abc import ABC, abstractmethod
import os
import pygame

class Animacao(ABC):

    def __init__(self, path: str):
        self.__animacao = []
        self.importar_pasta(path)

    def importar_pasta(self, path):
        surface_list = []
        
        for file in sorted(os.listdir(path)):
            if file.endswith(".png") or file.endswith(".jpg"):
                full_path = os.path.join(path, file)
                image_surf = pygame.image.load(full_path).convert_alpha()
                surface_list.append(image_surf)
        self.__animacao = surface_list

    @abstractmethod
    def animar(self):
        pass

    @property
    def animacao(self):
        return self.__animacao
    
    @property
    def index_animacao(self):
        return self.__index_animacao
    
    @property
    def velocidade_animacao(self):
        return self.__velocidade_animacao
    