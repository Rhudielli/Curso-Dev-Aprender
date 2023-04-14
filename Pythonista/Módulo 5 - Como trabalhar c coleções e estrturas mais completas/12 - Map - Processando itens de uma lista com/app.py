# Como podemos criar listas?

# 1. Criar listas usando range()
numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)


# 2. Criar listas usando Map
nomes = ['larissa', 'rafael', 'marcus', 'john']
def aprovar_pessoa(nome): # Pode fazer lógica mais complexa
    return nome + ' APROVADO'

print(list(map(aprovar_pessoa, nomes)))