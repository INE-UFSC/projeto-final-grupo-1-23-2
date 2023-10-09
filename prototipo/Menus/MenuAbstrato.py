from abc import ABC, abstractmethod

class MenuAbstrato(ABC):
    def __init__(self, screen, background: str, musica: str, botoes: list):
        self.__screen = screen
        self.__background = background
        self.__musica = musica
        self.__botoes = botoes

    @property
    def screen(self):
        return self.__screen
    
    @property
    def background(self):
        return self.__background
    
    @property
    def musica(self):
        return self.__musica
    
    @property
    def botoes(self):
        return self.__botoes

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def tocar_musica(self):
        pass
        