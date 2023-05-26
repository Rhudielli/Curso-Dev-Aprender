from tkinter import Radiobutton
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,600', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver


driver = iniciar_driver()
driver.get("https://cursoautomacao.netlify.app/desafios.html")

# Class name separado: btn2 btn btn-dark = btn2.btn.btn-dark

""" idade = driver.find_element(By.ID, 'campoIdade')

if idade.is_enabled():
    print('campo habilitado')

if idade.is_enabled() == False:
    print('campo desabilitado') """


######################################################################

# Desafio 🥇

# Encontre cada um destes botões usano o que aprendeu e descubra o estado de cada um desses botões

btn1 = driver.find_element(By.XPATH, '//*[@id="btn1"]')
btn2 = driver.find_element(By.XPATH, '/html/body/section[1]/button[2]')
btn3 = driver.find_element(By.XPATH, '/html/body/section[1]/button[3]')

if btn1.is_enabled():
    print('Btn 1 habilitado')
if btn1.is_enabled() == False:
    print('btn 1 desabilitado')

if btn2.is_enabled():
    print('Btn 2 habilitado')
if btn2.is_enabled() == False:
    print('btn 2 desabilitado')

if btn3.is_enabled():
    print('Btn 3 habilitado')
if btn3.is_enabled() == False:
    print('btn 3 desabilitado')