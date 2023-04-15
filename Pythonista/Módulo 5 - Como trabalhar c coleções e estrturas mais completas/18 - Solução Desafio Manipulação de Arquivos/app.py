import os

# DESAFIO 🥇

# 🥇 DESAFIO Manipulação de Arquivos🥇

# Primeiro crie 3 listas
#     * Uma lista que contem 5 frutas
#     * Uma lista que contem 5 cores
#     * Uma lista que contem 5 linguagens de programação

frutas = ['Maça', 'Banana', 'Manga', 'Melancia', 'Pera']
cores = ['Azul', 'Amarelo', 'Laranja', 'Verde', 'Vermelho']
programacao = ['Python', 'JavaScript', 'Java', 'Ruby', 'C++']

# Desafio 1 - Crie um novo arquivo chamado frutas.txt e insira dentro dele todos as 5 frutas que estão na lista de frutas

# Resolvido por mim
with open('frutas.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(str(frutas))

# Resolvido pelo professor
with open('frutas.txt', 'w', newline='') as arquivo:
    for fruta in frutas:
        arquivo.write(frutas + os.linesep)


# Desafio 2 - Imprima na tela todas as linhas que estao dentro do arquivo frutas.txt

# Resolvido por mim
with open('frutas.txt','r', encoding='utf-8') as arquivo:
    for fruta in arquivo:
        print(fruta)

# Resolvido pelo professor
with open('frutas.txt','r') as arquivo:
    for linha in arquivo:
        print(linha)


# Desafio 3 - Sem apagar os dados que já estão dentro de frutas.txt, adicione todas as cores que estão dentro da sua lista de cores ao arquivos frutas.txt

# Resolvido por mim
with open('frutas.txt', 'a', newline='') as arquivo:
    for cor in cores:
        arquivo.write(cor)

# Resolvido pelo professor
with open('frutas.txt', 'a', newline='') as arquivo:
    for cor in cores:
        arquivo.write(os.linesep + cor)


# Desafio 4 - Crie um novo arquivo chamado 'Top 5 Linguagens.txt' e popule o arquivo, de forma com que cada linuguagem ocupe apenas uma linha.

# Resolvido por mim
with open('Top 5 Linguagens.txt', 'w') as arquivo:
    for linguagens in programacao:
        arquivo.write(linguagens + os.linesep)

# Resolvido pelo professor
with open('Top 5 Linguagens.txt', 'w', newline='') as arquivo:
    for linguagens in programacao:
        arquivo.write(linguagens + os.linesep)

# BONUS - Como você poderia criar vários arquivos diferentes usando um laço for e strings dinâmicos(f'{}'), e também não escrever nada dentro deles?

arquivos = ['musica.mp3', 'foto.jpg', 'senhas.txt', 'relatorio.pdf']

for arquivo in arquivos:
    with open(arquivo, 'w') as arquivo:
        pass