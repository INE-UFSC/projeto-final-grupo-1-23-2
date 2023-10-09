class Botao_Jogo:
    def __init__(self, sprite_inicial: str, sprite_apertado: str):
        self.__sprite_inicial = sprite_inicial
        self.__sprite_apertado = sprite_apertado

    @property
    def sprite_inicial(self):
        return self.__sprite_inicial

    @property
    def sprite_apertado(self):
        return self.__sprite_apertado


    def interacao_jogador(self):
        pass