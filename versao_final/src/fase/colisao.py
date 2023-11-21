from fase import Fase

class Colisao:
    def __init__(self, fase: Fase):
        self.__fase = fase

    def colisao_horizontal_jogador_mapa(self):
        pass

    def colisao_vertical_jogador_mapa(self):
        jogador = self.__fase.jogador.sprite

        for sprite in self.__fase.tiles.sprites(): #verifica se o jogador esta colidindo com algum retangulo
            if sprite.colliderect(jogador.rect):
                if jogador.direcao.y > 0: #se o jogador está em cima, a parte debaixo do jogador e setada como a parte do topo do retangulo
                    jogador.rect.bottom = sprite.rect.top
                    jogador.direcao.y = 0
                    jogador.no_chao = True
                
                elif jogador.direcao.y < 0: #se o jogador está pulando e batendo na parte debaixo de um retangulo
                    jogador.rect.top = sprite.rect.bottom
                    jogador.direcao.y = 0
                    jogador.no_teto = True
                
                if jogador.no_chao and jogador.direcao.y < 0 or jogador.direcao.y > 1: #verifica se o jogador esta pulando
                    jogador.no_chao = False
                if jogador.no_teto and jogador.direcao.y > 0: #verifica se o jogador esta caindo
                    jogador.no_teto = False

    def update(self):
        self.colisao_horizontal_jogador_mapa()
        self.colisao_vertical_jogador_mapa()

