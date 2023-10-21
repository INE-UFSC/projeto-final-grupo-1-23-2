import pygame
import sys
from src.estados.estado import Estado
from src.estados.botao import Botao

class MenuState(Estado):
    def __init__(self, game):
        super().__init__(game)
        self.__background = pygame.image.load('assets/backgrounds/menu.png').convert_alpha()
        self.__logo = pygame.image.load('assets/logo.png').convert_alpha()
        self.__botoes = {'iniciar': Botao(0 , 0, 'assets/botoes/iniciar.png', 1), 
                         'sair': Botao(0, 0, 'assets/botoes/sair.png', 1)}
        # CARREGAMENTO DOS ASSETS DO MENU
        

    def entering(self):
        pass
            
    def exiting(self):
        pass

    def update(self, keys_pressed: list[int]):
        for key in keys_pressed:
            if key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            elif key == pygame.K_RETURN:
                self.game.set_state()
                
    def render(self):
        self.__game.screen.blit(self.__background, (0, 0))
        self.__game.screen.blit(self.__logo, (self.__game.largura_tela//2, 90))
        self.__botoes['iniciar'].draw()
        self.__botoes['sair'].draw()
        