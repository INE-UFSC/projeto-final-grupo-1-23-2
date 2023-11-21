import pygame
from src.ferramentas.suporte import importar_csv

class Fase:
    def __init__(self, informacao_fase, surface):
        self.__display_superficie = surface
        terreno = importar_csv(informacao_fase['terreno'])
        self.__sprites_terreno = self.gerador_tiles(terreno, 'terreno')
        
        def gerador_tiles(self, layout, tipo):
            tiles = pygame.sprite.Group()
            for linha_indice, linha in enumerate(layout):
                for coluna_indice, valor in enumerate(linha):
                    if valor != '-1':
                        x = coluna_indice * 64
                        y = linha_indice * 64
                        
                    if tipo == 'terreno':
                        pass
            return tiles