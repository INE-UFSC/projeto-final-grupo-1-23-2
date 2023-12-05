import pygame
import sys
from src.estados.estado import Estado
from src.estados.botao import Botao
from src.sistema.configuracoes import Configuracoes

class GameOverState(Estado):
    def __init__(self, game):
        super().__init__(game)
       
        # tela principal de finalização
        self.__caveira = pygame.image.load('assets/UI/game over/caveira.png').convert_alpha()
        
        self.__caveiray = 5
        self.__scroll = -0.3
        
        self.__gameover = pygame.image.load('assets/UI/game over/game over.png').convert_alpha()
        
        # BOTOES
        img_botao_menu = pygame.image.load('assets/UI/game over/menu.png').convert_alpha()
        img_botao_sair = pygame.image.load('assets/UI/game over/sair.png').convert_alpha()
        
        self.__botoes = {'menu': Botao(470 , 556, img_botao_menu), 
                         'sair': Botao(833, 556, img_botao_sair),}
        
        # CURSOR
        self.__cursor_img = pygame.image.load('assets/UI/mouse.png')
        self.__cursor_img_rect = self.__cursor_img.get_rect()
        
        

    def entering(self):
        pygame.mouse.set_visible(False) # esconde o cursor
        self.__screenshot = self.game.screen.copy() # tira um screenshot da tela anterior
        
        # desenha camada escura
        self.__surface = pygame.Surface((Configuracoes().largura_tela, Configuracoes().altura_tela), pygame.SRCALPHA)
        pygame.draw.rect(self.__surface, (255, 0, 0, 96), [0, 0, Configuracoes().largura_tela, Configuracoes().altura_tela])
            
    def exiting(self):
        pygame.mouse.set_visible(True)

    def update(self, event):
        if self.__botoes['sair'].clicado():
            pygame.quit()
            sys.exit()
            
        if self.__botoes['menu'].clicado():
            self.game.estados.muda_estado('menu inicial')
        
                
    def render(self):
        self.game.screen.blit(self.__screenshot, (0,0)) # desenha screenshot da tela anterior
        self.game.screen.blit(self.__surface, (0,0)) # desenha camada escura
                
        self.game.screen.blit(self.__gameover, (213, 313))
        self.game.screen.blit(self.__caveira, (507, self.__caveiray))
        
        for botao in self.__botoes.values():
            botao.draw(self.game.screen)

        if self.__caveiray > 30 or self.__caveiray < 5:
            self.__scroll *= -1
            
        self.__caveiray = self.__caveiray + self.__scroll

        # desenha o cursor
        self.__cursor_img_rect = pygame.mouse.get_pos()
        self.game.screen.blit(self.__cursor_img, self.__cursor_img_rect)
        