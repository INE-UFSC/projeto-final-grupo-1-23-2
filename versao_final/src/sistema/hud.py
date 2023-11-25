import pygame

class HUD:
    def __init__(self, surface, vida_max):
        #vida
        self.__coracaoVazio = pygame.image.load('assets/UI/HUD/coracao_vazio.png').convert_alpha()
        self.__coracao = pygame.image.load('assets/UI/HUD/coracao.png').convert_alpha()
        self.__vidas = []

        #chave
        self.__chaveApagada = pygame.image.load('assets/UI/HUD/chave transparente.png').convert_alpha()
        self.__chave = pygame.image.load('assets/tiles/chave/chave1.png').convert_alpha()
        
        self.__vida_max = vida_max
        self.__superficie = surface
    

    def mostrar_vida(self, vidas):
        mortes = self.__vida_max - vidas
        
        for i in range(vidas):
            x = i*50
            self.__vidas.append(self.__superficie.blit(self.__coracao, (x,10)))
            
        for i in range(mortes):
            self.__vidas[i+vidas] = self.__superficie.blit(self.__coracaoVazio, ((vidas+i)*50,10))


    def mostrar_chave(self, indicador_chave: bool):
        localizacao_x = (self.__vida_max * 50) + 10
        
        if indicador_chave == False:
            self.__superficie.blit(self.__chaveApagada,(localizacao_x,8))
        else:
            self.__superficie.blit(self.__chave,(localizacao_x,8))
        pass
        

    def render(self, vidas, indicador_chave):
        self.mostrar_vida(vidas)
        self.mostrar_chave(indicador_chave)


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