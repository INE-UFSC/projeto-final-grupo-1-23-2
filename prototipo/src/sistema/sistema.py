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
        pygame.display.set_caption("NOME NÃO DEFINIDO")

    def run(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            MenuState(self).render(self.screen)

            pygame.display.update()
            clock.tick(self.__FPS)
            
    @property
    def largura_tela(self):
        return self.__largura_tela
    
    @property
    def altura_tela(self):
        return self.__altura_tela
    
    

# faltam implementar:
# fase = Fase(mapa1, tela, 1)
# fase.run()
