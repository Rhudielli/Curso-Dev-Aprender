# Listas
preco_1 = 10
preco_2 = 20
preco_3 = 30

# print(precos[2]) # Indice
precos = [10, 20, 30, 40, 50, 60, 100, 250, 560, 23, 74]
print(precos[precos.index(100)])

# Listas no python são dinamicas (aceitam qualquer tipo de dado)
itens = [1, 3, 6, 'Olá', 'Café', True, 10.6]
print(itens[4])

# Maneiras diferentes de gerar uma lista
# Multiplicação de valores (repetição)
lista_9 = [9] * 10
print(lista_9)
lista_20 = ['Isaque'] * 20
print(lista_20)

# Usando gerador range (Sequencia)
# 1 até 29
faixa_numeros = list(range(30))
print(faixa_numeros)

# Gerar a partir de strings
print(list('Bem-vindo ao treinamento'))

# Lista de lista (matriz)
matiz_nomes = [['Carol', 30],['Marcus', 50]]
print(matiz_nomes[0])
print(matiz_nomes[1][1])

###############################################################################################################################################################

# Desafios 🥇


# Desafio
    # 1 Crie uma lista que tenha os nomes dos 3 objetos que você mais usa durante o dia e imprima ele na tela

objetos = ['Notebook', 'Celular', 'Desodorante']

# Desafio
   # 2 Usando apenas uma linha de código, crie uma lista de 10 a 131

numbs = (list(range(10, 131 + 1)))

# Desafio
    # 3 Imprima na tela o resultado da combinação da lista do desafio 1 e desafio 2

print(objetos, numbs)

# Desafio
   # 4 Crie uma lista de listas (matriz) que tenha os nomes dos 3 objetos que você mais usa durante o dia, mas agora dentro de cada item você vai colocar uma informação extra, coloque o valor em reais desse objeto também e imprima ele na tela

matriz = [['Notebook', 3.000],['Celular', 1.000],['Desodorante', 12,90]]
print(matriz[0])