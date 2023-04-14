valores = [1, 2, 3, 4, 2, 5, 6, 8, 9, 10, 2]
anos = [2020, 2030, 2040, 2020]

# Para adicionar ao final da lista
valores.append(11)
print(valores)

# Unir listas
valores.extend(anos)
print(valores)

# Adicionar lista
nova_lista = valores + anos
print(nova_lista)

# Acessar valor dentro da lista
print(anos[1])

# Inserir valor
anos.insert(2, 2031)
print(anos)

# Extrair com base no indice
anos_2020 = anos.pop(0)
print(anos_2020)

# Remover item da lista
anos.remove(2040)
del anos[2]
print(anos)

# Remover faixa de valores
del valores[1:6]
print(valores)

# Contando a ocorrencia de um valor
print(valores.count(2))


# Resetar
valores.clear()
print(valores)