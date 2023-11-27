import pygame
import sys
from src.estados.estado import Estado
from src.estados.botao import Botao
from src.sistema.configuracoes import Configuracoes

class GameOverState(Estado):
    def __init__(self, game):
        super().__init__(game)
        # CARREGAMENTO DOS ASSETS DO MENU
        background = pygame.image.load('assets/backgrounds/menu.png').convert_alpha()
        self.__background = pygame.transform.scale(background, (Configuracoes().largura_tela, Configuracoes().altura_tela))
        self.__texto = pygame.image.load('assets/UI/texto_parabens.png').convert_alpha()
        img_botao_menu = pygame.image.load('assets/UI/botoes/play.png').convert_alpha()
        img_botao_sair = pygame.image.load('assets/UI/botoes/quit.png').convert_alpha()
        self.__botoes = {'menu': Botao((Configuracoes().largura_tela - img_botao_menu.get_width())//4 , 500, img_botao_menu, 1), 
                         'sair': Botao((Configuracoes().largura_tela - img_botao_sair.get_width())*3//4, 500, img_botao_sair, 1)}
        self.__cursor_img = pygame.image.load('assets/UI/mouse.png')
        self.__cursor_img_rect = self.__cursor_img.get_rect()
        

    def entering(self):
        pygame.mouse.set_visible(False)
            
    def exiting(self):
        pygame.mouse.set_visible(True)

    def update(self, event):
        if self.__botoes['sair'].clicado():
            pygame.quit()
            sys.exit()
            
        if self.__botoes['menu'].clicado():
            self.game.estados.muda_estado('menu inicial')
                
    def render(self):
        self.game.screen.fill('White')
        self.game.screen.blit(self.__background, (0, 0))
        self.game.screen.blit(self.__texto, ((Configuracoes().largura_tela - self.__texto.get_width())//2, 186))
        self.__botoes['menu'].draw(self.game.screen)
        self.__botoes['sair'].draw(self.game.screen)
        
        # desenha o cursor
        self.__cursor_img_rect.center = pygame.mouse.get_pos()
        self.game.screen.blit(self.__cursor_img, self.__cursor_img_rect)
        