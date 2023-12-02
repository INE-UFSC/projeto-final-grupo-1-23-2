import pygame
from src.entities.estadojogador import EstadoJogador
from src.entities.animacaojogador import AnimacaoJogador

class Jogador(pygame.sprite.Sprite):
    def __init__(self, posicao: tuple, velocidade: int):
        super().__init__()

        self.__estado_jogador = EstadoJogador(velocidade)
        self.__animacao_jogador = AnimacaoJogador(posicao, self.__estado_jogador)

        self.__image = self.__animacao_jogador.image
        self.__rect = self.animacao_jogador.rect


        self.__abrir_porta = False
        
    def reset(self):
        novo_jogador = Jogador(self.animacao_jogador.posicao_inicial, self.estado_jogador.velocidade)
        self.__dict__.update(novo_jogador.__dict__)

    def movimentar(self):  
        teclas = pygame.key.get_pressed() #mapeia as teclas

        self.__image = self.__animacao_jogador.image
        self.__rect = self.animacao_jogador.rect

        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]: #movimento para a direita
            self.animacao_jogador.animar()
            self.estado_jogador.mover_para_direita()
         
        elif teclas[pygame.K_LEFT] or teclas[pygame.K_a]: #movimento para a esquerda
            self.animacao_jogador.animar()
            self.estado_jogador.mover_para_esquerda()

        else: #parado
            self.animacao_jogador.animar(False)
            self.estado_jogador.parar_movimento_horizontal()

        self.animacao_jogador.atualizar_posicao_horizontal() #atualiza a posicao do rect do jogador

        if (teclas[pygame.K_SPACE] or teclas[pygame.K_w] or teclas[pygame.K_UP]) and self.estado_jogador.no_chao: #aplica o pulo
            self.estado_jogador.pular()

    def desbloquear_porta(self):
        self.__abrir_porta = True

    def update(self): 
        self.movimentar()

    #getters e setters    
    @property
    def abrir_porta(self):
        return self.__abrir_porta
    
    @property
    def estado_jogador(self):
        return self.__estado_jogador
    
    @property
    def animacao_jogador(self):
        return self.__animacao_jogador

    @property
    def image(self):
        return self.__image
    
    @property
    def rect(self):
        return self.__rect
    