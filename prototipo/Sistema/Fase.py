import pygame
from Sistema.TileMap import TileMap
from Sistema.presets import *
from Sistema.Jogador import Jogador
from itens.Chave import Chave
from itens.Porta import Porta

tela = pygame.display.set_mode((largura_tela, altura_tela))

class Fase:
    def __init__(self, informacao_fase, superficie):
        self.display_superficie = superficie
        self.fase_setup(informacao_fase)
        self.__num_fase = 1

    def run(self):
        #self.tiles.update()
        self.tiles.draw(self.display_superficie) #desenha a fase

        #porta
        self.porta.update()
        self.colisao_porta()
        #self.colisao_vertical_porta()
        self.porta.draw(self.display_superficie)

        #chave
        self.chave.update()
        self.colisao_chave()
        self.chave.draw(self.display_superficie)

        #jogador
        self.jogador.update() #atualiza a posição do jogador
        self.colisao_horizontal_tiles()
        self.colisao_vertical_tiles()
        self.jogador.draw(self.display_superficie) #desenha o jogador na sua posição



    def fase_setup(self,layout):
        self.tiles = pygame.sprite.Group()
        self.jogador = pygame.sprite.GroupSingle() #so um jogador
        self.chave = pygame.sprite.GroupSingle() #so uma chave
        self.porta = pygame.sprite.GroupSingle() #so uma porta

        for linha_i, linha in enumerate(layout):
            for coluna_i, elemento in enumerate(linha): #para manter controle de onde os 'X' estao de acordo com linha e coluna
                x = coluna_i*tamanho_tile
                y = linha_i*tamanho_tile

                if elemento == 'X':
                    tilemap = TileMap((x, y), tamanho_tile, 'green')   
                    self.tiles.add(tilemap)
                elif elemento == 'Z':
                    tilemap = TileMap((x, y), tamanho_tile, 'brown')
                    self.tiles.add(tilemap)
                elif elemento == 'P':
                    self.jogador_sprite = Jogador((x, y),3)
                    self.jogador.add(self.jogador_sprite) #self. para se quisermos trocar a skin/deletar o jogador quando morre
                elif elemento == 'C':
                    self.chave_sprite = Chave((x,y)) #self. pois precisa ser mantido para depois esse sprite ser deletado depois de colidir com o jogador
                    self.chave.add(self.chave_sprite)
                elif elemento == 'D':
                    self.porta_sprite = Porta((x,y))
                    self.porta.add(self.porta_sprite)

    def colisao_horizontal_tiles(self):
        jogador = self.jogador.sprite
        jogador.rect.x += jogador.direcao.x * jogador.velocidade #aplica o movimento horizontal

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(jogador.rect): #checa se o jogador esta colidindo com algum retangulo
                if jogador.direcao.x < 0: #se o jogador esta andando pra esquerda
                    jogador.rect.left = sprite.rect.right #colisao acontece na esquerda do jogador, entao ele fica na direita do tile q ele colidiu
                elif jogador.direcao.x > 0: #se o jogador esta andando pra direita
                    jogador.rect.right = sprite.rect.left

    def colisao_vertical_tiles(self):
        jogador = self.jogador.sprite
        jogador.aplicar_gravidade()
        teclas = pygame.key.get_pressed()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(jogador.rect): #checa se o jogador esta colidindo com algum retangulo
                if jogador.direcao.y > 0: 
                    jogador.rect.bottom = sprite.rect.top 
                    jogador.direcao.y = 0
                    if teclas[pygame.K_UP]: #implementa o pulo
                        jogador.pular() 
                        
                elif jogador.direcao.y < 0: 
                    jogador.rect.top = sprite.rect.bottom
                    jogador.direcao.y = 0


    def colisao_chave(self):
        jogador = self.jogador.sprite
        chave = self.chave.sprite

        for sprite in self.chave.sprites():
            if sprite.rect.colliderect(jogador.rect): #checa se o jogador esta colidindo com a chave
                self.chave.remove(self.chave_sprite)
                self.jogador_sprite.desbloquear_porta()

    def colisao_porta(self):
        jogador = self.jogador.sprite

        for sprite in self.porta.sprites():
            if sprite.rect.colliderect(jogador.rect): #checa se o jogador esta colidindo com algum retangulo
                if self.jogador_sprite.abrir_porta == True:
                    self.__num_fase +=1
                    self.update_mapa()

    def update_mapa(self):
        if self.__num_fase == 2:
            nova_fase = Fase(mapa2, tela)
            self.__dict__.update(nova_fase.__dict__)
