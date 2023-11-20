import pygame

class HUD:
    def __init__(self, surface):
        #vida
        self.__coracao = pygame.image.load('Assets/ui/coracao.png').convert_alpha()
        self.__coracao = pygame.transform.scale(self.__coracao, (64,64))
        self.__vidas = []

        #chave
        self.__chaveApagada = pygame.image.load('Assets/ui/chaveApagada.gif').convert_alpha()
        self.__chaveApagada = pygame.transform.scale(self.__chaveApagada, (120,120))
        self.__chave = pygame.image.load('Assets/ui/chave.png').convert_alpha()
        self.__chave = pygame.transform.scale(self.__chave, (120,120))


        self.__superficie = surface
       # self.__num_vidas = num_vidas
        #self.__indicador_chave = indicador_chave
        #self.__num_fase = num_fase
    
    

    def mostrar_vida(self, vidas):
        for i in range(vidas):
            x = i*70
            self.__vidas.append(self.__superficie.blit(self.__coracao, (x,10)))
        #self.__superficie.blit(self.__coracao, (20,10))
        pass

    def mostrar_chave(self, indicador_chave: bool):
        if indicador_chave == False:
            self.__superficie.blit(self.__chaveApagada,(20,60))
        else:
            self.__superficie.blit(self.__chave,(20,60))
        pass
        





    def num_vidas(self):
        return self.__num_vidas
    
    @property
    def indicador_chave(self):
        return self.__indicador_chave
    
    @property
    def num_fase(self):
        return self.__num_fase
    
    def draw(self):
        pass