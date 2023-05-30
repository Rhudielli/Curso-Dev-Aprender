import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,850', '--incognito']
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

#driver.maximize_window()
driver = iniciar_driver()
""" driver.get('https://cursoautomacao.netlify.app')
sleep(2)

# janela inicial
janela_inicial = driver.current_window_handle
print(f'Primeira janela: {janela_inicial}')

driver.execute_script('window.scrollTo(0, 500)')
sleep(3)

abrir_janela = driver.find_element(By.XPATH, '//button[text()="Abrir Janela"]')
sleep(1)
driver.execute_script('arguments[0].click()', abrir_janela)
sleep(1)

# quais janelas estao abertas
janelas = driver.window_handles
for janela in janelas:
    print(f'Janela secundaria: {janela}')
    if janela not in janela_inicial:
        # alterar para essa nova janela
        driver.switch_to.window(janela)
        sleep(2)
        campo_pesquisa = driver.find_element(By.ID, 'campo_pesquisa')
        sleep(2)
        campo_pesquisa.send_keys('computador')
        sleep(2)
        botao_pesquisar = driver.find_element(By.ID, 'fazer_pesquisa')
        sleep(2)
        botao_pesquisar.click()
        driver.close()
driver.switch_to.window(janela_inicial) """

######################################################################

# Desafio 🥇

driver.get('https://cursoautomacao.netlify.app/desafios.html')
sleep(2)

driver.execute_script('window.scrollTo(0, 3000)')
sleep(2)

janela1 = driver.current_window_handle

novaJanela = driver.find_element(By.XPATH, '/html/body/section[7]/button')
novaJanela.click()
sleep(2)

janelas = driver.window_handles

for janela in janelas:
    if janela not in janela1:
        driver.switch_to.window(janela)
        sleep(2)
        campoJanela2 = driver.find_element(By.XPATH, '//*[@id="opiniao_sobre_curso"]')
        sleep(2)
        campoJanela2.send_keys('''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.''')

        btnPesquisar = driver.find_element(By.XPATH, '//*[@id="fazer_pesquisa"]')
        sleep(2)
        btnPesquisar.click()
        sleep(2)
        driver.close()
driver.switch_to.window(janela1)

sleep(2)
pesquisa_volta = driver.find_element(By.XPATH, '//*[@id="campo_desafio7"]')
pesquisa_volta.send_keys('''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.''')


input('')