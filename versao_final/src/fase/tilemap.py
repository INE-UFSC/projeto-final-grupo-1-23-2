import pygame

class TileMap(pygame.sprite.Sprite):
    def __init__(self, posicao, imagem, grupo):
        super().__init__(grupo)
        self.image = imagem # valores de x e y (iguais nesse caso)
        posicao = (posicao[0] * 64, posicao[1] * 64)
        self.rect = self.image.get_rect(topleft = posicao)
        
        
class Background(pygame.sprite.Sprite):
    def __init__(self, imagem, grupo):
        super().__init__(grupo)
        self.image = imagem
        self.rect = self.image.get_rect(topleft = (0,0))
        