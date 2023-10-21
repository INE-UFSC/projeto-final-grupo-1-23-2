import pygame
import sys
from src.estados.menu import MenuState


class Sistema:
    def __init__(self):
        pygame.init()

        # variaveis de renderizacao
        self.__largura_tela = 1280
        self.__altura_tela = 720
        self.__FPS = 60
        self.screen = pygame.display.set_mode(
            (self.__largura_tela, self.__altura_tela))

        # definindo nome do jogo/janela
        pygame.display.set_caption("Joguinho - Grupo 1 :P")
        
        # estado atual
        self.__estado_atual = MenuState(self)

    def run(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.__estado_atual.render()
                self.__estado_atual.update(event)

            pygame.display.update()
            clock.tick(self.__FPS)
            
    def define_estado(self, estado):
        self.__estado_atual.exiting()
        self.__estado_atual = estado
        self.__estado_atual.entering()


# faltam implementar:
# fase = Fase(mapa1, tela, 1)
# fase.run()
