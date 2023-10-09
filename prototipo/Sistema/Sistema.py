class Sistema:
    def __init__(self, fase_atual, jogando: bool, fases: list, estado: str, info_jogador):
        self.__fase_atual = fase_atual
        self.__jogando = jogando
        self.__fases = fases
        self.__estado = estado
        self.__info_jogador = info_jogador
        
    @property
    def fase_atual(self):
        return self.__fase_atual
    
    @property
    def jogando(self):
        return self.__jogando
    
    @property
    def fases(self):
        return self.__fases
    
    @property
    def estado(self):
        return self.__estado
    
    @property
    def info_jogador(self):
        return self.__info_jogador
    
    def trocar_fase(self):
        pass
    
    def salvar_dados(self):
        pass
        