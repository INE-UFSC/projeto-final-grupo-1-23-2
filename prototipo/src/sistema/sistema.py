import pygame
import sys
from src.estados.menu import MenuState
from src.fase.mapas import Mapa
from src.estados.jogo import Jogo


class Sistema:
    def __init__(self):
        pygame.init()

        # variaveis de renderizacao
        self.largura_tela = Mapa().largura_tela
        self.altura_tela = Mapa().altura_tela
        self.__FPS = 60
        self.screen = pygame.display.set_mode(
            (self.largura_tela, self.altura_tela))

        # definindo nome do jogo/janela
        pygame.display.set_caption("Joguinho - Grupo 1 :P")
        
        # estado atual
        self.__estados = {'menu': MenuState(self), 'jogo': Jogo(self)}
        self.__estado_atual = self.__estados['menu']

    def run(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.__estado_atual.update(event)
            self.__estado_atual.render()

            pygame.display.update()
            clock.tick(self.__FPS)
            
    def define_estado(self, estado):
        self.__estado_atual.exiting()
        self.__estado_atual = self.__estados[estado]
        self.__estado_atual.entering()


# faltam implementar:
# fase = Fase(mapa1, tela, 1)
# fase.run()
