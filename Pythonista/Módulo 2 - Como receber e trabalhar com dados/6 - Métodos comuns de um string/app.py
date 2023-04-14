nome_curso = ' Edição de Vídeo '
            #012345
print(nome_curso.upper())
print(nome_curso.lower())
print(nome_curso.strip())
print(nome_curso.lstrip())
print(nome_curso.rstrip())
print(nome_curso.find('ção'))
print(nome_curso.replace('Vídeo', 'Música'))
print('https://pr.olx.com.br/?o=90&q=relogio'.replace('relogio', 'carro'))

##########################################################################################################################################

# Desafio - Através da criação de strings dinâmicos e os métodos de um string que acabou de aprender, use como base as variáveis para criar as seguinte frase

# É melhor FEITO que PERFEITO

a = 'é'
b = 'MELHOR'
c = 'QUE'
d = 'feito'
e = 'perfeito'

print(f'{a.upper()} {b.lower()} {d.upper()} {c.lower()} {e.upper()}')