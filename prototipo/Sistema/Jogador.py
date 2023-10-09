class Jogador:
    def __init__(self, imagem: str, altura: float, largura: float, vida: int, posicao: tuple, possui_chave: bool, velocidade: int):
        self.__imagem = imagem
        self.__altura = altura
        self.__largura = largura
        self.__vida = vida
        self.__posicao = posicao
        self.__possui_chave = possui_chave
        self.__velocidade = velocidade

    @property
    def imagem(self):
        return self.__imagem
    
    @property
    def altura(self):
        return self.__altura

    @property
    def largura(self):
        return self.__largura

    @property
    def vida(self):
        return self.__vida
    
    @property
    def posicao(self):
        return self.__posicao
    
    @property
    def possui_chave(self):
        return self.__possui_chave

    @property
    def velocidade(self):
        return self.__velocidade
    
    def andar(self):
        pass

    def pular(self):
        pass

    def agachar(self):
        pass

    def abrir_porta(self):
        pass

    def chave_segue(self):
        pass