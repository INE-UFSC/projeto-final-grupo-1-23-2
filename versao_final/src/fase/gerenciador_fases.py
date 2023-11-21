import os
from src.fase.fase_nova import Fase

class GerenciadorFases:
    def __init__(self, screen):
        self.__screen = screen
        self.__fases = self.importa_csv('fases')
        self.__num_fase = 0
        self.__fase_atual = Fase(self.__fases[self.__num_fase], self.__screen)
        
    def importa_csv(self, caminho):
        fases = [fase for fase in os.listdir(caminho) if fase.startswith('fase')]
        
        csv_fases = {}
        
        for pasta in fases:
            csv_fase = {}
            caminho_pasta = os.path.join(caminho, pasta, 'csv')
            csv_arquivos = [os.path.join(caminho_pasta, arquivo) for arquivo in os.listdir(caminho_pasta) if arquivo.endswith('.csv')]
            
            for arquivo in csv_arquivos:
                nome_arquivo = os.path.splitext(os.path.basename(arquivo))[0][6:]
                csv_fase[nome_arquivo] = arquivo
            csv_fases[int(pasta[4:])] = csv_fase
        
        return csv_fases
    