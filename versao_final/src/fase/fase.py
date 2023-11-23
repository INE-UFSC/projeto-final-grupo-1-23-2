import pygame
from src.fase.tilemap import TileMap, Background
from src.entities.jogador import Jogador
from src.itens.chave import Chave
from src.itens.porta import Porta
from src.itens.botao_jogo import Botao_Jogo
from src.fase.mapas import Mapa
from src.entities.inimigo import Inimigo
from pytmx.util_pygame import load_pygame
import pytmx

class Fase:
    def __init__(self, informacao_fase, sistema, num_fase, vida):
        self.__display_superficie = sistema.screen
        self.__sistema = sistema
        self.__tem_botao = False
        self.__tem_inimigo = False
        self.fase_setup(informacao_fase)
        self.__num_fase = num_fase
        self.__vidas = vida
    
    def run(self):
        #colisores do inimigo
        self.inimigo_colisores.update()
        self.inimigo_colisores.draw(self.display_superficie)

        #desenha a fase
        self.background.draw(self.display_superficie)
        self.tiles.draw(self.display_superficie)
        self.ncolide.draw(self.display_superficie)
 
        #porta
        self.porta.update()
        self.porta.draw(self.display_superficie)

        #chave
        self.chave.update()
        self.chave.draw(self.display_superficie)

        #botao
        self.botao.update()
        self.botao.draw(self.display_superficie)
        self.escada.draw(self.display_superficie)

        #jogador
        self.jogador.update() #atualiza a posição do jogador
        self.jogador.draw(self.display_superficie) #desenha o jogador na sua posição

        #inimigo
        self.inimigo.update()
        self.inimigo.draw(self.display_superficie)
        self.escada.update()
        
    def fase_setup(self,layout):
        tmxdata = load_pygame('fases/fase0/setup/fase0.tmx')

        self.escada = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()
        self.background = pygame.sprite.Group()
        self.jogador = pygame.sprite.GroupSingle() #so um jogador
        self.chave = pygame.sprite.GroupSingle() #so uma chave
        self.inimigo = pygame.sprite.GroupSingle()
        self.porta = pygame.sprite.GroupSingle() #so uma porta
        self.botao = pygame.sprite.GroupSingle()
        #self.barreira = pygame.sprite.Group()
        self.ncolide = pygame.sprite.Group()
        self.inimigo_colisores= pygame.sprite.Group()

        for layer in tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, surf in layer.tiles():
                    
                    if layer.name == 'escada':
                        TileMap((x,y), surf, self.escada)
                    
                    elif layer.name in ['terreno', 'ponte']:
                        TileMap((x, y), surf, self.tiles)
                        
                    elif layer.name in ['arvores', 'dentro', 'decoracao', 'escada']:
                        TileMap((x, y), surf, self.ncolide)
                        
                    elif layer.name == 'chave':
                        self.chave_sprite = Chave((64*x,64*y))
                        self.chave.add(self.chave_sprite)
                    
                    elif layer.name == 'porta':
                        self.porta_sprite = Porta((64*x,64*y))
                        self.porta.add(self.porta_sprite)
                        
                    elif layer.name == 'player':
                        self.jogador_sprite = Jogador((64*x, 64*y),3, self.__display_superficie)
                        self.jogador.add(self.jogador_sprite)
                    elif layer.name == 'inimigo':
                        self.__tem_inimigo = True
                        self.inimigo_sprite = Inimigo((64*x, 64*y), 1)
                        self.inimigo.add(self.inimigo_sprite)    
                    elif layer.name == 'colisao_inimigo':
                        TileMap((x,y), surf, self.inimigo_colisores)
                    
            else:
                Background(layer.image, self.background)

    def gameover(self):
        nova_fase = Fase(Mapa().mapa[0], self.__sistema, 0, 5)
        self.__dict__.update(nova_fase.__dict__)
        self.__sistema.define_estado('gameover')

    def verificao_fase_atual(self): #verifica se o jogo terminou
        if self.__num_fase == len(Mapa().mapa): # verificacao de gameover
            self.gameover()
        else:
            self.update_mapa(self.__vidas)

    def update_mapa(self, vidas):
        for num_mapa in range(len(Mapa().mapa)):
            if num_mapa == self.__num_fase:
                nova_fase = Fase(Mapa().mapa[num_mapa], self.__sistema, self.__num_fase, vidas)
                self.__dict__.update(nova_fase.__dict__)

    def update(self):
        self.run()

    @property
    def vidas(self):
        return self.__vidas
    @vidas.setter
    def vidas(self, numero):
        self.__vidas += numero
    
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
        return self.__num_fase
    
    @num_fase.setter
    def num_fase(self, novo_num_fase):
        self.__num_fase = novo_num_fase

    @property
    def tem_inimigo(self):
        return self.__tem_inimigo