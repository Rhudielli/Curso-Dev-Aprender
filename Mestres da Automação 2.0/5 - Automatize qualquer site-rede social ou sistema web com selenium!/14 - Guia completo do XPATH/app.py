from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

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

# Exemplo 1 - //*[contains(text(),'Dropdown') and contains(text(),'Bootstrap')]
# Exemplo 2 - //div[@id='select-class-example']//fieldset/h4
# Exemplo 3 - //thead//tr//th[3]

driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app')

driver.find_element(By.XPATH, '//thead//tr//th[3]')