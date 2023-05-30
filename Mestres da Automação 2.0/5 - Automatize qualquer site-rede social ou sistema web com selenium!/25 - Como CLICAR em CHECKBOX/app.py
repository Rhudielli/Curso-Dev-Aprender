from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


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
sleep(2)
driver.execute_script("window.scrollTo(0, 500);")

checkbox_1 = driver.find_element(By.ID, 'acessoNivel1Checkbox')
checkbox_2 = driver.find_element(By.ID, 'acessoNivel2Checkbox')
checkbox_3 = driver.find_element(By.ID, 'acessoNivel3Checkbox')

checkbox_1.click()
checkbox_2.click()
checkbox_3.click()

if checkbox_2.is_selected() == True:
    print('Checkbox 2 está selecionado')

input('') """

######################################################################

# Desafio 🥇

driver.get('https://cursoautomacao.netlify.app/desafios.html')
sleep(2)

driver.execute_script("window.scrollTo(0, 800)")
sleep(2)

carro = driver.find_element(By.XPATH, "//input[@id='conversivelcheckbox']")
road = driver.find_element(By.XPATH, "//input[@id='offroadcheckbox']")

carro.click()
road.click()


input('')