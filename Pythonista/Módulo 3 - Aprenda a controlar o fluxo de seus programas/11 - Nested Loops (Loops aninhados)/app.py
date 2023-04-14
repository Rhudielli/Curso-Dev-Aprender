# Loop Aninhados
# País + Estação
paises = ['brasil','india','estados unidos']
estacoes_ano = ['primaveira','verão','outono','inverno']
for pais in paises:
    for estacao in estacoes_ano:
            print(f'{estacao} {pais}')

for x in range(1,11): # Externo
      for y in range(1,6): # Interno
            print(f'Valor externo de {x} e interno de {y}')

###############################################################################################################################################################

# Desafio

# Imprima na tela a marca + celular de todos os celulares, usando as informações abaixo

celulares = ['Asus','Samsung','Sony','Apple']
versoes = ['Plus','Premium Plus','Premuim Deluxe','Plus Premuim Ultra']

for celular in celulares:
      for versao in versoes:
            print(celular, versao)