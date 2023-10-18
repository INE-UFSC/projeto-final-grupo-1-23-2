import pygame, sys
from Sistema.presets import *
from Sistema.Fase import Fase

pygame.init()

tela = pygame.display.set_mode((largura_tela, altura_tela))
clock = pygame.time.Clock()
pygame.display.set_caption("jogo de plataforma sem nome")

fase = Fase(mapa1, tela)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill('Blue')
    fase.run()
                      
    pygame.display.update()
    clock.tick(60)

    #teste