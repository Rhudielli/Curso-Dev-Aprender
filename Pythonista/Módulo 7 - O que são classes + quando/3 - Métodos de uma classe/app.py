# Metodos de uma classe -> Ligar, desligar e exibir dados do computador 
class Computador: 
    def __init__(self, marca, memoria_ram, placa_video) -> None:
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_video = placa_video
    def ligar(self):
        print('Estou ligando o computador')

    def desligar(self):
        print('Estou desligando o computador')

    def exibir_dados_computador(self):
        print(f'Computador da {self.marca}, com {self.memoria_ram} de memória ram e {self.placa_video} como placa de vídeo')
    
computador1 = Computador('Asus', '32gb', 'Nvidia')
computador1.ligar()
computador1.desligar()
computador1.exibir_dados_computador()

computador2 = Computador('Dell', '4gb', 'amd integrada')
computador2.ligar()
computador2.desligar()
computador2.exibir_dados_computador()
