from src.estados.estado import Estado
from src.estados.botao import Botao
from src.sistema.configuracoes import Configuracoes
import sys
import pygame

class MenuPauseState(Estado):
    def __init__(self, game):
        super().__init__(game)
        # IMAGENS
        img_botao_home = pygame.image.load('assets/UI/pause/home.png').convert_alpha()
        img_botao_restart = pygame.image.load('assets/UI/pause/restart.png').convert_alpha()
        img_botao_quit = pygame.image.load('assets/UI/pause/quit.png').convert_alpha()
        img_botao_mute = pygame.image.load('assets/UI/pause/audio.png').convert_alpha()
        img_botao_fechar = pygame.image.load('assets/UI/pause/fechar.png').convert_alpha()
        
        self.__fundo = pygame.image.load('assets/UI/pause/fundo.png').convert_alpha()
        
        # BOTOES
        self.__botoes = {'home': Botao(655, 207, img_botao_home), 
                         'restart': Botao(655, 348, img_botao_restart),
                         'quit': Botao(599, 490, img_botao_quit),
                         'mute': Botao(811, 490, img_botao_mute),
                         'fechar': Botao(917, 72, img_botao_fechar)}
        
        # CURSOR
        self.__cursor_img = pygame.image.load('assets/UI/mouse.png')        
        self.__cursor_img_rect = self.__cursor_img.get_rect()

    def entering(self):
        pygame.mouse.set_visible(False) # esconde o cursor
        self.screenshot = self.game.screen.copy() # tira um screenshot da tela anterior
        
        # desenha camada escura
        self.surface = pygame.Surface((Configuracoes().largura_tela, Configuracoes().altura_tela), pygame.SRCALPHA)
        pygame.draw.rect(self.surface, (0, 0, 0, 150), [0, 0, Configuracoes().largura_tela, Configuracoes().altura_tela])
            
    def exiting(self):
        pygame.mouse.set_visible(True)

    def update(self, event):
        if self.__botoes['quit'].clicado():
            pygame.quit()
            sys.exit()
            
        if self.__botoes['home'].clicado():
            self.game.estados.muda_estado('menu inicial')
            
        if self.__botoes['restart'].clicado():
            self.game.estados.reset('jogo')
            self.game.estados.muda_estado('jogo')
            
        if self.__botoes['fechar'].clicado():
            self.game.estados.muda_estado('jogo')
                
    def render(self):
        self.game.screen.blit(self.screenshot, (0,0)) # desenha screenshot da tela anterior

        self.game.screen.blit(self.surface, (0,0)) # desenha camada escura
        
        self.game.screen.blit(self.__fundo, (358,88)) # desenha fundo do menu
        
        # renderiza botoes
        for botao in self.__botoes.values():
            botao.draw(self.game.screen)
            
        # desenha o cursor
        self.__cursor_img_rect.center = pygame.mouse.get_pos()
        self.game.screen.blit(self.__cursor_img, self.__cursor_img_rect)