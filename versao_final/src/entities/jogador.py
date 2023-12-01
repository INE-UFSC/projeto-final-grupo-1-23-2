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
        self.posicao_inical = posicao
        self.__rect = self.image.get_rect(topleft = self.posicao_inical)

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

        self.__abrir_porta = False

        #temporário para desenhar retângulo de ataque
        self.__superficie = superficie

        #ataque
        self.__atacando = False
        self.__retangulo_ataque = pygame.Rect(
        self.__rect.centerx, self.__rect.y, 2 * self.rect.width, self.__rect.height)
        self.__duracao_ataque = 1
        self.__cronometro_ataque = 0
        self.__duracao_cooldown = 600
        self.__cooldown_state = False
        self.__cronometro_cooldown = 0
        
    def reset(self):
        novo_jogador = Jogador(self.posicao_inical, self.velocidade, self.__superficie)
        self.__dict__.update(novo_jogador.__dict__)

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
        
    def mover_para_esquerda(self):
        self.animar()
        self.__direcao.x = -1
        self.__virado_para_direita = False
    
    def mover_para_direita(self):
        self.animar()
        self.__direcao.x = 1
        self.__virado_para_direita = True
    
    def parar_movimento_horizontal(self):
        self.animar(False)
        self.__direcao.x = 0

    def aplicar_movimento_horizontal(self):
        self.__rect.x += self.__direcao.x * self.__velocidade #aplica o movimento horizontal

    def movimentar(self):  
        teclas = pygame.key.get_pressed() #mapeia as teclas

        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]: #movimento para a direita
            self.mover_para_direita()
         
        elif teclas[pygame.K_LEFT] or teclas[pygame.K_a]: #movimento para a esquerda
           self.mover_para_esquerda()

        else: #parado
           self.parar_movimento_horizontal()

        self.aplicar_movimento_horizontal() #aplica o movimento horizontal

        if (teclas[pygame.K_SPACE] or teclas[pygame.K_w] or teclas[pygame.K_UP]) and self.no_chao: #aplica o pulo
            self.pular()

    def atacar(self, event):
        if not self.__atacando and not self.__cooldown_state:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]: #essa linha detecta o clique esquerdo ÚNICO
                    self.__atacando = True
                    self.__cronometro_ataque = pygame.time.get_ticks() + self.__duracao_ataque
                    #determina para qual direção será desenhado o retangulo
                    if self.__virado_para_direita:
                        self.__retangulo_ataque = pygame.Rect(self.__rect.centerx, self.__rect.y, 1.5 * self.rect.width, self.__rect.height)
                    else:
                        self.__retangulo_ataque = pygame.Rect(
                            self.__rect.centerx - 66, self.__rect.y, 1.5 * self.rect.width, self.__rect.height)
                    pygame.draw.rect(self.__superficie, (0,255,0), self.__retangulo_ataque)

        #quando atacando for true e o tempo do jogo (get_ticks) ultrapassa o cronometro, atacando fica falso, e o tempo de cooldown é ativado, o que começa o cronometro do cooldown
        if self.__atacando and pygame.time.get_ticks() >= self.__cronometro_ataque: 
            self.__atacando = False
            self.__cooldown_state = True
            self.__cronometro_cooldown = pygame.time.get_ticks() + self.__duracao_cooldown

        #mesmo de antes aqui
        if self.__cooldown_state and pygame.time.get_ticks() >= self.__cronometro_cooldown:
            self.__cooldown_state = False


    def aplicar_gravidade(self):
        self.__direcao.y += self.__gravidade
        self.rect.y += self.__direcao.y

    def pular(self):
        self.__direcao.y = self.__altura_pulo
        
    def desbloquear_porta(self):
        self.__abrir_porta = True

    def update(self, event): 
        self.movimentar()
        self.atacar(event) 

    #getters e setters    
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
    def retangulo_ataque(self):
        return self.__retangulo_ataque
    
    @property
    def atacando(self):
        return self.__atacando