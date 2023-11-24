import pygame
from src.fase.tilemap import TileMap, Background
from src.entities.jogador import Jogador
from src.itens.chave import Chave
from src.itens.porta import Porta
from src.entities.inimigo import Inimigo
from pytmx.util_pygame import load_pygame
import pytmx

class Fase:
    def __init__(self, tiles, superficie, vida=5):
        self.__tiles = tiles
        self.__display_superficie = superficie
        
        self.fase_setup(tiles)
        
        self.__vidas = vida
        self.__tem_inimigo = False
        self.passou_porta = False
    
    def render(self):
        self.inimigo_colisores.draw(self.__display_superficie)
        self.background.draw(self.__display_superficie)
        self.tiles.draw(self.__display_superficie)
        self.escada.draw(self.__display_superficie)
        self.ncolide.draw(self.__display_superficie)
        self.porta.draw(self.__display_superficie)
        self.chave.draw(self.__display_superficie)
        self.botao.draw(self.__display_superficie)
        self.jogador.draw(self.__display_superficie) 
        self.inimigo.draw(self.__display_superficie)
        
    def update(self, event):
        self.inimigo.update()
        self.inimigo_colisores.update()
        self.porta.update()
        self.chave.update()
        self.botao.update()
        self.jogador.update(event)
        
        
    def fase_setup(self, tmxdata):
        self.escada = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()
        self.background = pygame.sprite.Group()
        self.jogador = pygame.sprite.GroupSingle() #so um jogador
        self.chave = pygame.sprite.GroupSingle() #so uma chave
        self.inimigo = pygame.sprite.GroupSingle()
        self.porta = pygame.sprite.GroupSingle() #so uma porta
        self.botao = pygame.sprite.GroupSingle()
        self.ncolide = pygame.sprite.Group()
        self.inimigo_colisores = pygame.sprite.Group()

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

    def reset(self):
        nova_fase = Fase(self.__tiles, self.__display_superficie, self.__vidas)
        self.__dict__.update(nova_fase.__dict__)

    @property
    def vidas(self):
        return self.__vidas
    @vidas.setter
    def vidas(self, numero):
        self.__vidas += numero

    @property
    def tem_inimigo(self):
        return self.__tem_inimigo