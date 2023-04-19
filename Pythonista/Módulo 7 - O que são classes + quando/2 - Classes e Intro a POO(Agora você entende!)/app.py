# Código solto
marca = input('Digite a marca do seu computador: ')
memoria = input('Digite a quantidade de memória ram: ')
placa = input('Digite o nome da placa de vídeo: Lenovo')

print(f'Seu computador é da marca: {marca}')
print(f'Seu computador possui {memoria} de memória')
print(f'Seu computador possui uma placa de vídeo: {placa}')

# Funções
def exibir_informacoes_computador():
    marca = input('Digite a marca do seu computador: ')
    memoria = input('Digite a quantidade de memória ram: ')
    placa = input('Digite o nome da placa de vídeo: ')

    print(f'Seu computador é da marca: {marca}')
    print(f'Seu computador possui {memoria} de memória')
    print(f'Seu computador possui uma placa de vídeo: {placa}')

exibir_informacoes_computador()

# Classes
class Computador: 
    def __init__(self, marca, memoria_ram, placa_video) -> None:
        self.marca = marca  # Pode usar valor estatico ('Lenovo')
        self.memoria_ram = memoria_ram
        self.placa_video = placa_video

# marca , memória ram, placa de vídeo
computador1 = Computador('Asus', '8gb', 'NVIDIA')
print(computador1.marca)
print(computador1.memoria_ram)
print(computador1.placa_video)