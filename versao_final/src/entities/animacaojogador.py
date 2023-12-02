import pygame
from src.ferramentas.suporte import importar_pasta
from src.entities.estadojogador import EstadoJogador
from src.entities.animacao import Animacao


class AnimacaoJogador(Animacao):

    def __init__(self, posicao: tuple, estado_jogador: EstadoJogador, path: str):
        super().__init__(path) #faz o import da pasta contendo os assets do jogador

        self.__estado_jogador = estado_jogador

        #animacao do jogador
        self.__path = path
        self.__index_animacao = 0
        self.__velocidade_animacao = 0.15
        self.__image =  self.animacao[self.__index_animacao]
        self.__posicao_inicial = posicao
        self.__rect = self.image.get_rect(topleft = self.__posicao_inicial)

    def animar(self, andando = True):
        self.__index_animacao += self.__velocidade_animacao
        if self.__index_animacao > len(self.animacao) or not andando:
            self.__index_animacao = 0
        
        imagem = self.animacao[int(self.__index_animacao)]
        
        if self.estado_jogador.virado_para_direita:
            self.__image = imagem
        else:
            self.__image = pygame.transform.flip(imagem, True, False)

        
    def atualizar_posicao_horizontal(self): #atualiza a posicao horizontal do rect do jogador na tela
        self.rect.x += self.estado_jogador.direcao.x * self.estado_jogador.velocidade
    
    def atualizar_posicao_vertical_com_gravidade(self): #atualiza a posicao vertical do rect do jogador na tela, com a logica de gravidade
        self.estado_jogador.direcao.y += self.estado_jogador.gravidade
        self.rect.y += self.estado_jogador.direcao.y

    @property
    def path(self):
        return self.__path

    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self, novo_rect):
        self.__rect = novo_rect

    @property
    def image(self):
        return self.__image
    
    @property
    def posicao_inicial(self):
        return self.__posicao_inicial
    
    @property
    def estado_jogador(self):
        return self.__estado_jogador
