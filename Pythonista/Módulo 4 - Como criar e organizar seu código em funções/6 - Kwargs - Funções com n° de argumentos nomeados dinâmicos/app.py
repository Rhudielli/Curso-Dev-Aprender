# **kwargs (Keywords Arguments)
def concatenar(**palavras):
    frase = ''
    for palavra in palavras.values():
        frase += palavra + ' '
    print(frase)

concatenar(a = 'Nós', b = 'Somos', c = 'Pythonista', d = 'Profissionais')


# nome = agumento comum / args = qnt ilimitada de argumentos posicionais / **kwargs = qnt ilimitada de argumentos nomeados
# agumento comum = 'Isaque'
# qnt ilimitada de argumentos posicionais = 4,5,6,7
# qnt ilimitada de argumentos nomeados = a=1, b=2, c=3 ou com espaço

def fazer_calculo(nome, *args, **kwargs):
    print(nome)
    print(args)
    print(kwargs)
    for arg in args:
        print(arg)
    for kwarg in kwargs.values():
        print(kwarg)

fazer_calculo('Isaque', 4,5,6,7, a=1,b=2,c=3)