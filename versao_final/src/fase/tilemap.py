import pygame
from ferramentas.suporte import importar_pasta

class Tile(pygame.sprite.Sprite):
    def __init__(self, posicao, tamanho):
        super().__init__()
        self.__image = pygame.Surface((tamanho,tamanho))
        self.__rect = self.__image.get_rect(topleft = posicao)
        
        def update(self, shift):
            self.__rect.x += shift
            
class TileEstatico(Tile):
    def __init__(self, posicao, x, y, surface):
        super().__init__(posicao, x, y)
        self.__image = surface
        
class TileDinamico(Tile):
    def __init__(self, posicao, x, y, caminho_pasta):
        super().__init__(posicao, x, y)
        self.__frames = importar_pasta(caminho_pasta)
        self.__frame_index = 0
        self.__image = self.__frames[self.__frame_index]
        
    def animar(self):
        self.__frame_index += 0.15
        if self.__frame_index >= len(self.__frames):
            self.__frame_index = 0
        self.__image = self.__frames[int(self.__frame_index)]
        
    def update(self, shift):
        self.animar()
        self.__rect.x += shift