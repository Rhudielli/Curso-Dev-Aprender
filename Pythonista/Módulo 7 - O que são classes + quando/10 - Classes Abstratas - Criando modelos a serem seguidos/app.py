# Classes abstratas
# Criar um contrato(esqueleto) -> que deve ser implementado na classe que a herda

from  abc import ABC, abstractmethod

class Camera(ABC):
    @abstractmethod
    def definir_tamanho_lente(self, tamanho):
        pass

class CameraProfissional(Camera):
    def definir_tamanho_lente(self, tamanho):
        print(f'Alterando a lente para {tamanho}')

camera_profissional = CameraProfissional()
camera_profissional.definir_tamanho_lente(5)

###############################################################################################################################################################

# DESAFIO 🥇

# Crie uma classse abstrata chamada Monitor, que irá ter 2 métodos abstratos:
# aumentar_claridade e reduzir_claridade

# Os métodos iram receber um número que representa o quanto de claridade deve ser aumentado ou diminuido ao chamar eles.

# Após ter criado a classe abstrata, crie uma nova classe chamada de MonitorFullHD e coloque a implementaçãodos metodos aumentar_claridade e reduzir_claridade dentro deles.