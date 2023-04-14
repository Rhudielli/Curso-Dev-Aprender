idade = 21
possui_convite = False
filho_do_dono = True
print((idade >= 21) and (possui_convite == True))
print(idade >= 21 or possui_convite == True)

# Entrar na festa caso - Maior que 21 e Possui convite ou Seja filho do dono
print((idade > 21 and possui_convite == True) or (filho_do_dono == True))

# Pode trabalhar caso - Maior de idade e possiur carteira de trabalho
maior_de_idade = True
possiu_carteira_trabalho = True
trabalha_atualmente = True
possui_veiculo_proprio = False

# Queremos contratar pessoas que não possuam veículo prórprio, mas já possuam carteira de trabalho
print(True and True)
print(maior_de_idade == True and possiu_carteira_trabalho == True)
print(possui_veiculo_proprio == False and not possiu_carteira_trabalho == True)

# Operadores Significado
#  ()   = Parenteses
#  **   = Expoente
#  *    = Multiplicação
#  /    = Divisão
#  //   = Divisão por inteiros
#  %    = Modulus
#  +,   = Adição, subtração
#  not  = NOT booleano
#  and  = AND booleano
#  or   = OR booleano
#  ==, !=, >,
#  <, >=,<=,
# is, is not,
# in, not in = Compadores lógicos, identidade, pertencimento em conjuntos

###############################################################################################################################################################

# ​Desafio 🥇


# Quero que você defina as seguintes variáveis, inicialmente todas como False, a ideia aqui não é de se importar com os valores dentro dessas variáveis, mas sim como montar condicionais.

possui_passaporte = True

passagem_comprada = True

menor_de_idade = False

# E Crie as seguintes condições usando o que acabou de ver e imprima o resultado na tela. Tente fazer cada condição e depois veja a solução no final deste aula.

# Uma pessoa só pode viajar se possuir passaporte e tiver a passagem comprada e não for menor de idade
print((possui_passaporte and passagem_comprada) and not menor_de_idade)

# Uma pessoa só pode viajar se possuir passaporte ou tiver a passagem comprada e não for menor de idade
print((possui_passaporte or passagem_comprada) and not menor_de_idade)

# Uma pessoa só pode viajar se não possuir passaporte ou tiver a passagem comprada e não for menor de idade
print((not possui_passaporte or passagem_comprada) and not menor_de_idade)

# Uma pessoa não pode viajar se não possuir passaporte ou não tiver a passagem comprada e for menor de idade
print((possui_passaporte or not passagem_comprada) and menor_de_idade)