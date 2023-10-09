class Botao:
    def __init__(self, imagem: str, imagem_sombra: str, posicao: tuple, posicao_sombra: tuple, estado: str):
        self.__imagem = imagem
        self.__imagem_sombra = imagem_sombra
        self.__posicao = posicao
        self.__posicao_sombra = posicao_sombra
        self.__estado = estado

    @property
    def imagem(self):
        return self.__imagem
    
    @property
    def imagem_sombra(self):
        return self.__imagem_sombra
    
    @property
    def posicao(self):
        return self.__posicao
    
    @property
    def posicao_sombra(self):
        return self.__posicao_sombra
    
    @property
    def estado(self):
        return self.__estado
    
    def draw(self):
        pass
    
    def controle_evento(self):
        pass