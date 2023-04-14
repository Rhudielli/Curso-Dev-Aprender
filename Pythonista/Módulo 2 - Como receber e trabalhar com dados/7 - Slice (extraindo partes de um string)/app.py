""" teclado = 'sdxcfvgbhhjnkmkkmjnhbrgvcfdxzsdxfcgvhbjnkm'
          #0123456
print(teclado[21])
print(teclado.index('r'))
print(teclado[teclado.index('r')])

# Acessando partes de um string
link = 'facebook.com/devaprender'
print(link[0])
print(link[-1])
print(link[0:5])
print(link[0:])
print(link[-5:])
print(link[5:])
print(link[:-5])

frase = 'Clean Code'
print(frase.rindex('C')) """

##########################################################################################################################################

# Desafio 1 - Encontre o índice de 'o' dentro da variável biblioteca

biblioteca = 'Biblioteca'
print(biblioteca.rindex('o'))

# Desafio 2 - Usando a frase Desenvolvimento de Aplicações, imprima apenas (de Aplicações)

frase = 'Desenvolvimento De Aplicações'
print(frase[16:])

# Correção pelo professor

print(biblioteca.index('o'))

indice_d = frase.rindex('D')
indice_s = frase.rindex('s')
print(frase[indice_d:indice_s+1])