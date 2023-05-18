import pyautogui

# Mostrar alerta
""" pyautogui.alert(text='Iniciando sua automação', title='Automação', button='ok')

# Pedir informação
email = pyautogui.prompt(text='Digite seu email', title='informações obrigatórias')
print(f'Você digitou {email}')

# Confirmar se algo deve ou não acontecer
resposta = pyautogui.confirm(text='Continuar rodando nossa automação?', title='confrimação', buttons=['sim', 'não', 'cancelar'])
print(resposta)

if resposta == 'sim':
    print('continuando automação')
elif resposta == 'não':
    print('encerrando automação')
else:
    print('automação cancelada')

# Como pegar senha
senha = pyautogui.password(text='digite sua senha', title='dados de login', mask='*')
print(senha) """

########################################################################################################

# Desafio 🥇

# Crie um programa que pede o usuário e senha, na sequencia, copia e cola o usuario dentro de um bloco de notas

email = pyautogui.prompt(text='Seu email', title='Email')
print(f'Email: {email}')

senha = pyautogui.password(text='Sua senha', title='Senha', mask='@')
print(f'Sua senha: {senha}')

pyautogui.click(1479,604)

pyautogui.typewrite(email)
pyautogui.typewrite(senha)