# Loop while (laço while) / while = enquanto
tentativas = 0
while tentativas < 3:
    print('Tente novamnete')
    tentativas += 1

# Senha
senha = ''
while senha != '123456':
    senha = input('Digite sua senha: ')
print('Bem-vindo!')

# Receber nome do usuario
nome = ''
while nome == '':
    nome = input('Digite seu nome: ')
print(f'Bem-vindo! {nome}')

# Ver por do sol as 17h
horario = 0
while horario <= 17:
    print(horario)
    horario += 1
print('Hora de ir ver o por do sol')

# Contagem regressiva
contador = 100
while contador >= 0:
    print(contador)
    contador -= 1

###############################################################################################################################################################

# ​DESAFIOS 🥇

# DESAFIO 1 - Crie um loop while que irá contar e imprimir no console de 1 até 120
contar = 1
while contar <= 120: # ou < 121
    print(f' Número {contar}') # ou só contar
    contar += 1

# DESAFIO 2 - Crie um loop while que irá continuamente pedir ao usuário a senha para entrada, e só irá permitir o programa continuar caso ele digite a senha 'secreto'
senha = ''
while senha != 'secreto':
    senha = input('Digite novamente: ')
print('Certo! Vamos continuar')

# DESAFIO 3 - Crie um loop que conte e imprima na tela o valor em ordem descrescente de 100 para 1
regressiva = 100
while regressiva >= 1: # ou > 0
    print(regressiva)
    regressiva -= 1