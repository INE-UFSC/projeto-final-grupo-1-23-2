from src.estados.menu import MenuState
from src.estados.jogo import Jogo
from src.estados.gameover import GameOverState

class StateMachine:
    def __init__(self, game):
        self.__estados = {
            'menu': MenuState(game),
            'gameover': GameOverState(game),
            'jogo': Jogo(game)
        }
        # self.gera_fases('fases/tmx', game)
        self.__estado_atual = 'menu'
        
    def muda_estado(self, estado):
        self.__estados[self.__estado_atual].exiting()
        self.__estado_atual = estado
        self.__estados[self.__estado_atual].entering()

    def run(self, event):
        self.__estados[self.__estado_atual].render()
        self.__estados[self.__estado_atual].update(event)
            