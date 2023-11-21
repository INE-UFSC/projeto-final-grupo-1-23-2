import pygame
import sys
from src.estados.menu import MenuState
from src.fase.mapas import Mapa
from src.estados.jogo import Jogo
from src.estados.gameover import GameOverState


class Sistema:
    def __init__(self):
        pygame.init()

        # variaveis de renderizacao
        # pega a largura e altura seguindo os tiles (que estão na classe Mapa)
        self.largura_tela = Mapa().largura_tela
        self.altura_tela = Mapa().altura_tela
        self.__FPS = 60
        self.screen = pygame.display.set_mode(
            (self.largura_tela, self.altura_tela))

        # definindo nome do jogo/janela
        pygame.display.set_caption("Joguinho - Grupo 1 :P")

        # estado atual
        self.__estados = {'menu': MenuState(self), 'jogo': Jogo(
            self, self.screen), 'gameover': GameOverState(self)}
        self.__estado_atual = self.__estados['menu']

        self.altera_mouse()

    def run(self):
        clock = pygame.time.Clock()

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.__estado_atual.update(event)
            self.__estado_atual.render()

            # renderização do mouse
            self.cursor_img_rect.center = pygame.mouse.get_pos()
            self.screen.blit(self.cursor_img, self.cursor_img_rect)

            pygame.display.update()
            clock.tick(self.__FPS)

    # função que serve para mudar o estado atual para um outro estado que esteja no dicionario de estados
    # essa função eh chamada dentro da classe de cada estado

    def define_estado(self, estado):
        self.__estado_atual.exiting()
        self.__estado_atual = self.__estados[estado]
        self.__estado_atual.entering()

    def altera_mouse(self):
        pygame.mouse.set_visible(False)
        self.cursor_img = pygame.image.load(
            'Assets/assets_forest/smaller_image_401.png')
        self.cursor_img_rect = self.cursor_img.get_rect()
