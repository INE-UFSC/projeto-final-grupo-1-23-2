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
        self.__vida_inicial = 3
        self.__vivo = True

        # dano e morte do inimigo
        self.__sendo_atacado = False
        self.__x_y_morte = (self.__rect.x, self.__rect.y)
        self.__cronometro_dano = 0
        self.__duracao_dano = 100

    def importar_assets(self):
        #animação de andar
        path_personagem = 'assets/entities/inimigo/skin01'
        self.__animacao = []
        self.__animacao = importar_pasta(path_personagem)

        #imagem de quando o inimigo toma dano
        self.__imagem_inimigo_dano = pygame.image.load('assets/entities/inimigo/skin01/inimigo_dano/feiticeiro_dano.png').convert_alpha()

        #animação da morte do inimigo (fumaça)
        path_morte = 'assets/entities/inimigo/fumaca'
        self.__animacao_morte = []
        self.__animacao_morte = importar_pasta(path_morte)

    def animar(self):
        if not self.__sendo_atacado:
            self.__index_animacao += self.__velocidade_animacao
            if self.__index_animacao > len(self.__animacao):
                self.__index_animacao = 0
            
            imagem = self.__animacao[int(self.__index_animacao)]
            if self.__direcao.x < 0:
                self.__image = imagem
            else:
                self.__image = pygame.transform.flip(imagem, True, False)
    
    def andar(self):
        if not self.__sendo_atacado:
            self.__rect.x += self.__direcao.x * self.__velocidade

    def dano_recebido(self):
        if self.__sendo_atacado:    
            self.__x_y_ataque = (self.__rect.x, self.__rect.y) #calcula posição que o inimigo está quando toma o hit (para ser usado quando o hit resulta em morte)
            self.__cronometro_dano = pygame.time.get_ticks() + self.__duracao_dano
            self.__vida_inicial -= 1

            
            # self.__velocidade_original = self.__velo
            # self.__velocidade = 0

            #self.__image = self.__imagem_inimigo_dano

        if self.__sendo_atacado and pygame.time.get_ticks() >= self.__cronometro_dano:
            self.__sendo_atacado = False

    def morte(self):
        self.__rect.x = 10000
        self.__rect.y = 10000
    
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

    @property
    def sendo_atacado(self):
        return self.__sendo_atacado
    
    @sendo_atacado.setter
    def sendo_atacado(self, sendo_atacado):
        self.__sendo_atacado = sendo_atacado
    
    
    
    