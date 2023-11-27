from src.estados.menu_inicial import MenuInicialState
from src.estados.menu_pause import MenuPauseState
from src.estados.jogo import Jogo
from src.estados.gameover import GameOverState

class StateMachine:
    def __init__(self, game):
        self.__estados = {
            'menu inicial': MenuInicialState(game),
            'gameover': GameOverState(game),
            'jogo': Jogo(game),
            'menu pause': MenuPauseState(game)
        }
        # self.gera_fases('fases/tmx', game)
        self.__estado_atual = 'menu inicial'
        
    def muda_estado(self, estado):
        self.__estados[self.__estado_atual].exiting()
        self.__estado_atual = estado
        self.__estados[self.__estado_atual].entering()

    def run(self, event):
        self.__estados[self.__estado_atual].render()
        self.__estados[self.__estado_atual].update(event)
        
    def reset(self, estado):
        self.__estados[estado].reset()
            