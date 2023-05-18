# Como digitar em Pyautogui

import pyautogui
import pyperclip

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')

# Mover mouse até campo de digitar
pyautogui.moveTo(1650,1033, duration=1)
# Clicar no campo de digitar

pyautogui.click()
# Digitar minha mensagem
""" pyautogui.typewrite('Olá, bom dia!') """
escrever_frase('Olá, bom dia!')

# Clicar no botão de enviar
pyautogui.click(1888,1035, duration=1)

###################################################################

# Desafio 🥇

# Crie um programa que vai até onde seu bloco de notas estiver aberto e digita a frase "Automação é Incrível!"

def frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

pyautogui.click(1173,595, duration=1)
frase('Automação é Incrível!')