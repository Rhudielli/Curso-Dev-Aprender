from turtle import Turtle

# Inicializar uma Turtle
t = Turtle()
""" t.speed(1)

# Movimentar Turtle para frente
t.forward(100)

# Rotacionar Turtle em X graus para direita
t.right(90)
t.forward(100)

# Rotacionar Turtle em X graus para esquerda
t.left(90)
t.forward(100)

# Movimentar Turtle para trás
t.backward(200)

while True:
    distancia = int(input('Distancia a percorrer? '))
    t.forward(distancia) """

###############################################################################################################################################################

# Desafio 🥇

### Desafio 1 

# Monte um mini-game turtle, que possibilite que o usuário controle para qual direção a tartaruga deve andar(frente/trás) e qual ângulo deverá ser tomado a cada nova movimentação

# ### Desafio 2 

# Usando o mini-game, desenha um quadrado passando instruções para a turtle, totalmente através do input do usuário

# #### Dicas Iniciais

# * Crie uma nova turtle primeiro

# * Coloca seu programa em loop 

# * Faça perguntas ao usuário para decidir se a tartaruga deve movimentar para frente ou para trás

# * Após decidir se ele deve movimentar para frente ou para trás, receba do usuário quantos pixels devem ser percorridos

# * Faça perguntas ao usuário para decidir se a tartaruga deve rotacionar para esquerda ou direta

# * Após decidir se ele deve rotacionar para esquerda ou direita, receba do usuário quantos pixels devem ser rotacionados

# * Ao executar essa ação pergunte ao usuário "Continuar andando?", e reaga de acordo com a resposta do usuário.

# #### Dicas Adicionais

# * Não esqueça de converter o input do usuário para o tipo apropriado

# * Resolva um problema de cada vez e lembre de seguir a seguinte lógica: 

# Pergunte -> Processe resposta -> A

###############################################################################################################################################################

# Resolução
while True:
    rotacionar = input('Rotacionar? ')
    if rotacionar == 'sim':
        direcao = input('Direita, Esquerda, Trás ou Frente? ')
        if direcao == 'direita':
            graus_d = int(input('Quantos graus? '))
            t.right(graus_d)
            cm_frente = int(input('Quanto CM para frente? '))
            t.forward(cm_frente)
            continue
        if direcao == 'esquerda':
            graus_e = int(input('Quantos graus? '))
            t.left(graus_e)
            cm_frente = int(input('Quanto CM para frente? '))
            t.forward(cm_frente)
            continue
        if direcao == 'tras':
            cm_t = int(input('Quantos CM para trás? '))
            t.backward(cm_t)
            continue
        if direcao == 'frente':
            graus_f = int(input('Quanto CM para frente? '))
            t.forward(graus_f)
    if rotacionar == 'nao':
        break