import pygame

class Porta(pygame.sprite.Sprite):
    def __init__(self, posicao):
        super().__init__()
        self.image = pygame.image.load('assets/tiles/porta/portaFechada.png')
        self.image.convert_alpha() #alpha porque a imagem é transparente
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(topleft = posicao)
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)
