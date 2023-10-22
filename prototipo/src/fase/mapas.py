class Mapa():
    def __init__(self):
        self.__mapa = [ # agora os mapas estão 20x12
                [
                    '                    ',
                    '                    ',
                    '                    ', 
                    '                    ', 
                    '                    ',
                    '            C       ',
                    '           XXX      ',
                    '        X   Z       ',
                    'P   XXX  D Z        ',
                    'XXXXXXXXXXXXXXXXXXXX',
                    'XXXXXXXXXXXXXXXXXXXX',
                    'XXXXXXXXXXXXXXXXXXXX'
                ],
                [
                    '                    ',
                    '                    ',
                    '                    ',
                    '                    ',
                    '                    ',
                    'bbb                 ',
                    'bDb                 ',
                    'XXX   X             ',
                    'P    XX   X C  B    ',
                    'XXXXXXXXXXXXXXXXXXXX',
                    'XXXXXXXXXXXXXXXXXXXX',
                    'XXXXXXXXXXXXXXXXXXXX'
                ],
                [
                    '                    ', 
                    '                    ',
                    '                    ',
                    '                    ', 
                    'P                   ',
                    'XXX                 ',
                    '      X             ',
                    '  XD    X           ',
                    '   X      X C  B    ',
                    'XXXXXXXXXXXXXXXXXXXX',
                    'XXXXXXXXXXXXXXXXXXXX',
                    'XXXXXXXXXXXXXXXXXXXX'
                ]
            ]
        
        self.__tamanho_tile = 64
        self.__largura_tela = self.__tamanho_tile*16
        self.__altura_tela = len(self.__mapa[0])*self.__tamanho_tile
        
    @property
    def mapa(self):
        return self.__mapa
        
    @property
    def largura_tela(self):
        return self.__largura_tela
    
    @property
    def altura_tela(self):
        return self.__altura_tela
    
    @property
    def tamanho_tile(self):
        return self.__tamanho_tile
