from src.estados.menu_inicial import MenuInicialState
from src.estados.menu_pause import MenuPauseState
from src.estados.jogo import Jogo
from src.estados.gameover import GameOverState
from src.estados.tutorial import TutorialState
from src.estados.menu_vitoria import MenuVitoriaState

class StateMachine:
    def __init__(self, game):
        self.__estados = {
            'menu inicial': MenuInicialState(game),
            'gameover': GameOverState(game),
            'jogo': Jogo(game),
            'menu pause': MenuPauseState(game),
            'tutorial': TutorialState(game),
            'menu vitoria': MenuVitoriaState(game)
        }
        self.__estado_atual = 'menu inicial'
        self.__estado_anterior = 'menu inicial'
        
    def muda_estado(self, estado):
        self.__estados[self.__estado_atual].exiting()
        self.__estado_anterior = self.__estado_atual
        self.__estado_atual = estado
        self.__estados[self.__estado_atual].entering()

    def run(self, event):
        self.__estados[self.__estado_atual].render()
        self.__estados[self.__estado_atual].update(event)
        
    def reset(self, estado):
        self.__estados[estado].reset()
            
    @property
    def estado_anterior(self):
        return self.__estado_anterior