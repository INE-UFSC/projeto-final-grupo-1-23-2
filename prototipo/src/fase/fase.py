import pygame
from src.fase.tilemap import TileMap
from src.entities.jogador import Jogador
from src.itens.chave import Chave
from src.itens.porta import Porta
from src.itens.botao_jogo import Botao_Jogo
from src.fase.mapas import Mapa

tela = pygame.display.set_mode((Mapa().altura_tela, Mapa().largura_tela))

class Fase:
    def __init__(self, informacao_fase, superficie, num_fase):
        self.__display_superficie = superficie
        self.__tem_botao = False
        self.fase_setup(informacao_fase)
        self.__num_fase = num_fase
        self.__fase_atual = None
    
    @property
    def display_superficie(self):
        return self.__display_superficie
    
    @property
    def tem_botao(self):
        return self.__tem_botao
    
    @tem_botao.setter
    def tem_botao(self,novo_valor):
        self.__tem_botao = novo_valor
    
    @property
    def num_fase(self):
        return self.__fase_atual
    
    @property
    def fase_atual(self):
        return self.__fase.atual
    

    def run(self):
        #self.tiles.update()
        self.display_superficie.fill('Blue') #preenche a tela com a cor azul
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

        #botao
        self.botao.update()
        self.botao.draw(self.display_superficie)
        self.barreira.update()
        self.colisao_botao()
        self.barreira.draw(self.display_superficie)


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
        self.botao = pygame.sprite.GroupSingle()
        self.barreira = pygame.sprite.Group()

        for linha_i, linha in enumerate(layout):
            for coluna_i, elemento in enumerate(linha): #para manter controle de onde os 'X' estao de acordo com linha e coluna
                x = coluna_i*Mapa().tamanho_tile
                y = linha_i*Mapa().tamanho_tile

                if elemento == 'X':
                    tilemap = TileMap((x, y), Mapa().tamanho_tile, 'green')   
                    self.tiles.add(tilemap)
                elif elemento == 'Z':
                    tilemap = TileMap((x, y), Mapa().tamanho_tile, 'brown')
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
                elif elemento == 'B':
                    self.tem_botao = True
                    self.botao_sprite = Botao_Jogo((x,y))
                    self.botao.add(self.botao_sprite)
                elif elemento == 'b':
                    
                    tilemap = TileMap((x, y), Mapa().tamanho_tile, 'Gray')
                    self.barreira.add(tilemap)

    def colisao_horizontal_tiles(self):
        jogador = self.jogador.sprite
        jogador.rect.x += jogador.direcao.x * jogador.velocidade #aplica o movimento horizontal

        for sprite in self.tiles.sprites() + self.barreira.sprites():
            if sprite.rect.colliderect(jogador.rect): #checa se o jogador esta colidindo com algum retangulo
                if jogador.direcao.x < 0: #se o jogador esta andando pra esquerda
                    jogador.rect.left = sprite.rect.right #colisao acontece na esquerda do jogador, entao ele fica na direita do tile q ele colidiu
                elif jogador.direcao.x > 0: #se o jogador esta andando pra direita
                    jogador.rect.right = sprite.rect.left
            if jogador.rect.left <= 0:
                jogador.rect.left = 0
            if jogador.rect.right >= Mapa().largura_tela:
                jogador.rect.right = Mapa().largura_tela
    

    def colisao_vertical_tiles(self):
        jogador = self.jogador.sprite
        jogador.aplicar_gravidade()
        teclas = pygame.key.get_pressed()
        
        for sprite in self.tiles.sprites() + self.barreira.sprites():
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

        if self.chave_sprite.rect.colliderect(jogador.rect):
            self.chave.remove(self.chave_sprite)
            self.jogador_sprite.desbloquear_porta()
        #for sprite in self.chave.sprites():
         #   if sprite.rect.colliderect(jogador.rect): #checa se o jogador esta colidindo com a chave
          #      self.chave.remove(self.chave_sprite)
          #      self.jogador_sprite.desbloquear_porta()

    def colisao_porta(self):
        jogador = self.jogador.sprite

        if self.porta_sprite.rect.colliderect(jogador.rect): #checa se o jogador esta colidindo com algum retangulo
            if self.jogador_sprite.abrir_porta == True:
                self.__num_fase +=1
                self.update_mapa()

    def update_mapa(self):
        for num_mapa in range(len(Mapa().mapa)):
            if num_mapa == self.__num_fase:
                nova_fase = Fase(Mapa().mapa[num_mapa], tela, self.__num_fase)
                self.__dict__.update(nova_fase.__dict__)

    def colisao_botao(self):
        jogador = self.jogador.sprite

        if self.tem_botao == True:
            if self.botao_sprite.rect.colliderect(jogador.rect):
                self.botao.empty()
                self.barreira.empty()