import pygame

class EstadoJogador:

    def __init__(self, velocidade: int):

        #movimento do jogador
        self.__direcao = pygame.math.Vector2(0,0)
        self.__velocidade = velocidade
        self.__gravidade = 0.8
        self.__altura_pulo = -16

        #informacoes do jogador
        self.__virado_para_direita = True
        self.__no_chao = False
        self.__no_teto = False
        self.__na_direita = False
        self.__na_esquerda = False
    
    def mover_para_esquerda(self):
        self.__direcao.x = -1
        self.__virado_para_direita = False
    
    def mover_para_direita(self):
        self.__direcao.x = 1
        self.__virado_para_direita = True
    
    def parar_movimento_horizontal(self):
        self.animar(False)
        self.__direcao.x = 0

    def pular(self):
        self.__direcao.y = self.__altura_pulo
    
    @property
    def direcao(self):
        return self.__direcao
    
    @property
    def velocidade(self):
        return self.__velocidade

    @property
    def gravidade(self):
        return self.__gravidade
    
    @property
    def no_chao(self):
        return self.__no_chao
    
    @no_chao.setter
    def no_chao(self, no_chao):
        self.__no_chao = no_chao
    
    @property
    def no_teto(self):
        return self.__no_teto
    
    @no_teto.setter
    def no_teto(self, no_teto):
        self.__no_teto = no_teto
    
    @property
    def na_direita(self):
        return self.__na_direita
    
    @na_direita.setter
    def na_direita(self, na_direita):
        self.__na_direita = na_direita

    @property
    def na_esquerda(self):
        return self.__na_esquerda

    @na_esquerda.setter
    def na_esquerda(self, na_esquerda):
        self.__na_esquerda = na_esquerda

    @property
    def virado_para_direita(self):
        return self.__virado_para_direita
    
    @virado_para_direita.setter
    def virado_para_direita(self, virado_para_direita):
        self.__virado_para_direita = virado_para_direita
