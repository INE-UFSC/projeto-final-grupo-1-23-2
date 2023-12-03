import pygame
from src.entities.animacao import Animacao

class Chave(pygame.sprite.Sprite, Animacao):
    def __init__(self, posicao, path):
        super().__init__()
        Animacao.__init__(self, path)
        
        #animacao inimigo
        self.__posicao_inicial = posicao
        self.__index_animacao = 0
        self.__velocidade_animacao = 0.1
        self.__image = self.animacao[self.__index_animacao]
        self.__rect = self.__image.get_rect(topleft = posicao)
    

    def animar(self):
        self.__index_animacao += self.__velocidade_animacao
        if self.__index_animacao > len(self.animacao):
            self.__index_animacao = 0
        
        self.__image = self.animacao[int(self.__index_animacao)]
        
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
    