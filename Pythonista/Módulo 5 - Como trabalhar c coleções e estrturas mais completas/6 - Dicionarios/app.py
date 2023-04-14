# Pessoa
#     nome
#     idade
#     altura

# Lista comum
pessoa = ['Carol', 18, 1.60, 'Mike', 50, 1.80]

# Dicionário (chave > valor)
dicionario_pessoa = {'nome': 'Carol', 'idade': 18, 'altura': 1.60} # Use strings, e não números (int) para identidificar os valores
print(dicionario_pessoa.keys()) # Apenas chaves
print(dicionario_pessoa.values()) # Apenas valores
print(dicionario_pessoa.items()) # Par de chave e valor

# Iterar sobre um dicionário
for item in dicionario_pessoa.items():
    print(item)
    print(item[1])

# Outra maneira de criar dicionário
pessoa_2 = dict(nome='Carol', idade=18, altura=1.60)
print(pessoa_2['idade'])