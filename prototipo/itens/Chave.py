from ItemAbstrato import ItemAbstrato

class Chave(ItemAbstrato):
    def __init__(self, imagem: str, som_interacao: str):
        super().__init__(imagem, som_interacao)

    def colisao_jogador(self):
        pass