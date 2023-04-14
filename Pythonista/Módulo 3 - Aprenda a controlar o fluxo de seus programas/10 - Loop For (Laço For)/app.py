for numero in range(1, 30, 2): # ou (5 + 1) / terceiro parametro - step (pula o valor inserido)
    print('Carrgando', numero)

nomes = ['jeff', 'carl', 'jean', 'luke']
for nome in nomes:
    print(nome)

# excercicio de fixação
carros = ['206', '207', '307', '308']
for carro in carros:
    print(carro)
# ou
y = ['206', '207', '307', '308']
for x in y:
    print(x)

###############################################################################################################################################################

# Desafios 

# 1 - Usando um loop, exiba na tela: Estamos em X onde X é um valor iniciando em 18 e finalizando em 110
for numero in range(18, 110 + 1): # ou (18, 111)
    print(numero)

# 2 - Você precisa de 10 passos para finaliazar uma tarefa, exiba na tela, usando loop for a seguinte frase 'Realizando passo X'
for passo in range(1, 11): # ou (1, 10 + 1)
    print(f'Realizando passo {passo}')