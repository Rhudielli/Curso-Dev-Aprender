from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
""" driver.get('https://cursoautomacao.netlify.app/exemplo_chains')

# ActionChains(sequencia de passos)
botao = driver.find_element(By.ID, 'botao-direito')
chain = ActionChains(driver)
chain.context_click(botao).pause(3).send_keys(Keys.DOWN).pause(3).send_keys(Keys.DOWN).pause(3).send_keys(Keys.DOWN).pause(3).click().perform() """

###########

driver.get('https://cursoautomacao.netlify.app/')
radio_button = driver.find_element(By.ID, 'WindowsRadioButton')
chain2 = ActionChains(driver)
chain2.click(radio_button).pause(3).send_keys(Keys.DOWN).pause(3).send_keys(Keys.UP).click().perform()


input('')