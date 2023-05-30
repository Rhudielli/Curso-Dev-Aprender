import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,800', '--incognito']
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
""" driver.get('https://cursoautomacao.netlify.app')

dropdown = driver.find_element(By.XPATH, '//select[@id="paisselect"]')
opcoes = Select(dropdown)
# indice
opcoes.select_by_index(2)
sleep(2)
# value
opcoes.select_by_value('estadosunidos')
sleep(2)
# texto de exibição
opcoes.select_by_visible_text('Brasil')
sleep(2)

input('') """

######################################################################

# Desafio 🥇

driver.get('https://cursoautomacao.netlify.app/desafios.html')
sleep(2)
driver.execute_script("window.scrollTo(0, 2200)")
sleep(2)

dropdown = driver.find_element(By.XPATH, '//*[@id="paisesselect"]')
opcoes = Select(dropdown)
opcoes.select_by_index(2)
sleep(1)
opcoes.select_by_value('africa')
sleep(1)
opcoes.select_by_visible_text('Chille')
sleep(1)

input('')