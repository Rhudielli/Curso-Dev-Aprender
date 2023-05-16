# Polimorfismo
print(10 + 20) # O (+) é polimorfismo
print('Olá' + ' Dev')

print(len('Livro'))
print(len([25, 20, 30]))
print(len({'Título': 'Livro1', 'Lançamento': '2010', 'Categoria': 'Lifestyle'}))

# Polimorfismo em Funções
class Carro:
    def ligar(self):
        print('Ligando o carro')
    
class Moto:
    def ligar(self):
        print('Ligando a moto')

def iniciar(veiculo):
    veiculo.ligar()

carro = Carro()
moto = Moto()

iniciar(carro)
iniciar(moto)

# Versões diferentes da mesma função

class Pessoa:
    def apresentar(self, nome, idade=None, profissao=None):
        print(nome)
        if idade and profissao != None:
            print(f'{nome}, {idade}, {profissao}')
        elif idade != None:
            print(f'{nome}, {idade}')
        elif profissao != None:
            print(f'{nome}, {profissao}')
        else:
            print(nome)



pessoa = Pessoa()
pessoa.apresentar(nome= 'Amanda', idade=18, profissao='Programadora')
pessoa.apresentar(nome= 'Amanda', idade=18)
pessoa.apresentar(nome= 'Amanda', profissao='Programadora')
pessoa.apresentar(nome= 'Amanda')