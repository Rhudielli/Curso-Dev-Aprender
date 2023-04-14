from datetime import datetime

def depositar_dinheiro():
    print('Depositando dinheiro')
    
    def despositando_dolar():
        print('Depositando dolares')

    def depositando_reais():
        print('Despositando reais')

    despositando_dolar()
    depositando_reais()

###############################################################################################################################################################

def pai(numero):
    def filho_1():
        print('Sou filho 1')
    def filho_2():
        print('Sou filho 2')
    if numero == 1:
        return filho_1

resultado = pai(1)
resultado()

###############################################################################################################################################################

# Decorators
def meu_decorator(funcao):
    def wrapper():
        print('Antes')
        funcao()
        print('Depois')
    return wrapper
@meu_decorator
def parabenizar():
    print('Parabéns!!!!')

parabenizar()

# resultado = meu_decorator(parabenizar)
# resultado()

###############################################################################################################################################################

# DESAFIOS

# Desafio 1
# Crie um decorador que irá pegar a função que for passado para ele e imprima o horário atual antes de executar a função e depois imprimir o horário após ter finalizado a execução da função.
#     Dica: você terá que usar o módulo datetime para conseguir o horário atual.

# Desafio da aula
def monitorar_horario(funcao):
    def monitor():
        print(datetime.now())
        funcao()
        print(datetime.now())
    return monitor

@monitorar_horario
def baixar_musicas():
    print('Baixando musicas')

baixar_musicas()

##############################

# Desafio de compreensão 1
def comprar_carro(trabalhar):
    def dinheiro():
        print('Trabalhando')
        trabalhar()
        print('Comprando 206')
    return dinheiro

@comprar_carro
def comprar_moto():
    print('Comprando FZ25')

comprar_moto()

# Desafio de compreensão 2
def viajar(liberdade):
    def ingles():
        print('Desenvolvendo')
        liberdade()
        print('Viajando')
    return ingles

@viajar
def estudar_ingles():
    print('Falando Inglês')

estudar_ingles()