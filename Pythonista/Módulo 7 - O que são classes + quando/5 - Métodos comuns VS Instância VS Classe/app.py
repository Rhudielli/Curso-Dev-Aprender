# Métodos comuns ✅
# Métodos de Classe(Class Methods) ✅
# Métodos de estáticos(Static Methods)

# Métodos comuns
class Computador:
    sistema_operacional = 'Windows 10'

    def __init__(self, marca, memoria_ram, placa_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_video = placa_video

    def exibir_dados_computador(self):
        print(self.marca, self.memoria_ram, self.placa_video, self.sistema_operacional)
    
    # Métodos de Classe(Class Methods)
    @classmethod
    def computador_escritoiro(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de vídeo - Baixo Custo')
    
    @classmethod
    def computador_pesado(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de vídeo - Alto Custo')
    
    # Métodos de estáticos(Static Methods)
    @staticmethod
    def roda_programas_pesados(memoria_ram):
        if memoria_ram >= 8:
            return True
        else:
            return False
        

# Métodos de Classe(Class Methods)
####################################
# Configuração p/ cliente de escritótio
computador1 = Computador.computador_escritoiro('8gb')

# Configuração p/ cliente de trabalho pesado (Jogos, edição vídeo, modelagem 3d)
computador2 = Computador.computador_pesado('16gb')

computador1.exibir_dados_computador()
print('########')
computador2.exibir_dados_computador()
print('########')



# Métodos de estáticos(Static Methods)
print(Computador.roda_programas_pesados(7))