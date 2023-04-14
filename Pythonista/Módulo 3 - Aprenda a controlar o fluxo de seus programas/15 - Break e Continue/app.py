# continue = ignorar/pular
for numero in range(100):
    if numero % 2 == 0:
        print(numero)
    else:
        continue

# break = para interromper a iteração
for numero in range(100):
    if numero % 2 == 0:
        print(numero)
    else:
        break

# lista
frutas = ['Maça','Manga','Laranja','Morango']
for fruta in frutas:
    if fruta == 'Laranja':
        break
    print(f'{fruta} adcionada a dieta')

###############################################################################################################################################################

# DESAFIOS 🥇

# Desafio 1

# Use a operação necessária (break ou continue) para que a seguinte condição aconteça.

# * Ao cegar ao estilo "Rap" o mesmo não deve ser impresso na tela

estilos = ['Hip-Hop','Rock','Rap','Pop']
for estilo in estilos:
    if estilo == 'Rap':
        continue
    print(estilo)

# Desafio 2 

# Use a operação necessária(braek ou continue) para que a seguinte condição aconteça:

# * Ao chegar ao estilo "Rock" a execução deve interrompida

for estilo in estilos:
    if estilo == 'Rock':
        break
    print(estilo)