# Valores aleatórios com random
import random

print(random.random()) # Gera um valor de 0.0 a 1.0

# Gera um valor DECIMAL de Valor minimo ao Valor maximo
print(random.uniform(4, 10))

# Gera um valor INTEIRO de Valor minimo ao Valor maximo
print(random.randint(4, 10))

# Escolher opção aleatória
cores = ['verde','vermelho','azul']
print(random.choices(cores, k=2))

# Embaralhar uma lista
cartas_de_um_baralho = ['carta1','carta2','carta3','carta4']
print(random.shuffle(cartas_de_um_baralho))
print(cartas_de_um_baralho)

##########################################################################################################################################

# Desafios 

# Desafio 1 - Simular a opção de jogar uma moeda e resultar em cara ou coroa. Jogue as opções dentro de uma lista e depois crie um programa que imprime cara ou coroa na tela.

moeda = ['cara','coroa']
print(random.choice(moeda))

# Desafio 2 - Fazer um sorteio entre 5 nomes em uma lista de nomes. Crie uma lista de 5 nomes e sorteie um nome dentro dessa lista exiba na tela

nomes = ['Vitória','Elaine','Larissa','Jéssica','Nathalin']
print(random.choice(nomes))

# Desafio 3 - Escolher aleatóriamente um número de 10-100. Imprima na tela um valor aleatório entre 10 e 100

print(random.randint(10, 100))