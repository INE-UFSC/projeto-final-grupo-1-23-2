import pygame
import sys
from src.estados.estado import Estado
from src.estados.botao import Botao

class MenuInicialState(Estado):
    def __init__(self, game):
        super().__init__(game)
        # CARREGAMENTO DOS ASSETS DO MENU
        
        # FUNDO
        self.__ceu = pygame.image.load('assets/backgrounds/River/1 ceu.png').convert_alpha()
        self.__nuvens = pygame.image.load('assets/backgrounds/River/2 nuvem.png').convert_alpha()
        self.__montanha1 = pygame.image.load('assets/backgrounds/River/3 montanha1.png').convert_alpha()
        self.__montanha2 = pygame.image.load('assets/backgrounds/River/4 montanha2.png').convert_alpha()
        self.__grama = pygame.image.load('assets/backgrounds/River/5 fundo grama.png').convert_alpha()
        
        # LOGO
        self.__logo = pygame.image.load('assets/UI/logo.png').convert_alpha()
        self.__trade = pygame.image.load('assets/UI/trade.png').convert_alpha()
        
        # BOTOES
        img_botao_play = pygame.image.load('assets/UI/botoes/play.png').convert_alpha()
        img_botao_quit = pygame.image.load('assets/UI/botoes/quit.png').convert_alpha()
        img_botao_skins = pygame.image.load('assets/UI/botoes/skins.png').convert_alpha()
        self.__botoes = {'play': Botao(490 , 422, img_botao_play), 
                         'skins': Botao(68, 521, img_botao_skins),
                         'quit': Botao(875, 521, img_botao_quit)}
        
        # CURSOR
        self.__cursor_img = pygame.image.load('assets/UI/mouse.png')
        self.__cursor_img_rect = self.__cursor_img.get_rect()
        
        # VARIAVEIS
        self.__scroll_montanha1 = 0
        self.__scroll_nuvem= 0
        self.__inicio = True
        self.__logoy = -500
        

    def entering(self):
        pygame.mouse.set_visible(False)
            
    def exiting(self):
        pygame.mouse.set_visible(True)

    def update(self, event):
        if self.__botoes['quit'].clicado():
            pygame.quit()
            sys.exit()
            
        if self.__botoes['play'].clicado():
            self.game.estados.muda_estado('jogo')
                
    def render(self):
        self.game.screen.blit(self.__ceu, (0,0)) # desenhando ceu
        
        # animacao da nuvem
        for i in range(0, -2, -1):
            self.game.screen.blit(self.__nuvens, (i * 1280 + int(self.__scroll_nuvem), 0))
        self.__scroll_nuvem +=0.5
        if abs(self.__scroll_nuvem) > 1280:
            self.__scroll_nuvem = 0
            
        # animacao da montanha fundo
        for i in range(2):
            self.game.screen.blit(self.__montanha1, (i * 1280 + int(self.__scroll_montanha1), 0))
        self.__scroll_montanha1 -=0.2
        if abs(self.__scroll_montanha1) > 1280:
            self.__scroll_montanha1 = 0
            
        self.game.screen.blit(self.__montanha2, (0,0)) # desenho montanha frente
            
        self.game.screen.blit(self.__grama, (0,0)) # desenho grama

        if self.__inicio:
            self.__logoy +=2
            if self.__logoy > -260:
                self.__inicio = False
        else:
            self.game.screen.blit(self.__trade, (419,80))
            
            for botao in self.__botoes.values():
                botao.draw(self.game.screen)
                
        self.game.screen.blit(self.__logo, (260, self.__logoy))
    
        # desenha o cursor
        self.__cursor_img_rect.center = pygame.mouse.get_pos()
        self.game.screen.blit(self.__cursor_img, self.__cursor_img_rect)
        