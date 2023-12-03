import pygame
from src.entities.animacao import Animacao

class Inimigo(pygame.sprite.Sprite, Animacao):
    def __init__(self, posicao, move_speed: int, path: str):
        super().__init__()
        Animacao.__init__(self, path) #chama o construtor de animacao, ja que tem herença multipla

        # animacao inimigo
        self.__index_animacao = 0
        self.__velocidade_animacao = 0.15
        self.__image = self.animacao[self.__index_animacao]
        self.__rect = self.__image.get_rect(topleft = posicao)
        
        # informacoes do inimigo
        self.__velocidade = move_speed
        self.__direcao = pygame.math.Vector2((self.__velocidade), 0)

    def andar(self):
        self.__rect.x += self.__direcao.x * self.__velocidade

    def animar(self):
        self.__index_animacao += self.__velocidade_animacao
        if self.__index_animacao > len(self.animacao):
            self.__index_animacao = 0
        
        imagem = self.animacao[int(self.__index_animacao)]
        if self.__direcao.x < 0:
            self.__image = imagem
        else:
            self.__image = pygame.transform.flip(imagem, True, False)

    def update(self):
        self.andar()
        self.animar()

    #GETTERS E SETTERS
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