import pygame, sys
from botao import Button
from estado import Estado

class MenuInicialTom(Estado):
    def __init__(self, game):
        super().__init__(self, game):

    def entering(self):
        self.__tela_fundo = pygame.image.load("placeholder")

    def exiting(self):
        pass

    def handler(self, tela):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if botao_iniciar.draw(tela):
                    
                    self.screen_manager.set_screen(GameScreen())
                elif self.quit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

    def update(self):
        pass

    def render(self, tela):
        #start button
        botao_iniciar = Button(200,150,"placeholder", 1)
        tela.blit(botao_iniciar)

        #quit button
        botao_sair = Button(200, 250, "placeholder", 1)
        tela.blit(botao_sair)


