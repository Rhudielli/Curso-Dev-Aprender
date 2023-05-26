from tkinter import Radiobutton
from time import sleep
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
driver.get("https://cursoautomacao.netlify.app/")
sleep(2)

botao_login = driver.find_element(By.LINK_TEXT, 'Login')
botao_login.click()
sleep(2)

campo_email = driver.find_element(By.NAME, 'email')
campo_email.send_keys('isaque@gmail.com')
sleep(2)

campo_senha = driver.find_element(By.ID, 'senha')
campo_senha.send_keys('jnhbugy')
sleep(2)

btao_enviar = driver.find_element(By.CLASS_NAME, 'btn.btn-primary')
btao_enviar.click()

input('')

######################################################################

# Desafio 🥇

driver.get("https://cursoautomacao.netlify.app/desafios.html")

name = driver.find_element(By.XPATH, 'https://cursoautomacao.netlify.app/desafios.html')
name.send_keys('Isaque')

botao = driver.find_element