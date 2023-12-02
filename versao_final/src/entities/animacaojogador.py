import pygame
from src.ferramentas.suporte import importar_pasta
from src.entities.estadojogador import EstadoJogador


class AnimacaoJogador:

    def __init__(self, posicao: tuple, estado_jogador: EstadoJogador):

        self.__estado_jogador = estado_jogador

        #animacao do jogador
        self.importar_assets()
        self.__index_animacao = 0
        self.__velocidade_animacao = 0.15
        self.__image =  self.__animacao[self.__index_animacao]
        self.__posicao_inicial = posicao
        self.__rect = self.image.get_rect(topleft = self.__posicao_inicial)
    
    #importa as imagens do jogador
    def importar_assets(self):
        path_personagem = 'assets/entities/jogador/skin01'
        self.__animacao = []
        self.__animacao = importar_pasta(path_personagem)

    def animar(self, andando = True):
        self.__index_animacao += self.__velocidade_animacao
        if self.__index_animacao > len(self.__animacao) or not andando:
            self.__index_animacao = 0
        
        imagem = self.__animacao[int(self.__index_animacao)]
        
        if self.estado_jogador.virado_para_direita:
            self.__image = imagem
        else:
            self.__image = pygame.transform.flip(imagem, True, False)

        if self.estado_jogador.no_chao and self.estado_jogador.na_direita:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.estado_jogador.no_chao and self.estado_jogador.na_esquerda:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.estado_jogador.no_chao:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.estado_jogador.no_teto and self.estado_jogador.na_direita:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.estado_jogador.no_teto and self.estado_jogador.na_esquerda:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.estado_jogador.no_teto:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
        
    def atualizar_posicao_horizontal(self): #atualiza a posicao horizontal do rect do jogador na tela
        self.rect.x += self.estado_jogador.direcao.x * self.estado_jogador.velocidade
    
    def atualizar_posicao_vertical_com_gravidade(self): #atualiza a posicao vertical do rect do jogador na tela, com a logica de gravidade
        self.estado_jogador.direcao.y += self.estado_jogador.gravidade
        self.rect.y += self.estado_jogador.direcao.y

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
