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
    arguments = ['--lang=pt-BR', '--window-size=1200,800', '--incognito']
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
driver.get('https://cursoautomacao.netlify.app')
sleep(2)

# uma imagem
""" bandeira = driver.find_element(By.XPATH, '//img[@alt="Bandeira do Brasil"]')
with open('bandeira.jpg','wb') as arquivo:
    arquivo.write(bandeira.screenshot_as_png) """

# mais de uma imagem
driver.execute_script('window.scrollTo(0, 1600)')
sleep(1)

imagens = driver.find_elements(By.XPATH, '//img[@class="img-thumbnail"]')
contador = 1
sleep(1)

for imagem in imagens:
    with open(f'imagem{contador}.jpg','wb') as arquivo:
        arquivo.write(imagem.screenshot_as_png)
        sleep(1)
    contador += 1

input('')