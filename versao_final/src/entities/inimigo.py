import pygame
from src.ferramentas.suporte import importar_pasta


class Inimigo(pygame.sprite.Sprite):
    def __init__(self, posicao, move_speed: int):
        super().__init__()

        # animacao inimigo
        self.importar_assets()
        self.__index_animacao = 0
        self.__velocidade_animacao = 0.15
        self.__image = self.__animacao[self.__index_animacao]
        self.__rect = self.__image.get_rect(topleft = posicao)
        
        # informacoes do inimigo
        self.__velocidade = move_speed
        self.__direcao = pygame.math.Vector2((self.__velocidade), 0)

        # vida inicial do inimigo
        self.__vida_inicial = 3

        self.__vivo = True
        self.__x_y_morte = (self.__rect.x, self.__rect.y)

    def importar_assets(self):
        path_personagem = 'assets/entities/inimigo/skin01'
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

    def dano_recebido(self):
        self.__x_y_ataque = (self.__rect.x, self.__rect.y) #calcula posição que o inimigo está quando toma o hit (para ser usado quando o hit resulta em morte)
        self.__vida_inicial -= 1
        print(self.__vida_inicial)
        print("hit")

    def morte(self):
        self.__rect.x = 10000
        self.__rect.y = 10000
        
        print(self.__x_y_ataque[0])
    
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

    @property
    def vida_inicial(self):
        return self.__vida_inicial
    
    @vida_inicial.setter
    def vida_inicial(self, vida_atual):
        self.__vida_inicial = vida_atual

    @property
    def vivo(self):
        return self.__vivo
    
    @vivo.setter
    def vivo(self, vivo):
        self.__vivo = vivo

    @property
    def rect_final(self):
        return self.__rect
    
    @rect_final.setter
    def rect_final(self, rect):
        self.__rect_final = rect
    
    @property
    def x_y_morte(self):
        return self.__x_y_morte
    
    @x_y_morte.setter
    def x_y_morte(self, x_y_morte):
        self.__x_y_morte = x_y_morte
    
    