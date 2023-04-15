# COMO CRIAR E MODIFICAR ARQUIVOS PYTHON

# 'a'  - Usado para acrescentar algo
# 'r'  - Usado somente para ler algo
# 'r+' - Usado para ler e escrever algo
# 'w'  - Usado somente para escrever algo

import os

with open('celulares.txt', 'w') as arquivo:
    arquivo.write('Celular 2')

nomes = ['Lucas', 'Carol', 'Jeff', 'Douglas']
numeros = [1, 2, 3, 5, 6]

with open('numeros.txt', 'a', newline='') as arquivo:
    for numero in numeros:
        arquivo.write(str(numero) + os.linesep)

with open('nomes.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)

with open('numeros.txt', 'r+') as arquivo:
    for numero in arquivo:
        print(numero)
    arquivo.write('9000')

###############################################################################################################################################################

# Desafio resolvido na próxima pasta