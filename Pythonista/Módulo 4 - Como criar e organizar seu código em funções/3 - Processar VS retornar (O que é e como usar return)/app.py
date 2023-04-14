# Processar VS Retornar

# Função que apenas processa dados
# print('Olá')

# Funções que retornam dados
# cidade = input('Qual é a sua cidade?')

# Como escolher entre funções que processam VS retornam dados?
# Depende, Eu vou precisar usar essa informação na lógica do meu programa ainda? Ou só preciso processar esse dado, irei utilizar ele depois?

# Processa dados
def exibir_cotacao_dia(moeda):
    if moeda == 'usd':
        print(5.47)

exibir_cotacao_dia('usd')

# Retorna dados
def obter_cotacao_dia(moeda):
    if moeda == 'usd':
        return 5.47

cotacao = obter_cotacao_dia('usd')
if cotacao > 5:
    print('Investir em ações americanas')
else:
    print('Cotação não favorável')