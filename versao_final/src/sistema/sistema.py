#coisa de linux pc sala
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame
import sys
from src.estados.controle_estados import StateMachine
from src.sistema.configuracoes import Configuracoes


class Sistema:
    def __init__(self):
        pygame.init()

        # variaveis de renderizacao
        self.__screen = pygame.display.set_mode(
            (Configuracoes().largura_tela, Configuracoes().altura_tela))
        self.__audio = True

        # definindo nome do jogo/janela
        pygame.display.set_caption("The Lost Key")
        pygame.display.set_icon(pygame.image.load("assets/UI/icon.png"))

        # maquina de estados
        self.__estados = StateMachine(self)

        pygame.mouse.set_visible(False)

    def run(self):
        clock = pygame.time.Clock()

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.__estados.run(event)

            pygame.display.update()
            clock.tick(Configuracoes().FPS)

    @property
    def estados(self):
        return self.__estados
    
    @property
    def screen(self):
        return self.__screen
    
    @property
    def audio(self):
        return self.__audio
    
    @audio.setter
    def audio(self, audio):
        self.__audio = audio
    
    

