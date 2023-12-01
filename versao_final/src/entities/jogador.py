import pygame
from src.ferramentas.suporte import importar_pasta
from src.entities.estadojogador import EstadoJogador
from src.entities.animacaojogador import AnimacaoJogador

class Jogador(pygame.sprite.Sprite):
    def __init__(self, posicao: tuple, velocidade: int):
        super().__init__()

        self.__estado_jogador = EstadoJogador(velocidade)
        self.__animacao_jogador = AnimacaoJogador(posicao, self.__estado_jogador)

        self.__abrir_porta = False
        
    def reset(self):
        novo_jogador = Jogador(self.posicao_inical, self.velocidade)
        self.__dict__.update(novo_jogador.__dict__)

    def movimentar(self):  
        teclas = pygame.key.get_pressed() #mapeia as teclas

        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]: #movimento para a direita
            self.animacao_jogador.animar()
            self.mover_para_direita()
         
        elif teclas[pygame.K_LEFT] or teclas[pygame.K_a]: #movimento para a esquerda
            self.animacao_jogador.animar()
            self.mover_para_esquerda()

        else: #parado
            self.animacao_jogador.animar(False)
            self.parar_movimento_horizontal()

        self.animacao_jogador.atualizar_posicao_horizontal() #atualiza a posicao do rect do jogador

        if (teclas[pygame.K_SPACE] or teclas[pygame.K_w] or teclas[pygame.K_UP]) and self.no_chao: #aplica o pulo
            self.pular()
    
    def aplicar_gravidade(self):
        self.estado_jogador.direcao.y += self.estado_jogador.gravidade
        self.animacao_jogador.rect.y += self.estado_jogador.direcao.y

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

    