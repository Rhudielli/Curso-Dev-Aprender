# Herança Multipla

class Pessoa:
    nome = 'Sou uma pessoa'

class Profissional:
    nome = 'Sou um profissional'

class AtorProfissional(Pessoa, Profissional):
    pass

print(AtorProfissional.nome)
# MRO(Method Resolution Order)