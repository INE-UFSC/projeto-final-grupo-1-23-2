from src.sistema.configuracoes import Configuracoes
import pygame
class Colisao:
    def __init__(self, fase):
        self.__fase = fase

    def colisao_horizontal_jogador_mapa(self):
        jogador = self.__fase.jogador.sprite

        for sprite in self.__fase.colide.sprites() + self.__fase.libera_chave.sprites():
            if sprite.rect.colliderect(jogador.rect): #verifica se o jogador esta colidindo com algum retangulo
                if jogador.direcao.x < 0: #faz o jogador ficar na direita do retangulo que ele colidiu
                    jogador.rect.left = sprite.rect.right #visto que ele se aproximou pela esquerda
                    jogador.na_esquerda = True
                
                elif jogador.direcao.x > 0: #faz o jogador ficar na esquerda do retangulo que ele colidiu
                    jogador.rect.right = sprite.rect.left #visto que ele se aproximou pela direita
                    jogador.na_direita = True

        #verificacoes para o jogador nao sair horizontalmente do mapa
        if jogador.rect.left <= 0:
            jogador.rect.left = 0
        if jogador.rect.right >= Configuracoes().largura_tela:
            jogador.rect.right = Configuracoes().largura_tela


    def colisao_vertical_jogador_mapa(self):
        jogador = self.__fase.jogador.sprite
        jogador.aplicar_gravidade()

        for sprite in self.__fase.colide.sprites() + self.__fase.libera_chave.sprites(): #verifica se o jogador esta colidindo com algum retangulo
            if sprite.rect.colliderect(jogador.rect):
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

    def colisao_chave(self):
        jogador = self.__fase.jogador.sprite

        if self.__fase.chave_sprite.rect.colliderect(jogador.rect): #verifica se ha colisao entre a chave e o jogador
            self.__fase.chave_sprite.hide()
            self.__fase.libera_chave.empty()
            self.__fase.jogador_sprite.desbloquear_porta()

    def colisao_porta(self):
        jogador = self.__fase.jogador.sprite

        if self.__fase.porta_sprite.rect.colliderect(jogador.rect): #verifica se ha colisao entre a porta e o jogador
            if self.__fase.jogador_sprite.abrir_porta == True:
                self.__fase.passou_porta = True

    def colisao_inimigo_jogador(self):
        if self.__fase.inimigo in self.__fase.tiles:
            jogador = self.__fase.jogador.sprite
            inimigo = self.__fase.inimigo.sprite
            inimigo_center_x = inimigo.rect.x + inimigo.rect.width // 2
            inimigo_center_y = inimigo.rect.y + inimigo.rect.height // 2
            inimigo_collide_area = pygame.Rect(
                inimigo_center_x - 22,
                inimigo_center_y - 22,
                45,
                45
            )

            if jogador.rect.colliderect(inimigo_collide_area):
                self.__fase.vidas = -1
                self.__fase.reset()

    def colisao_espinho_jogador(self):
        if self.__fase.espinhos in self.__fase.tiles:
            jogador = self.__fase.jogador.sprite
            for sprite in self.__fase.espinhos.sprites():
                espinho_center_x = sprite.rect.x + sprite.rect.width // 2
                espinho_center_y = sprite.rect.y + sprite.rect.height // 2
                # Define o retângulo da área do centro do espinho
                center_area_rect = pygame.Rect(
                    espinho_center_x - 10,  #numero aleatorio, da pra alterar
                    espinho_center_y - 10, 
                    20, #numero aleatorio, da pra alterar
                    20,  
                )
                if jogador.rect.colliderect(center_area_rect):
                    self.__fase.vidas = -1
                    self.__fase.reset()

    def colisao_inimigo_obstaculo(self):
        if self.__fase.inimigo in self.__fase.tiles:
            inimigo = self.__fase.inimigo.sprite
            for sprite in self.__fase.inimigo_colisores.sprites():
                if sprite.rect.colliderect(inimigo.rect): #verifica se o jogador esta colidindo com algum retangulo
                    if inimigo.direcao.x < 0 or inimigo.direcao.x >0: #faz o jogador ficar na direita do retangulo que ele colidiu
                        inimigo.direcao.x *= -1


    def colisao_inimigo_espada(self):
        if self.__fase.inimigo in self.__fase.tiles:
            inimigo = self.__fase.inimigo_sprite
            jogador = self.__fase.jogador_sprite
            area_ataque = jogador.retangulo_ataque
            if area_ataque.colliderect(inimigo.rect) and jogador.atacando:
                inimigo.vida_inicial -= 1
                print(inimigo.vida_inicial) # if try == 8#mychoise
                print("hit")
                

    def colisao_inimigo_espada(self):
        if self.__fase.inimigo in self.__fase.tiles:
            inimigo = self.__fase.inimigo_sprite
            jogador = self.__fase.jogador_sprite
            area_ataque = jogador.retangulo_ataque

            if inimigo.vida_inicial > 0:
                if area_ataque.colliderect(inimigo.rect) and jogador.atacando:
                    inimigo.dano_recebido()
    
            else:
                inimigo.morte()
                self.__vivo = False
                

    def update(self):
        self.colisao_horizontal_jogador_mapa()
        self.colisao_vertical_jogador_mapa()
        self.colisao_chave()
        self.colisao_porta()
        self.colisao_inimigo_jogador()
        self.colisao_inimigo_obstaculo()
        self.colisao_inimigo_espada()
        self.colisao_espinho_jogador()

