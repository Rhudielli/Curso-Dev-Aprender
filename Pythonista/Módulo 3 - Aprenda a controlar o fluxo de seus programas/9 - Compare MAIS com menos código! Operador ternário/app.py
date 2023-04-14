# Caso a idade seja maior ou igual a 18 anos, essa pessoa é maior de idade, caso contrário ela é menor de idade
idade = 15
if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')

# Expressão condicional / Operador ternario

# expressao > if > cindicao > else > expressao
idade = 25
print('Maior de idade') if idade >= 18 else print('Menor de idade')

possiu_passaporte = True
print('Favor embarcar') if possiu_passaporte else print('Favor tirar passaporte')

###############################################################################################################################################################
# Desafio 

# Use a expressão condicional (operador ternário) para criar a seguinte condição

# Se a velocidade estiver acima de 100, exibir: "Você foi multado". Caso contrario exiba siga em frente.

velocidade = 100
print('Você foi multado') if velocidade >= 100 else print('Siga em frente')