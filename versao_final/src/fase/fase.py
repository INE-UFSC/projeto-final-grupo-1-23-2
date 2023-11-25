import pygame
from src.fase.tilemap import TileMap, Background
from src.entities.jogador import Jogador
from src.itens.chave import Chave
from src.itens.porta import Porta
from src.entities.inimigo import Inimigo
from src.fase.colisao import Colisao
import pytmx

class Fase:
    def __init__(self, tiles, superficie, vida=5):
        self.__mapa = tiles
        self.__display_superficie = superficie
        self.__colisao = Colisao(self)
        
        self.fase_setup(tiles)
        
        self.__vidas = vida
        self.__passou_porta = False
    
    def render(self):
        for tile in self.__background + self.__tiles:
            tile.draw(self.__display_superficie)
        
    def update(self, event):
        for objeto in self.__tiles:
            if hasattr(objeto, 'update'):
                try:
                    objeto.update()
                except TypeError:
                    objeto.update(event) 
                    
        self.__colisao.update()
        
    def fase_setup(self, tmxdata):
        self.escada = pygame.sprite.Group()
        self.colide = pygame.sprite.Group()
        self.ncolide = pygame.sprite.Group()
        
        self.chave = pygame.sprite.GroupSingle()
        self.porta = pygame.sprite.GroupSingle() 
        
        self.jogador = pygame.sprite.GroupSingle() #so um jogador
        self.inimigo = pygame.sprite.GroupSingle()
        
        self.inimigo_colisores = pygame.sprite.Group()
        
        self.__tiles = []
        self.__background = []

        for layer in tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, surf in layer.tiles():
                    x *= self.__mapa.tilewidth
                    y *= self.__mapa.tilewidth
                    
                    if layer.name == 'escada':
                        self.__tiles.append(TileMap((x,y), surf, self.escada))
                    
                    elif layer.name in ['terreno', 'ponte']:
                        self.__tiles.append(TileMap((x, y), surf, self.colide))
                        
                    elif layer.name in ['arvores', 'dentro', 'decoracao']:
                        self.__tiles.append(TileMap((x, y), surf, self.ncolide))
                        
                    elif layer.name == 'chave':
                        self.chave_sprite = Chave((x,y))
                        self.chave.add(self.chave_sprite)
                    
                    elif layer.name == 'porta':
                        self.porta_sprite = Porta((x,y))
                        self.porta.add(self.porta_sprite)
                        
                    elif layer.name == 'player':
                        self.jogador_sprite = Jogador((x, y),3, self.__display_superficie)
                        self.jogador.add(self.jogador_sprite)
                        
                    elif layer.name == 'inimigo':
                        self.inimigo_sprite = Inimigo((x, y), 1)
                        self.inimigo.add(self.inimigo_sprite) 
                        self.__tiles.append(self.inimigo)
                        
                    elif layer.name == 'colisao_inimigo':
                        TileMap((x,y), surf, self.inimigo_colisores)
                    
            elif isinstance(layer, pytmx.TiledImageLayer):
                if layer.name == 'nuvem':
                    self.__background.append(Background(layer.image, animado=True))
                else:
                    self.__background.append(Background(layer.image))
                
        self.__tiles += [self.porta, self.chave, self.jogador]

    def reset(self):
        nova_fase = Fase(self.__mapa, self.__display_superficie, self.__vidas)
        self.__dict__.update(nova_fase.__dict__)

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
    
    