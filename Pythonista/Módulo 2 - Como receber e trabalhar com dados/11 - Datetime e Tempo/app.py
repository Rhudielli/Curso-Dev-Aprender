from datetime import datetime

print(datetime.now())
print(datetime.now().microsecond)
print(datetime.now().second)
print(datetime.now().minute)
print(datetime.now().hour)
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

# Como criar uma data
lancamento_app = datetime(2021,5,28)
print(lancamento_app)

data_de_lancamento = datetime.strptime(input('Quando devemos lançar o aplicativo? '),'%d/%m/%Y')
print(type(data_de_lancamento))

# Como calcular o intervalo entre datas
data_atual = datetime.now()
prazo = data_de_lancamento - data_atual
print(prazo.days)

##########################################################################################################################################

# Desafio - Calcule quantos dias faltam até o seu aniversário

aniversario = datetime.strptime(input('Quando é meu aniversário? '),'%d/%m/%Y')
hoje = datetime.now()
dias = aniversario - hoje
print(f'Faltam {dias.days} para meu aniversário.')