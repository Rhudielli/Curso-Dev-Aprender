""" def exibir_preco(*, nome_produto, preco):
    print(f'{nome_produto} está no valor de: {preco}')

# Argumentos posicionais
exibir_preco('Iphone', 5000)
exibir_preco(nome_produto='Iphone', preco=5000)

# Argumentos nomeados
exibir_preco(preco=5000, nome_produto='Iphone') """

###############################################################################################################################################################

# Desafio 🥇


# Crie uma função chamado gerar_objeto_personalizado que irá receber 3 parâmetros, cor, altura, formato.

# A sua função deve apenas imprimir na tela o que foi passado para ela, nada mais, nada menos.

# Porém ela deve seguir as seguintes regras:

# 1 - O primeiro argumento deve ser posicional

# 2 - Os argumentos altura e formato precisam OBRIGATORIAMENTE serem nomeados

def gerar_objeto_personalizado(cor, *, altura, formato):
    print(cor, altura, formato)

gerar_objeto_personalizado('Azul', altura = 1.70, formato = 'quadrado')