import pygame
from src.ferramentas.suporte import importar_pasta

class Jogador(pygame.sprite.Sprite):
    def __init__(self, posicao: tuple, velocidade: int):
        super().__init__()
        self.importar_assets()
        self.__frame_index = 0
        self.__velocidade_animacao = 0.15
        self.__image =  self.__animacoes['idle'][self.__frame_index]
        self.__rect = self.image.get_rect(topleft = posicao)

        #movimento do jogador
        self.__direcao = pygame.math.Vector2(0,0)
        self.__velocidade = velocidade
        self.__gravidade = 0.8
        self.__altura_pulo = -15
        
        #informacoes do jogador
        self.__virado_para_direita = True
        self.__no_chao = False
        self.__no_teto = False
        self.__na_direita = False
        self.__na_esquerda = False

        self.__abrir_porta = False

    def importar_assets(self):
        path_personagem = 'Assets/character/'
        self.__animacoes = {'idle': [], 'run': [], 'jump': [], 'fall': []}

        for animacao in self.__animacoes.keys():
            full_path = path_personagem + animacao
            self.__animacoes[animacao] = importar_pasta(full_path)

    def get_comportamento(self):
        if self.__direcao.y < 0:
            return 'jump'
        elif self.__direcao.y > 0:
            return 'fall'
        elif self.__direcao.y == 0 and self.__direcao.x != 0:
            return 'run'
        else:
            return 'idle'

    def animar(self):
        animacao = self.__animacoes[self.get_comportamento()]

        self.__frame_index += self.__velocidade_animacao
        if self.__frame_index > len(animacao):
            self.__frame_index = 0
        
        imagem = animacao[int(self.__frame_index)]
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

    def andar(self):
        teclas = pygame.key.get_pressed() #mapeia as teclas
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]: #implementa a direção em que o jogador anda
            self.__direcao.x = 1
            self.__virado_para_direita = True
        elif teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.__direcao.x = -1
            self.__virado_para_direita = False
        else:
            self.__direcao.x = 0

        if (teclas[pygame.K_SPACE] or teclas[pygame.K_UP]) and self.no_chao:
            self.pular()

    def aplicar_gravidade(self):
        self.__direcao.y += self.__gravidade
        self.rect.y += self.__direcao.y

    def pular(self):
        self.__direcao.y = self.__altura_pulo


    def desbloquear_porta(self):
        self.__abrir_porta = True

    def update(self): #TEM que ter o nome de update, se não, nao vai funcionar em Fase.py por causa do pygame groups
        self.andar() 
        self.animar()
        
    @property
    def image(self):
        return self.__image
    
    @property
    def rect(self):
        return self.__rect

    @property
    def abrir_porta(self):
        return self.__abrir_porta

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