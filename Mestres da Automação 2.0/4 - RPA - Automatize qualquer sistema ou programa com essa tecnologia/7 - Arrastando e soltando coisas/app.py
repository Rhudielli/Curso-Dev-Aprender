# Como pegar e "arrastar" algo para outro lugar

import pyautogui

for i in range(10):
    # Passos
    # Mover até uma coordenada
    pyautogui.moveTo(1250,200, duration=0.2)

    # Clicar e arrastar até um ponto e soltar
    pyautogui.dragTo(1250,966, button='left', duration=0.2)