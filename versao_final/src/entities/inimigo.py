from typing import Any
import pygame
from src.ferramentas.suporte import importar_pasta


class Inimigo(pygame.sprite.Sprite):
    def __init__(self, posicao, move_speed: int):
        super().__init__()

        #animacao inimigo
        self.importar_assets()
        self.__index_animacao = 0
        self.__velocidade_animacao = 0.15
        self.__image = self.__animacao[self.__index_animacao]
        self.__rect = self.__image.get_rect(midbottom = posicao)
        
        #informacoes do inimigo
        self.__velocidade = move_speed
        self.__direcao = pygame.math.Vector2((self.__velocidade), 0)


    def importar_assets(self):
        path_personagem = 'Assets/inimigo_fantasma/'
        self.__animacao = []
        self.__animacao = importar_pasta(path_personagem)

    def animar(self):
        self.__index_animacao += self.__velocidade_animacao
        if self.__index_animacao > len(self.__animacao):
            self.__index_animacao = 0
        
        imagem = self.__animacao[int(self.__index_animacao)]
        if self.__direcao.x < 0:
            self.__image = imagem
        else:
            self.__image = pygame.transform.flip(imagem, True, False)
    
    def andar(self):
        self.__rect.x += self.__direcao.x * self.__velocidade
    
    def update(self):
        self.andar()
        self.animar()

    @property
    def velocidade(self):
        return self.__velocidade
    
    @property
    def direcao(self):
        return self.__direcao
    
    @property
    def rect(self):
        return self.__rect
    
    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self, nova_imagem):
        self.__image = nova_imagem

    