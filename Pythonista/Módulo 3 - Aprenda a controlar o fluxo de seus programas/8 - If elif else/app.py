# if condição:
#    comandos a serem executados

# Trabalho terminado
trabalho_termidado = False
if trabalho_termidado == True:
    print('Bora dar uma saida!')
else:
    print('Não posso sair agora!')

# Chegar atrasado
numero_atrasos = 4
if numero_atrasos >= 3:
    print('Vá para a diretoria!')
elif numero_atrasos == 2:
    print('Essa é sua segunda falta!')
elif numero_atrasos == 1:
    print('Essa é sua primeira falta')
else: print('Pode entrar')

# A velocidade maxima para essa rua é de 50km

# * Cruzou entre 51km a 60km, levou multa de 2 pontos
# * Cruzou entre 61km a 75km, levou multa de 3 pontos
# * Cruzou acima de 75km, levou multa de 7 pontos

# Chaining
velocidade = 55
if velocidade <= 50:
    print('Não foi multado')
# elif velocidade >= 51 and velocidade <= 60:
elif 51 <= velocidade <= 60:
    print('Levou multa de 2 pontos')
elif velocidade >= 61 and velocidade <= 75:
    print('Levou multa de 3 pontos')
else:
    print('Levou multa de 7 pontos')

###############################################################################################################################################################

# Desafio 🥇

# Monte o seguinte cenário usando condicionais

# Você está montando um sistema para um salão de beleza para calcular o preço do corte de cabelos grandes que irá seguir as seguinte regras

# Disclaimer the haircut values are completely ficticious, I have no ideia of actual prices

# Se seu cabelo estiver com ou abaixo de 20cm você paga o valor de R$50,00

# Se seu cabelo estiver entre 21cm a 30cm você paga o valor de R$70,00

# Se seu cabelo estiver entre 31cm a 50cm você paga o valor de R$100,00

# Acima de 50cm Favor consultar na recepção

# Declare uma variável que represente o tamanho atual do cabelo

# Apenas imprima na tela a mensagem apropriada, nada além disso é necesário

tamanho_cabelo = 51
if tamanho_cabelo <= 20:
    print('Pagar R$ 50,00')
elif tamanho_cabelo >= 21 and tamanho_cabelo <= 30:
    print('Pagar R$ 70,00')
elif tamanho_cabelo >= 31 and tamanho_cabelo <= 50:
    print('Pagar R$ 100,00')
else:
    print('Favor consultar na recepção')

# Versão chaining
if tamanho_cabelo <= 20:
    print('Pagar R$ 50,00')
elif 21 and tamanho_cabelo <= 30:
    print('Pagar R$ 70,00')
elif 31 and tamanho_cabelo <= 50:
    print('Pagar R$ 100,00')
else:
    print('Favor consultar na recepção')
