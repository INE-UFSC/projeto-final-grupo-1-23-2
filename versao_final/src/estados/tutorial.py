import pygame
import sys
from src.estados.estado import Estado
from src.estados.botao import Botao
from src.sistema.configuracoes import Configuracoes

class TutorialState(Estado):
    def __init__(self, game):
        super().__init__(game)
        
        # imagem principal tutorial
        self.__menututorial = pygame.image.load('assets/UI/tutorial.png').convert_alpha()
        
        # botao fechar
        img_botao_quit = pygame.image.load('assets/UI/pause/fechar.png').convert_alpha()
        self.__botoes = {'quit': Botao(1210, 16, img_botao_quit)}
        
        # carregando dados cursor
        self.__cursor_img = pygame.image.load('assets/UI/mouse.png')        
        self.__cursor_img_rect = self.__cursor_img.get_rect()
        
        
        
    def entering(self):
        pygame.mouse.set_visible(False) # esconde o cursor
        self.__screenshot = self.game.screen.copy() # tira um screenshot da tela anterior
        
        # desenha camada escura
        self.__surface = pygame.Surface((Configuracoes().largura_tela, Configuracoes().altura_tela), pygame.SRCALPHA)
        pygame.draw.rect(self.__surface, (0, 0, 0, 150), [0, 0, Configuracoes().largura_tela, Configuracoes().altura_tela])
    
    def exiting(self):
        pygame.mouse.set_visible(True)
    
    def update(self, event):
        if self.__botoes['quit'].clicado():
            
            if self.game.estados.estado_anterior == 'menu pause':
                self.game.estados.muda_estado('jogo')
                
            else:
                self.game.estados.muda_estado(self.game.estados.estado_anterior)
    
    def render(self):
        self.game.screen.blit(self.__screenshot, (0,0)) # desenha screenshot da tela anterior
        self.game.screen.blit(self.__surface, (0,0)) # desenha camada escura
        self.game.screen.blit(self.__menututorial, (27,38)) # desenha fundo do menu
        
        # renderiza botoes
        for botao in self.__botoes.values():
            botao.draw(self.game.screen)
            
        # desenha o cursor
        self.__cursor_img_rect = pygame.mouse.get_pos()
        self.game.screen.blit(self.__cursor_img, self.__cursor_img_rect)
        
        
