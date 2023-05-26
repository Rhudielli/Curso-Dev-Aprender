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
driver.get("https://cursoautomacao.netlify.app/desafios.html")

# Rolar até o fim da página
""" driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# Rolar até o topo da página
driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
# Rolar X quantidade de pixels da página (descer)
driver.execute_script("window.scrollTo(0, 1500);")
# Rolar X quantidade de pixels da página (subir)
driver.execute_script("window.scrollTo(0, -1500);")
 """
######################################################################

# Desafio 🥇

# navegue ate o final da pagina e depois para o inicio da pagina

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
sleep(2)