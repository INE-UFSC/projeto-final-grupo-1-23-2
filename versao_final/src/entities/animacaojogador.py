import pygame
from src.ferramentas.suporte import importar_pasta


class AnimacaoJogador:

    def __init__(self, posicao: tuple):

        #animacao do jogador
        self.importar_assets()
        self.__index_animacao = 0
        self.__velocidade_animacao = 0.15
        self.__image =  self.__animacao[self.__index_animacao]
        self.posicao_inical = posicao
        self.__rect = self.image.get_rect(topleft = self.posicao_inical)
    
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
        
        if self.__virado_para_direita:
            self.__image = imagem
        else:
            self.__image = pygame.transform.flip(imagem, True, False)

        if self.no_chao and self.na_direita:
            self.__rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.no_chao and self.na_esquerda:
            self.__rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.no_chao:
            self.__rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.no_teto and self.na_direita:
            self.__rect = self.image.get_rect(topright = self.rect.topright)
        elif self.no_teto and self.na_esquerda:
            self.__rect = self.image.get_rect(toplet = self.rect.topleft)
        elif self.no_teto:
            self.__rect = self.image.get_rect(midtop = self.rect.midtop)

