import pygame
from src.ferramentas.suporte import importar_pasta

class Jogador(pygame.sprite.Sprite):
    def __init__(self, posicao: tuple, velocidade: int, superficie):
        super().__init__()

        #animacao do jogador
        self.importar_assets()
        self.__index_animacao = 0
        self.__velocidade_animacao = 0.15
        self.__image =  self.__animacao[self.__index_animacao]
        self.__rect = self.image.get_rect(topleft = posicao)

        #movimento do jogador
        self.__direcao = pygame.math.Vector2(0,0)
        self.__velocidade = velocidade
        self.__gravidade = 0.8
        self.__altura_pulo = -16
        self.__escalar = False
        #informacoes do jogador
        self.__virado_para_direita = True
        self.__no_chao = False
        self.__no_teto = False
        self.__na_direita = False
        self.__na_esquerda = False

        self.__abrir_porta = False

        self.__superficie = superficie

    #importa as imagens do jogador
    def importar_assets(self):
        path_personagem = 'Assets/jogador/'
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

    def andar(self):
        teclas = pygame.key.get_pressed() #mapeia as teclas
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]: #implementa a direção em que o jogador anda
            self.animar()
            self.__direcao.x = 1
            self.__virado_para_direita = True
        elif teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.animar()
            self.__direcao.x = -1
            self.__virado_para_direita = False
        else:
            self.animar(False)
            self.__direcao.x = 0

        self.__rect.x += self.__direcao.x * self.__velocidade #aplica o movimento horizontal

        if (teclas[pygame.K_SPACE] or teclas[pygame.K_w]) and self.no_chao:
            self.pular()


        if teclas[pygame.K_UP]:
            self.escalandoUP()
        if teclas[pygame.K_DOWN]:
            self.escalandoDOWN()


    def atacar(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]: #essa linha detecta o clique esquerdo ÚNICO
                self.ataque()

    def ataque(self):
        retangulo_de_ataque = pygame.Rect(self.__rect.centerx,
                                          self.__rect.y,
                                          2 * self.rect.width,
                                          self.__rect.height
                                          )
        pygame.draw.rect(self.__superficie, (0,255,0), retangulo_de_ataque)
    def aplicar_gravidade(self):
        self.__direcao.y += self.__gravidade
        self.rect.y += self.__direcao.y

    def pular(self):
        self.__direcao.y = self.__altura_pulo
    
    def escalandoUP(self):
        if self.__escalar == True:
            self.rect.y += -5
    
    def escalandoDOWN(self):
        if self.no_chao == False:
            self.rect.y -= -5
        
    def desbloquear_porta(self):
        self.__abrir_porta = True

    def update(self, event): 
        self.andar()
        self.atacar(event) 
        
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

    @property
    def escalar(self):
        return self.__escalar
    
    @escalar.setter
    def escalar(self, novo_valor):
        self.__escalar = novo_valor