# Quando usar módulos
# 1° - Separar funcionalidades relacionadas
# 2° - Não acoplar o seu código - acoplar (não vai misturar, o que não deve ser misturado, em um mesmo local)
# 3° - Não ter um arquivo (unico) gigante

from banco_dados import buscar_usuario
from configuracoes import senha

buscar_usuario()
print(senha)