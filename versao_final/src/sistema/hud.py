import pygame

class HUD:
    def __init__(self, surface):
        #vida
        self.__coracaoVazio = pygame.image.load('assets/UI/HUD/coracao_vazio.png').convert_alpha()
        self.__coracaoVazio = pygame.transform.scale(self.__coracaoVazio, (64,64))
        self.__coracao = pygame.image.load('assets/UI/HUD/coracao.png').convert_alpha()
        self.__coracao = pygame.transform.scale(self.__coracao, (64,64))
        self.__vidas = []

        #chave
        self.__chaveApagada = pygame.image.load('assets/UI/HUD/chave transparente.png').convert_alpha()
        self.__chave = pygame.image.load('assets/tiles/chave/chave1.png').convert_alpha()


        self.__superficie = surface
    

    def mostrar_vida(self, vidas):
        for i in range(vidas):
            x = i*50
            self.__vidas.append(self.__superficie.blit(self.__coracao, (x,10)))
        if vidas != 5:
            
            #self.__vidas[4] = self.__superficie.blit(self.__coracaoVazio, (4*50,10))
            for i in range(5 - vidas):
                self.__vidas[i+vidas] = self.__superficie.blit(self.__coracaoVazio, ((vidas+i)*50,10))

        #self.__superficie.blit(self.__coracao, (20,10))
        pass

    def mostrar_chave(self, indicador_chave: bool):
        if indicador_chave == False:
            self.__superficie.blit(self.__chaveApagada,(270,8))
        else:
            self.__superficie.blit(self.__chave,(270,8))
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