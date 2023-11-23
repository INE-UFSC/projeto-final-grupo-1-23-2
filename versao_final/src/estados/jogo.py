from src.estados.estado import Estado
from src.fase.fase import Fase
from src.fase.mapas import Mapa
from src.sistema.hud import HUD
from src.fase.colisao import Colisao
import pygame

class Jogo(Estado):
    def __init__(self, game, superficie):
        super().__init__(game)
        self.__fase = Fase(Mapa().mapa[0], self.game, 0, 5) # Cria várias fases com todos os mapas possíveis dentro da classe Mapas. Se quiser aumentar o número de fases, basta adicionar mais mapas na classe Mapas.
        self.__hud = HUD(superficie)
        self.__colisao = Colisao(self.__fase)

    def entering(self):
        pass
    
    def exiting(self):
        pass
    
    def update(self, event):
            #condicional virou função abrir_menu()
            self.abrir_menu(event)

            self.__fase.update(event)
            self.__colisao.update()
            
            #criada a função morto()
            self.morto()
            
            self.__hud.mostrar_vida(self.__fase.vidas)
            self.__hud.mostrar_chave(self.__fase.jogador_sprite.abrir_porta)

    def abrir_menu(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.define_estado('menu')

    def morto(self):
        if self.__fase.vidas == 0:
            self.game.define_estado('gameover')

    def render(self):
        pass