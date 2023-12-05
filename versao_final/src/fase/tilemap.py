import pygame

class TileMap(pygame.sprite.Sprite):
    def __init__(self, posicao, imagem, grupo):
        super().__init__(grupo)
        self.__image = imagem # valores de x e y (iguais nesse caso)
        self.__rect = self.image.get_rect(topleft = posicao)
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    @property
    def image(self):
        return self.__image
    
    @property
    def rect(self):
        return self.__rect

        
        
class Background:
    def __init__(self, imagem, animado=False):
        self.__animado = animado
        self.__image = imagem
        self.__rect = self.image.get_rect(topleft = (0,0))
        self.__scroll = 0
        
    def draw(self, surface):
        if self.__animado:
            for i in range(2):
                surface.blit(self.image, (i * surface.get_width() + int(self.__scroll), 0))
            self.__scroll -=0.2
            if abs(self.__scroll) > surface.get_width():
                self.__scroll = 0
        else:
            surface.blit(self.image, self.rect)

    @property
    def image(self):
        return self.__image
    
    @property
    def rect(self):
        return self.__rect