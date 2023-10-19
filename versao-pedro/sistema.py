import pygame, sys

class Sistema:
    def __init__(self):
        pygame.init()
        
        # variaveis de renderizacao
        self.__largura_tela = 1280
        self.__altura_tela = 720
        self.__FPS = 60
        self.__screen = pygame.display.set_mode((self.__largura_tela, self.__altura_tela))
        
        # definindo nome do jogo/janela
        pygame.display.set_caption("NOME NÃO DEFINIDO")

    def run(self):
        clock = pygame.time.Clock()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.__screen.fill('Blue')
            
            pygame.display.update()
            clock.tick(self.__FPS)

