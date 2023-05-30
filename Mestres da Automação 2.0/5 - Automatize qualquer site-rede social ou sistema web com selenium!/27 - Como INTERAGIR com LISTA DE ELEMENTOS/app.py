from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import random


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

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
sleep(4)
checkboxes[0].click()
checkboxes[2].click()

input('') """

######################################################################

# Desafios 🥇

driver.get('https://cursoautomacao.netlify.app/desafios.html')
sleep(2)

driver.execute_script("window.scrollTo(0, 1700)")
sleep(2)

carro2 = driver.find_element(By.XPATH, '/html/body/section[5]/div[2]/input')
carro2.click()

carro4 = driver.find_element(By.XPATH, '/html/body/section[5]/div[4]/input')
carro4.click()

carro5 = driver.find_element(By.XPATH, '/html/body/section[5]/div[5]/input')
carro5.click()

sleep(2)

motos = driver.find_elements(By.XPATH, "//input[@name='motos']")
for moto in motos:
    moto.click()

input('')