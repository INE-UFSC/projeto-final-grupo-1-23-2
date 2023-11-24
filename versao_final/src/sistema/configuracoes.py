class Configuracoes:
    def __init__(self):
        self.__tamanho_tile = 64
        self.__largura_tela = 20*self.__tamanho_tile
        self.__altura_tela = 12*self.__tamanho_tile
        self.__FPS = 60
        
    @property
    def tamanho_tile(self):
        return self.__tamanho_tile
    
    @property
    def largura_tela(self):
        return self.__largura_tela
    
    @property
    def altura_tela(self):
        return self.__altura_tela
    
    @property
    def FPS(self):
        return self.__FPS