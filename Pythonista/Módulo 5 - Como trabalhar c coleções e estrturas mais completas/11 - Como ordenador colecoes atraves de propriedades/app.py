from operator import itemgetter

""" nomes = ['Zack','Camilla','julius','Romer']
valores = [31, 23, 6, 36, 21, 33, 37, 7, 20, 23]

pessoas = [
    {'nome': 'Jonh', 'idade': 32, 'nivel_acesso': 2},
    {'nome': 'Carol', 'idade': 18, 'nivel_acesso': 3},
    {'nome': 'Thomas', 'idade': 45, 'nivel_acesso': 5},
    {'nome': 'Amanda', 'idade': 23, 'nivel_acesso': 1}
]

pessoas.sort(key=itemgetter('idade'))
print(pessoas)


produtos = [
    ('celular', 750),
    ('bicicleta', 1500),
    ('microfone', 550)
]

produtos.sort(key=itemgetter(0), reverse=True)
print(produtos)


matriz = [[5, 10], [15, 21], [1, 5]]
matriz.sort(key=itemgetter(1))
print(matriz) """

###############################################################################################################################################################

# DESAFIO 🥇

# Ordene a lista de produtos abaixo pelo preço em ordem crescente
produtos = [
    {'nome': 'Celular', 'preco': 1500},
    {'nome': 'Monitor', 'preco': 500},
    {'nome': 'Microfone', 'preco': 300}
]

produtos.sort(key=itemgetter('preco'))
print(produtos)

# Ordene em ordem descrescente a lista de equipamento_filmagem por valor do equipamento
equipamento_filmagem = [
    ('Tripé', 300),
    ('Câmera', 1700),
    ('Iluminação', 200),
]

equipamento_filmagem.sort(key=itemgetter(1), reverse=True)
print(equipamento_filmagem)

# Ordene em ordem crescente a cotacao_moedas com base no valor da moeda

cotacao_moedas = [['usd', 5.25], ['brl', 1.56], ['eur', 6.47]]
cotacao_moedas.sort(key=itemgetter(1))
print(cotacao_moedas)