import pygame
from src.fase.tilemap import TileMap, Background
from src.entities.jogador import Jogador
from src.itens.chave import Chave
from src.itens.porta import Porta
from src.entities.inimigo import Inimigo
from src.fase.colisao import Colisao
from src.sistema.hud import HUD
import random
import pytmx
import pygame

class Fase:
    def __init__(self, tiles, superficie, vida=5):
        self.__mapa = tiles
        self.__display_superficie = superficie
        self.__colisao = Colisao(self)
        self.__HUD = HUD(superficie, vida)
        self.fase_setup(tiles)

        self.__vidas = vida
        self.__passou_porta = False

    def render(self):
        for tile in self.__background + self.__tiles:
            tile.draw(self.__display_superficie)

        self.__HUD.render(self.__vidas, self.__jogador_sprite.abrir_porta)

    def update(self, event):

        for objeto in self.__tiles:
            if hasattr(objeto, 'update'):
                try:
                    objeto.update()
                except TypeError:
                    objeto.update(event)

        self.__colisao.update()

    def fase_setup(self, tmxdata):
        self.__colide = pygame.sprite.Group()
        self.__libera_chave = pygame.sprite.Group()
        self.__ncolide = pygame.sprite.Group()
        self.__espinhos = pygame.sprite.Group()

        self.__chave = pygame.sprite.GroupSingle()
        self.__porta = pygame.sprite.GroupSingle()

        self.__jogador = pygame.sprite.GroupSingle()  # so um jogador
        self.__inimigo = pygame.sprite.Group()

        self.__inimigo_colisores = pygame.sprite.Group()

        self.__tiles = []
        self.__background = []
        self.__bloco_chaves = []

        for layer in tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, surf in layer.tiles():
                    opacidade = int(255*layer.opacity)
                    surf.set_alpha(opacidade)
                    x *= self.__mapa.tilewidth
                    y *= self.__mapa.tilewidth


                    if layer.name[-7:] == "-colide":
                        self.__tiles.append(TileMap((x, y), surf, self.__colide))

                    elif layer.name[-8:] == "-ncolide":
                        self.__tiles.append(
                            TileMap((x, y), surf, self.__ncolide))

                    elif layer.name[-5:] == '-dano':
                        TileMap((x, y), surf, self.__espinhos)
                        
                    elif layer.name == 'chave':
                        self.__chave_sprite = Chave((x, y))
                        self.__chave.add(self.__chave_sprite)

                    elif layer.name == 'porta':
                        self.__porta_sprite = Porta((x, y))
                        self.__porta.add(self.__porta_sprite)
                        
                    elif layer.name == 'libera_chave':
                        self.__bloco_chaves.append(
                            TileMap((x, y), surf, self.__libera_chave))

                    elif layer.name[-7:] == '-player':
                        try:
                            tipo = layer.name[:-7]
                            path = 'assets/entities/jogador/' + tipo
                            self.__jogador_sprite = Jogador((x, y), 3, path)
                        except FileNotFoundError:
                            path = 'assets/entities/jogador/' + 'normal' 
                            self.__jogador_sprite = Jogador((x, y), 3, path)
                        self.__jogador.add(self.__jogador_sprite)

                    elif layer.name[-8:] == "-inimigo":
                        try:
                            tipo = layer.name[:-8]
                            path_inimigo = f'assets/entities/inimigo/' + tipo
                            self.__inimigo_sprite = Inimigo((x, y), 1, path_inimigo)
                        except FileNotFoundError:
                            path_inimigo = f'assets/entities/inimigo/' + 'cavaleiro'
                            self.__inimigo_sprite = Inimigo((x, y), 1, path_inimigo)
                        self.__inimigo.add(self.__inimigo_sprite)

                    elif layer.name == 'colisao_inimigo':
                        TileMap((x, y), surf, self.__inimigo_colisores)
                        
            elif isinstance(layer, pytmx.TiledImageLayer):
                if layer.name[-8:] == '-animado':
                    self.__background.append(
                        Background(layer.image, animado=True))
                else:
                    self.__background.append(Background(layer.image))

        self.__tiles += [self.__porta, self.__chave, self.__libera_chave,
                         self.__jogador, self.__inimigo, self.__espinhos]

    def reset(self):
        self.__jogador_sprite.reset()
        self.__chave_sprite.reset()
        [self.__libera_chave.add(tile) for tile in self.__bloco_chaves]

    @property
    def vidas(self):
        return self.__vidas

    @vidas.setter
    def vidas(self, numero):
        self.__vidas += numero

    @property
    def tiles(self):
        return self.__tiles

    @property
    def passou_porta(self):
        return self.__passou_porta

    @passou_porta.setter
    def passou_porta(self, passou_porta):
        self.__passou_porta = passou_porta

    @property
    def colide(self):
        return self.__colide
    
    @colide.setter
    def colide(self, colide):
        self.__colide = colide
    
    @property
    def libera_chave(self):
        return self.__libera_chave
    
    @libera_chave.setter
    def libera_chave(self, libera_chave):
        self.__libera_chave = libera_chave
    
    @property
    def ncolide(self):
        return self.__ncolide
    
    @ncolide.setter
    def ncolide(self, ncolide):
        self.__ncolide = ncolide

    @property
    def espinhos(self):
        return self.__espinhos
    
    @espinhos.setter
    def espinhos(self, espinhos):
        self.__espinhos = espinhos
    
    @property
    def chave(self):
        return self.__chave
    
    @chave.setter
    def chave(self, chave):
        self.__chave = chave
    
    @property
    def porta(self):
        return self.__porta
    
    @porta.setter
    def porta(self, porta):
        self.__porta = porta
    
    @property
    def inimigo(self):
        return self.__inimigo
    
    @inimigo.setter
    def inimigo(self, inimigo):
        self.__inimigo = inimigo
    
    @property
    def jogador(self):
        return self.__jogador
    
    @jogador.setter
    def jogador(self, jogador):
        self.__jogador = jogador
    
    @property
    def inimigo_colisores(self):
        return self.__inimigo_colisores
    
    @inimigo_colisores.setter
    def inimigo_colisores(self, inimigo_colisores):
        self.__inimigo_colisores = inimigo_colisores
    
    @property
    def jogador_sprite(self):
        return self.__jogador_sprite
    
    
    
    