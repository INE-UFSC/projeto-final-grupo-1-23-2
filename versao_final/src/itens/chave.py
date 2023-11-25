import pygame
from src.ferramentas.suporte import importar_pasta

class Chave(pygame.sprite.Sprite):
    def __init__(self, posicao):
        super().__init__()
        
        #animacao inimigo
        self.importar_assets()
        self.__posicao_inicial = posicao
        self.__index_animacao = 0
        self.__velocidade_animacao = 0.1
        self.__image = self.__animacao[self.__index_animacao]
        self.__rect = self.__image.get_rect(topleft = posicao)
        

    def importar_assets(self):
        path_personagem = 'assets/tiles/chave'
        self.__animacao = []
        self.__animacao = importar_pasta(path_personagem)

    def animar(self):
        self.__index_animacao += self.__velocidade_animacao
        if self.__index_animacao > len(self.__animacao):
            self.__index_animacao = 0
        
        self.__image = self.__animacao[int(self.__index_animacao)]
        
    def update(self):
        self.animar()
        
    def draw(self, surface):
        surface.blit(self.__image, self.__rect)
        
    def hide(self):
        self.__rect.x = -10000
        self.__rect.y = -10000
        
    def reset(self):
        self.__rect = self.__image.get_rect(topleft = self.__posicao_inicial)
        
    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect
    