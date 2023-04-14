# Trabalhando com Multiplas Listas

from itertools import zip_longest

#########################################################################
a_lista = ['A','B','C','D','E']
b_lista = [1, 2, 3, 4, 6]

for a, b in zip(a_lista, b_lista):
    print(a)
    print(b)

#########################################################################
produtos = ['produto 1','produto 2','produto 3','produto 4','produto 5']
precos = [250, 150, 220, 550, 50]

for a, b in zip(produtos, precos):
    print(f'Salvando produto {a} com valor de R$ {b}')

#########################################################################
titulos = ['Titulo 1','Titulo 2','Titulo 3','Titulo 4',]
descricoes = ['Descricao 1','Descricao 2','Descricao 3']

for titulo, descricao in zip_longest(titulos, descricoes):
    print(f'Encontramos o {titulo} com a descrição: {descricao}')

###############################################################################################################################################################

# ​DESAFIOS 🥇

## DESAFIO 1

# Usando as listas abaixo:

produtos = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4', 'Produto 5']
precos = ['R$500,00', 'R$1500,00', 'R$2700,00', 'R$5000,00']

# Estamos extraindo preços de um site de produtos e queremos armazenar as informações encontradas, porém a pesquisa foi encontrada em momentos diferentes, assim acabamos com duas listas diferentes, favor criar uma mensagem que diz o nome e valor produto, como as mensagens abaixo:

for produto, preco in zip_longest(produtos, precos):
    print(f'Produto: {produto} encontrado no valor de R$ {preco}')

# Produto: Produto 1 encontrado no valor de R$500,00

# Produto: Produto 2 encontrado no valor de R$1500,00

# Produto: Produto 3 encontrado no valor de R$2700,00

# Produto: Produto 4 encontrado no valor de R$5000,00

# Produto: Produto 5 encontrado no valor de None