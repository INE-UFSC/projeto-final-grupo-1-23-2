import os

class ReaderCSV:
    def __init__(self, caminho):
        self.__fases = self.ler_csv(caminho)
        
    def ler_csv(self, caminho):
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
    
reader = ReaderCSV('fases')