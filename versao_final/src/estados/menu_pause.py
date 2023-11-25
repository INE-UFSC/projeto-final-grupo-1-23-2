from src.estados.estado import Estado
from src.estados.botao import Botao
from src.sistema.configuracoes import Configuracoes
import sys
import pygame

class MenuPauseState(Estado):
    def __init__(self, game):
        super().__init__(game)
        img_botao_play = pygame.image.load('assets/UI/botoes/play.png').convert_alpha()
        img_botao_quit = pygame.image.load('assets/UI/botoes/quit.png').convert_alpha()
        img_botao_skins = pygame.image.load('assets/UI/botoes/skins.png').convert_alpha()
        self.__botoes = {'play': Botao(490 , 422, img_botao_play), 
                         'skins': Botao(68, 521, img_botao_skins),
                         'quit': Botao(875, 521, img_botao_quit)}
        
        # CURSOR
        self.__cursor_img = pygame.image.load('assets/UI/mouse.png')        
        self.__cursor_img_rect = self.__cursor_img.get_rect()

    def entering(self):
        pygame.mouse.set_visible(False)
        self.first = True
            
    def exiting(self):
        pygame.mouse.set_visible(True)

    def update(self, event):
        if self.__botoes['quit'].clicado():
            pygame.quit()
            sys.exit()
            
        if self.__botoes['play'].clicado():
            self.game.estados.muda_estado('jogo')
                
    def render(self):
        
        
        # renderiza botoes
        for botao in self.__botoes.values():
            botao.draw(self.game.screen)
            
        # desenha o cursor
        self.__cursor_img_rect.center = pygame.mouse.get_pos()
        self.game.screen.blit(self.__cursor_img, self.__cursor_img_rect)