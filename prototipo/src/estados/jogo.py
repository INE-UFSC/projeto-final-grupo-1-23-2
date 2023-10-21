from src.estados.estado import Estado
from src.fase.fase import Fase
from src.fase.mapas import Mapa
import pygame

class Jogo(Estado):
    def __init__(self, game):
        super().__init__(game)
        self.__fases = [Fase(Mapa().mapa[i], self.game.screen, i) for i in range(len(Mapa().mapa))] # Cria várias fases com todos os mapas possíveis dentro da classe Mapas. Se quiser aumentar o número de fases, basta adicionar mais mapas na classe Mapas.
        self.__fase_atual = 0 # Inicia na fase 0, cada fase é o indice da lista de fases.
        
    def entering(self):
        pass
    
    def exiting(self):
        pass
    
    def update(self, event):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.define_estado('menu')
            self.__fases[self.__fase_atual].run()
    
    def render(self):
        pass
