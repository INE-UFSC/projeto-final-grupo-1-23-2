from pytmx.util_pygame import load_pygame
import os

class Mapas:
    def __init__(self, path_pasta):
        self.__mapas = []
        self.carrega_mapas(path_pasta)
        
    def carrega_mapas(self, path_pasta):
        for file in sorted(os.listdir(path_pasta)):
            if file.endswith(".tmx"):
                self.__mapas.append(load_pygame(os.path.join(path_pasta, file)))
    
    @property
    def mapas(self):
        return self.__mapas