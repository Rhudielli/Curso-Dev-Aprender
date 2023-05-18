# Como usar a função click
import pyautogui

# link aula: https://cpstest.org/100-seconds.php

# pyautogui.click(x=1000, y=500, clicks=2, interval=0.0, button='left', duration=2)

# Click personalizado
pyautogui.click(x=1444, y=511, clicks=100, interval=0.1, button='left', duration=2)

# Click na posição atual (botão esquerdo)
pyautogui.click()

# right (direita) / middle (meio)
pyautogui.click(button='left')

# Clicar X vezes
pyautogui.click(clicks=10)

# Funções prontas para clicks
pyautogui.doubleClick()
pyautogui.rightClick()
pyautogui.leftClick()
pyautogui.middleClick()
pyautogui.tripleClick()

######################################################################

# Desafio 🥇

pyautogui.rightClick(1497,486, duration=2)
pyautogui.click(1580,887, duration=2)
pyautogui.click(1220,602, duration=2)