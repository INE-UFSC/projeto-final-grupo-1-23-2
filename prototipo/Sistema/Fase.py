class Fase:
    def __init__(self, local_spawn: tuple, local_chave: tuple, local_porta: tuple, mapa: str, num_fase: int):
        self.__local_spawn = local_spawn
        self.__local_chave = local_chave
        self.__local_porta = local_porta
        self.__mapa = mapa
        self.__num_fase = num_fase

    @property
    def local_spawn(self):
        return self.__local_spawn

    @property
    def local_chave(self):
        return self.__local_chave

    @property
    def local_porta(self):
        return self.__local_porta

    @property
    def mapa(self):
        return self.__mapa
    
    @property
    def num_fase(self):
        return self.__num_fase

    def gerenciar_tilemap(self):
        pass