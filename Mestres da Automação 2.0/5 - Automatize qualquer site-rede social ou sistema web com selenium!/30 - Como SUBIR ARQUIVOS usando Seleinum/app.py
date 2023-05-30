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
driver.get('https://cursoautomacao.netlify.app')
sleep(2)

driver.execute_script("window.scrollTo(0, 2500)")
sleep(2)

arquivo = driver.find_element(By.XPATH, '//input[@id="myFile"]')
arquivo.send_keys('C:\\Users\\Isaque\\Desktop\\pasta\\1307306.png')
sleep(2)

enviar = driver.find_element(By.XPATH, "//input[@value='Enviar Arquivo']")
enviar.click()

input('')