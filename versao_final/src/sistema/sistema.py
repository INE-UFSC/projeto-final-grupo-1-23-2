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

        # definindo nome do jogo/janela
        pygame.display.set_caption("The Lost Key")
        pygame.display.set_icon(pygame.image.load("assets/UI/icon.png"))
        
        
        # ajustes musica
        pygame.mixer.music.load("assets/sounds/8Bit.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.05)
        # musica faz loop quando acaba
        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        
        
        self.__audio = True
        

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
    
    

    
    

