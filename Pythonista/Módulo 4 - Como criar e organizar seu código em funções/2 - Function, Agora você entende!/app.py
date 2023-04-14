# Funções
# input()
# len()
# split()

# O que elas tem em comum? - Pegam uma funcionalidade acima, recebem alguns parametros e fazem algo internamente
 
# Uma função segue a seguinte sintaxe
def nome_função(parametros):
    pass

def dar_boas_vindas():
    print('Bem-vindo!')

dar_boas_vindas()

def dar_boas_vindas_personalizado(nome): # Poder ser adicionado mais parametros  idade, last...
    print(f'Bem-vindo(a) {nome}')

dar_boas_vindas_personalizado('Isaque')

# Valor padrão
def apresentar_lugar(horario_funcionamento, lugar='nossa loja'): # Caso tenha valor padrão (Lugar) deve ficar no final 
    print(f'Conheça {lugar}, horário de funcionamento das {horario_funcionamento}')

apresentar_lugar('8h as 18h','Castelo') # Caso coloque info, será substituida

###############################################################################################################################################################

# ​Desafio 🥇

# DESAFIO 1 - Crie uma função chamada gerar_nome_completo que recebe como parâmetro o nome e sobrenome de alguém e dá boas vindas para essa pessoa
def gerar_nome_completo(nome, sobrenome):
    print(f'Olá {nome} {sobrenome}, seja muito bem-vindo!')

gerar_nome_completo('Isaque', 'Rhudielli')

# DESAFIO 2 - # Crie uma função chamada calcular_valores que recebe 2 parâmetros o primeiro o preco de um produto e o segundo parâmetro é a quantidade, porém a quantidade deve haver um valor padrão de 1. Sua função deve exibir o resultado do preço do produto, multiplicado a quantidade escolhida.
def calcular_valores(preco, quantidade = 1):
    print(preco*quantidade)

calcular_valores(10, 2)