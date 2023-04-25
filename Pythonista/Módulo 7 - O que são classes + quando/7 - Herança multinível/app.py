""" class Usuario:
    def __init__(self, nome, salario, profissao):
        self.nome = nome
        self.salario = salario
        self.profissao = profissao

    def registrar_funcionario(self):
        print(f'Cadastrando usuário {self.nome}')

class Gestor(Usuario):
    def __init__(self, nome, salario, profissao, setor_responsavel):
        super().__init__(nome, salario, profissao)
        self.setor_responsavel = setor_responsavel

    def definir_setor(self, setor):
        print(f'Definir setor para {setor}')

usuario1 = Usuario('Camila', 5000, 'Analista de software')
gestor = Gestor('Roberta', 7000, 'Gestora', 'Gestão de projetos') """

# Herança multinivel
# 1° Problema
class Veiculo:
    pass

class VeiculoRodas(Veiculo):
    quantidade_maxima_rodas = 2

class Carro(VeiculoRodas):
    pass

class CarroEletrico(Carro):
    pass

class CarroEletricoDuaPortas(Carro):
    pass