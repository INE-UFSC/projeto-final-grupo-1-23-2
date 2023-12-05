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

        self.__HUD.render(self.__vidas, self.jogador_sprite.abrir_porta)

    def update(self, event):

        for objeto in self.__tiles:
            if hasattr(objeto, 'update'):
                try:
                    objeto.update()
                except TypeError:
                    objeto.update(event)

        self.__colisao.update()

    def fase_setup(self, tmxdata):
        self.colide = pygame.sprite.Group()
        self.libera_chave = pygame.sprite.Group()
        self.ncolide = pygame.sprite.Group()
        self.espinhos = pygame.sprite.Group()

        self.chave = pygame.sprite.GroupSingle()
        self.porta = pygame.sprite.GroupSingle()

        self.jogador = pygame.sprite.GroupSingle()  # so um jogador
        self.inimigo = pygame.sprite.Group()

        self.inimigo_colisores = pygame.sprite.Group()

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
                        self.__tiles.append(TileMap((x, y), surf, self.colide))

                    elif layer.name[-8:] == "-ncolide":
                        self.__tiles.append(
                            TileMap((x, y), surf, self.ncolide))

                    elif layer.name[-5:] == '-dano':
                        TileMap((x, y), surf, self.espinhos)
                        
                    elif layer.name == 'chave':
                        self.chave_sprite = Chave((x, y))
                        self.chave.add(self.chave_sprite)

                    elif layer.name == 'porta':
                        self.porta_sprite = Porta((x, y))
                        self.porta.add(self.porta_sprite)
                        
                    elif layer.name == 'libera_chave':
                        self.__bloco_chaves.append(
                            TileMap((x, y), surf, self.libera_chave))

                    elif layer.name[-7:] == '-player':
                        try:
                            tipo = layer.name[:-7]
                            path = 'assets/entities/jogador/' + tipo
                            self.jogador_sprite = Jogador((x, y), 3, path)
                        except FileNotFoundError:
                            path = 'assets/entities/jogador/' + 'normal' 
                            self.jogador_sprite = Jogador((x, y), 3, path)
                        self.jogador.add(self.jogador_sprite)

                    elif layer.name[-8:] == "-inimigo":
                        try:
                            tipo = layer.name[:-8]
                            path_inimigo = f'assets/entities/inimigo/' + tipo
                            self.inimigo_sprite = Inimigo((x, y), 1, path_inimigo)
                        except FileNotFoundError:
                            path_inimigo = f'assets/entities/inimigo/' + 'cavaleiro'
                            self.inimigo_sprite = Inimigo((x, y), 1, path_inimigo)
                        self.inimigo.add(self.inimigo_sprite)

                    elif layer.name == 'colisao_inimigo':
                        TileMap((x, y), surf, self.inimigo_colisores)
                        
            elif isinstance(layer, pytmx.TiledImageLayer):
                if layer.name[-8:] == '-animado':
                    self.__background.append(
                        Background(layer.image, animado=True))
                else:
                    self.__background.append(Background(layer.image))

        self.__tiles += [self.porta, self.chave, self.libera_chave,
                         self.jogador, self.inimigo, self.espinhos]

    def reset(self):
        self.jogador_sprite.reset()
        self.chave_sprite.reset()
        [self.libera_chave.add(tile) for tile in self.__bloco_chaves]

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