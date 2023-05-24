# Como usar botões e atalhos do teclado

import pyautogui

# Navegar e clicar no campo email
pyautogui.click(1411, 265, duration=2)

# digitar o email
pyautogui.typewrite('admin@hotmail.com')

# Apertar tab
pyautogui.press('tab')

# digiar minha senha
pyautogui.typewrite('123456')

# apertar tab
pyautogui.press('tab')

# apertar space
pyautogui.press('space')

# Dica ✔
print(pyautogui.KEYBOARD_KEYS)

######################################################################

# Mais coisas que não vou fazer pois nã tenho a tela de login

# Sem hotkey
pyautogui.keyDown('ctrl')
pyautogui.keyDown('a')
pyautogui.keyUp('ctrl')
pyautogui.keyUp('a')

# Com hotkey
pyautogui.hotkey('ctrl', 'a')