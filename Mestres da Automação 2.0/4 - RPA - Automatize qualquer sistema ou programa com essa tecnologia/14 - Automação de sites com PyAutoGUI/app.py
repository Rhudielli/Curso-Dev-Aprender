import webbrowser
import pyautogui
from time import sleep

#webbrowser.open('')

# Abrir uma aba no navegador existente ou criar outro
""" webbrowser.open_new('https://facebook.com')

# Abrir uma aba em um navegador existente ou criar outro
webbrowser.open_new_tab('https://www.google.com')

# Criar e abrir uma nova janela do zero
webbrowser.open_new('https://www.twitter.com') """

#########################################################################

# DESAFIO 🥇

# 1) Navegue até o site https://cursoautomacao.netlify.app/
webbrowser.open('https://cursoautomacao.netlify.app/')

# 2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas" e digite seu nome
pyautogui.moveTo(1475,626, duration=1.5)
pyautogui.scroll(-2100)
sleep(1.5)
pyautogui.click()
pyautogui.typewrite('Isaque Rhudielli')
sleep(1.5)


# 3) Clique em alerta, para gerar a alerta
pyautogui.click(1140,660, duration=1.5)

# 4) Feche a alerta
pyautogui.click(1711,195, duration=1.5)

# 5) Suba a página totalmente para cima
pyautogui.scroll(2100)
sleep(1.5)

# 6) Desça apenas o suficiente para conseguir chegar até a secção que contém os arquivos para o quais irá fazer o download e click no botão de download para realizar o downlaod dos arquivos excel e pdf.
pyautogui.scroll(-3500)

pyautogui.click(1292,670, duration=1.5)

pyautogui.click(1284,803, duration=1.5)

# 7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"
pyautogui.alert(text='Você terminou', title='Automação')