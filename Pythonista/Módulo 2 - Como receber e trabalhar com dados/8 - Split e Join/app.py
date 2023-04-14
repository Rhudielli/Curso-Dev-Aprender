frase = 'Olá, bem-vindo a este treinamento!'
print(frase.split())
print(frase.split(','))
print(frase.split('-'))

nomes = 'Jhonatan, rafael, carol, amanda,jefferson'
print(nomes.split())
print(nomes.split(','))

hashtags = 'music #guitar #gamer #coder #python'
print(hashtags.split())
print(hashtags.split('#'))
print(hashtags.split('#',3))

# Como concatenar (combinar) strings
hashtags_separadas_por_espacos = hashtags.split(' ')
print(hashtags_separadas_por_espacos)
print(','.join(hashtags_separadas_por_espacos))
print('.'.join(hashtags_separadas_por_espacos))
print(' '.join(hashtags_separadas_por_espacos))

##########################################################################################################################################

# Desafios 

frase1 = 'Desafio manipulação de strings'
frase2 = 'jhonatan,rafael,carol,camilla'

# Desafio 1: Transforme a frase1 em uma lista de palavras e guarde o resultado em uma variável chamada palavras1
palavras1 = frase1.split()

# Desafio 2: Trasnforme a frase2 em uma lista de palavras e guarde o resultado em uma variável chamada palavras2
palavras2 = (frase2.split(','))

# Desafio 3: Pegue o palavras1 e trasnforme elas no seguinte string: "Desafio,manipulação,de,strings". Imprima no console.
print(','.join(palavras1))

# Desafio 4: Pegue o palavras2 e trasnforme elas no seguinte string: "jhonatan & rafael & carol & camilla". Imprima no console.
print(' & '.join(palavras2))