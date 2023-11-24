from src.estados.estado import Estado
from src.fase.fase import Fase
from src.sistema.hud import HUD
from src.fase.colisao import Colisao
from src.fase.mapas import Mapas
import pygame

class Jogo(Estado):
    def __init__(self, game):
        super().__init__(game)
        self.__mapas = Mapas('fases').mapas
        self.__num_fase = 0
        
        self.__fase = Fase(self.__mapas[self.__num_fase], self.game.screen) # Cria várias fases com todos os mapas possíveis dentro da classe Mapas. Se quiser aumentar o número de fases, basta adicionar mais mapas na classe Mapas.
        
        self.__hud = HUD(game.screen)
        self.__colisao = Colisao(self.__fase)

    def entering(self):
        pass
    
    def exiting(self):
        pass
    
    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.estados.muda_estado('menu')

        self.__fase.update(event)
        self.__colisao.update()
        
        # verifica se o jogador ganhou a fase
        if self.__fase.passou_porta:
            self.proxima_fase()
        
        # verifica se o jogador perdeu a fase e reseta a fase
        if self.__fase.vidas == 0:
            self.game.estados.muda_estado('gameover')
            self.__num_fase = 0
            self.__fase = Fase(self.__mapas[self.__num_fase], self.game.screen)

    def render(self):
        self.__fase.render()
        self.__hud.render(self.__fase.vidas, self.__fase.jogador_sprite.abrir_porta)
        
    def proxima_fase(self):
        self.__num_fase += 1
        
        # verifica se existe mais alguma fase
        if self.__num_fase < len(self.__mapas):
            self.__fase = Fase(self.__mapas[self.__num_fase], self.game.screen)
            self.__colisao = Colisao(self.__fase)
            
        # se não existir mais fases, o jogador ganhou o jogo
        else:
            self.game.estados.muda_estado('gameover')
            self.__num_fase = 0
            self.__fase = Fase(self.__mapas[self.__num_fase], self.game.screen)
        