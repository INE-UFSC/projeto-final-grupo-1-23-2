from src.estados.estado import Estado
from src.fase.fase import Fase
from src.fase.mapas import Mapas
import pygame

class Jogo(Estado):
    def __init__(self, game):
        super().__init__(game)
        self.__mapas = Mapas('fases').mapas
        self.__num_fase = 0
        
        self.__fase = Fase(self.__mapas[self.__num_fase], self.game.screen, 1)
        self.__esc = False
        

    def entering(self):
        self.__esc = True
    
    def exiting(self):
        pass
    
    def update(self, event):
        # verificação se não está pegando evento de um estado anterior
        if self.__esc and (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) and self.game.estados.estado_anterior == 'menu pause':
            self.__esc = False
            
        if not self.game.estados.estado_anterior == 'menu pause':
            self.__esc = False
            
        
        if not self.__esc and event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.game.estados.muda_estado('menu pause')

        self.__fase.update(event)
        
        # verifica se o jogador ganhou a fase
        if self.__fase.passou_porta:
            self.proxima_fase()
        
        # verifica se o jogador perdeu a fase e reseta o jogo
        if self.__fase.vidas == 0:
            self.game.estados.muda_estado('gameover')
            self.__num_fase = 0
            self.__fase = Fase(self.__mapas[self.__num_fase], self.game.screen)
    
    def render(self):
        self.__fase.render()
        
    def proxima_fase(self):
        self.__num_fase += 1
        
        # verifica se existe mais alguma fase
        if self.__num_fase < len(self.__mapas):
            self.__fase = Fase(self.__mapas[self.__num_fase], self.game.screen)
            
        # se não existir mais fases, o jogador ganhou o jogo
        else:
            self.game.estados.muda_estado('menu vitoria')
            self.__num_fase = 0
            self.__fase = Fase(self.__mapas[self.__num_fase], self.game.screen)
            
    def reset(self):
        self.__fase.reset()
        