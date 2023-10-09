class Inimigo:
    def __init__(self, move_speed: int, som: str):
        self.__move_speed = move_speed
        self.__som = som
    
    @property
    def move_speed(self):
        return self.__move_speed
    
    @property
    def som(self):
        return self.__som
    
    def interacao_jogador(self):
        pass