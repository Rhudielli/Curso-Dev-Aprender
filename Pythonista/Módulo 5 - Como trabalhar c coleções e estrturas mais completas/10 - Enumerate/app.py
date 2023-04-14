# Enumerate

""" for indice, numero in enumerate(range(1, 11), 1):
    print(indice, numero)
    if indice == 5:
        print('Estamos na metade da lista')

nomes = ['nome1','nome2','nome3','nome4','nome5']

for indice, nome in enumerate(nomes, 1):
    print(indice, nome)
    if indice == 3:
        print('Isaque') """

###############################################################################################################################################################

# DESAFIOS 🥇

# Desafio 1
#     Itere sobre a lista abaixo exibindo o número de índice + nome da fruta. Porém quando o índice for 3 exiba 'N° índice + nome da fruta EM PROMOÇÃO'

frutas = ['Maça', 'Laranja', 'Morango', 'Limão']

for indice, fruta in enumerate(frutas, 0):
    if indice == 3:
        print(f'{indice} {fruta} EM PROMOÇÃO')
    else:
        print(indice, fruta)

# Excercicio de fixação
carros = ['206','208','307','308']

for indice, carro in enumerate(carros, 0):
    if indice == 0:
        print(f'{carro}, é o projeto que vou montar')
    else:
        print(indice, carro)