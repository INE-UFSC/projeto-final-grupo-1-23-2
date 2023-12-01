from src.sistema.configuracoes import Configuracoes

class Colisao:
    def __init__(self, fase):
        self.__fase = fase

    def colisao_horizontal_jogador_mapa(self):
        jogador = self.__fase.jogador.sprite

        for sprite in self.__fase.colide.sprites() + self.__fase.libera_chave.sprites():
            if sprite.rect.colliderect(jogador.animacao_jogador.rect): #verifica se o jogador esta colidindo com algum retangulo
                if jogador.estado_jogador.direcao.x < 0: #faz o jogador ficar na direita do retangulo que ele colidiu
                    jogador.animacao_jogador.rect.left = sprite.rect.right #visto que ele se aproximou pela esquerda
                    jogador.estado_jogador.na_esquerda = True
                
                elif jogador.estado_jogador.direcao.x > 0: #faz o jogador ficar na esquerda do retangulo que ele colidiu
                    jogador.animacao_jogador.rect.right = sprite.rect.left #visto que ele se aproximou pela direita
                    jogador.estado_jogador.na_direita = True

        #verificacoes para o jogador nao sair horizontalmente do mapa
        if jogador.animacao_jogador.rect.left <= 0:
            jogador.animacao_jogador.rect.left = 0
        if jogador.animacao_jogador.rect.right >= Configuracoes().largura_tela:
            jogador.animacao_jogador.rect.right = Configuracoes().largura_tela

    def colisao_vertical_jogador_mapa(self):
        jogador = self.__fase.jogador.sprite
        jogador.animacao_jogador.atualizar_posicao_vertical_com_gravidade()

        for sprite in self.__fase.colide.sprites() + self.__fase.libera_chave.sprites(): #verifica se o jogador esta colidindo com algum retangulo
            if sprite.rect.colliderect(jogador.animacao_jogador.rect):
                if jogador.estado_jogador.direcao.y > 0: #se o jogador está em cima, a parte debaixo do jogador e setada como a parte do topo do retangulo
                    jogador.animacao_jogador.rect.bottom = sprite.rect.top
                    jogador.estado_jogador.direcao.y = 0
                    jogador.estado_jogador.no_chao = True
                
                elif jogador.estado_jogador.direcao.y < 0: #se o jogador está pulando e batendo na parte debaixo de um retangulo
                    jogador.animacao_jogador.rect.top = sprite.rect.bottom
                    jogador.estado_jogador.direcao.y = 0
                    jogador.estado_jogador.no_teto = True
                            
            if jogador.estado_jogador.no_chao and jogador.estado_jogador.direcao.y < 0 or jogador.estado_jogador.direcao.y > 1: #verifica se o jogador esta pulando
                jogador.estado_jogador.no_chao = False
            if jogador.estado_jogador.no_teto and jogador.estado_jogador.direcao.y > 0: #verifica se o jogador esta caindo
                jogador.estado_jogador.no_teto = False

    def colisao_chave(self):
        jogador = self.__fase.jogador.sprite

        if self.__fase.chave_sprite.rect.colliderect(jogador.animacao_jogador.rect): #verifica se ha colisao entre a chave e o jogador
            self.__fase.chave_sprite.hide()
            self.__fase.libera_chave.empty()
            self.__fase.jogador_sprite.desbloquear_porta()

    def colisao_porta(self):
        jogador = self.__fase.jogador.sprite

        if self.__fase.porta_sprite.rect.colliderect(jogador.animacao_jogador.rect): #verifica se ha colisao entre a porta e o jogador
            if self.__fase.jogador_sprite.abrir_porta == True:
                self.__fase.passou_porta = True

    def colisao_inimigo_jogador(self):
        if self.__fase.inimigo in self.__fase.tiles:
            jogador = self.__fase.jogador.sprite
            inimigo = self.__fase.inimigo.sprite
            if inimigo.rect.colliderect(jogador.animacao_jogador.rect):
                self.__fase.vidas = -1
                self.__fase.reset()

    def colisao_espinho_jogador(self):
        if self.__fase.espinhos in self.__fase.tiles:
            jogador = self.__fase.jogador.sprite
            for sprite in self.__fase.espinhos.sprites():
                if sprite.rect.colliderect(jogador.animacao_jogador.rect):
                    self.__fase.vidas = -1
                    self.__fase.reset()

    def colisao_inimigo_obstaculo(self):
        if self.__fase.inimigo in self.__fase.tiles:
            inimigo = self.__fase.inimigo.sprite
            for sprite in self.__fase.inimigo_colisores.sprites():
                if sprite.rect.colliderect(inimigo.rect): #verifica se o jogador esta colidindo com algum retangulo
                    if inimigo.direcao.x < 0 or inimigo.direcao.x >0: #faz o jogador ficar na direita do retangulo que ele colidiu
                        inimigo.direcao.x *= -1

    def update(self):
        self.colisao_horizontal_jogador_mapa()
        self.colisao_vertical_jogador_mapa()
        self.colisao_chave()
        self.colisao_porta()
        self.colisao_inimigo_jogador()
        self.colisao_inimigo_obstaculo()
        self.colisao_espinho_jogador()

