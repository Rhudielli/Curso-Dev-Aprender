from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys


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
driver.get('https://cursoautomacao.netlify.app/')
sleep(1)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)

iframe = driver.find_element(By.XPATH, "//iframe[@src='https://cursoautomacao.netlify.app/desafios.html']")

# Mudar para dentro do iframe
driver.switch_to.frame(iframe)

# Interagir com ele
campo_nome = driver.find_element(By.ID, 'dadosusuario')
campo_nome.send_keys('Isaque')

# Sair do iframe
driver.switch_to.default_content()

input('')