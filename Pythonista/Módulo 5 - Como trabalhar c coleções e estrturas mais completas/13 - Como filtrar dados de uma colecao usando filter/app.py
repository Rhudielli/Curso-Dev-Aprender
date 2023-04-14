nomes = ['larissa','rafael','marcus','john']

def pessoa_aprovada(pessoa):
    if pessoa == 'marcus':
        return True
    else:
        return False

print(list(filter(pessoa_aprovada, nomes)))
print(list(map(pessoa_aprovada, nomes)))

# Filter
pinturas = [
    ['Pintura Classica', 'Azul', 1857],
    ['Pintura Medieval', 'Vermelha', 1867],
    ['Pintura Moderna', 'Verde', 1897],
]

def e_antiguidade(pintura):
    if pintura[2] < 1890:
        return True
    else:
        return False

print(list(filter(e_antiguidade, pinturas)))
print(list(map(e_antiguidade, pinturas)))

###############################################################################################################################################################

# DESAFIO 1 🥇

# Usando a lista abaixo, filtre apenas as vagas com salário acima de R$2500
vagas = [
    ['vaga 1', 1200],
    ['vaga 2', 2550],
    ['vaga 3', 5000]
]

def salario(valor):
    if valor[1] > 2500:
        return True
    else:
        return False
    
print(list(filter(salario, vagas)))
print(list(map(salario, vagas)))


# Exercicio de fixação
carros = [
    ['BMW', 'M4'],
    ['Mercedes', 'c63s'],
    ['Audi', 'RS5'],
]

def marcas(modelo):
    if modelo[1] == 'c63s':
        return True
    else:
        return False
    
print(list(filter(marcas, carros)))
print(list(map(marcas, carros)))