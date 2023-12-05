import pygame
import sys
from src.estados.estado import Estado
from src.estados.botao import Botao
from src.sistema.configuracoes import Configuracoes

class MenuVitoriaState(Estado):
    def __init__(self, game):
        super().__init__(game)
       
        # tela principal de finalização
        self.__tela_principal = pygame.image.load('assets/UI/tela final/tela final.png').convert_alpha()
        
        # BOTOES
        img_botao_menu = pygame.image.load('assets/UI/pause/home.png').convert_alpha()
        img_botao_encerrar = pygame.image.load('assets/UI/pause/quit.png').convert_alpha()
        
        self.__botoes = {'menu': Botao(470 , 444, img_botao_menu), 
                         'encerrar': Botao(833, 444, img_botao_encerrar),}
        
        # CURSOR
        self.__cursor_img = pygame.image.load('assets/UI/mouse.png')
        self.__cursor_img_rect = self.__cursor_img.get_rect()
        self.__scroll = -300
        
        

    def entering(self):
        self.__scroll = -300
        
        pygame.mouse.set_visible(False) # esconde o cursor
        self.__screenshot = self.game.screen.copy() # tira um screenshot da tela anterior
        
        # desenha camada escura
        self.__surface = pygame.Surface((Configuracoes().largura_tela, Configuracoes().altura_tela), pygame.SRCALPHA)
        pygame.draw.rect(self.__surface, (0, 0, 0, 150), [0, 0, Configuracoes().largura_tela, Configuracoes().altura_tela])
            
    def exiting(self):
        pygame.mouse.set_visible(True)

    def update(self, event):
        if self.__botoes['encerrar'].clicado():
            pygame.quit()
            sys.exit()
            
        if self.__botoes['menu'].clicado():
            self.game.estados.muda_estado('menu inicial')
        
                
    def render(self):
        self.game.screen.blit(self.__screenshot, (0,0)) # desenha screenshot da tela anterior
        self.game.screen.blit(self.__surface, (0,0)) # desenha camada escura
                
        self.game.screen.blit(self.__tela_principal, (0, self.__scroll))
        
        if self.__scroll < 0:
            self.__scroll += 4
        else:
            self.__scroll = 0
            for botao in self.__botoes.values():
                botao.draw(self.game.screen)
    
        # desenha o cursor
        self.__cursor_img_rect = pygame.mouse.get_pos()
        self.game.screen.blit(self.__cursor_img, self.__cursor_img_rect)
        