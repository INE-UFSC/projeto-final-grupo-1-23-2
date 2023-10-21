import pygame
import sys
from src.estados.estado import Estado
from src.estados.botao import Botao

class MenuState(Estado):
    def __init__(self, game):
        super().__init__(game)
        # CARREGAMENTO DOS ASSETS DO MENU
        self.__background = pygame.image.load('assets/backgrounds/menu.png').convert_alpha()
        self.__logo = pygame.image.load('assets/logo.png').convert_alpha()
        img_botao_iniciar = pygame.image.load('assets/botoes/iniciar.png').convert_alpha()
        img_botao_sair = pygame.image.load('assets/botoes/sair.png').convert_alpha()
        self.__botoes = {'iniciar': Botao(490 , 388, img_botao_iniciar, 1), 
                         'sair': Botao(490, 528, img_botao_sair, 1)}
        

    def entering(self):
        pass
            
    def exiting(self):
        pass

    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if self.__botoes['sair'].clicado():
            pygame.quit()
            sys.exit()
            
        if self.__botoes['iniciar'].clicado():
            print("oi")
                
    def render(self):
        self.game.screen.fill('White')
        self.game.screen.blit(self.__background, (0, 0))
        self.game.screen.blit(self.__logo, (357, 90))
        self.__botoes['iniciar'].draw(self.game.screen)
        self.__botoes['sair'].draw(self.game.screen)
        