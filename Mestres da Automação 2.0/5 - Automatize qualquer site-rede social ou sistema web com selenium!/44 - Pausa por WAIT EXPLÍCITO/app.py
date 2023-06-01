from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as condicao_esperada


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

    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException
        ]
    )

    return driver, wait

# Link selenium - https://selenium-python.readthedocs.io/api.html#module-selenium.common.exceptions

driver, wait = iniciar_driver()
# driver.implicitly_wait(10)
""" driver.get('http://google.com/flights')

sugestoes_voo = wait.until(condicao_esperada.visibility_of_any_elements_located((By.XPATH, '//div[@class="EWmqCb cl7p6d whkpce"]')))
sugestoes_voo = driver.find_elements(By.XPATH, "//div[@class='wIuJz']")
sugestoes_voo[0].click() """

# outro uso
driver.get('https://cursoautomacao.netlify.app/login.html')
campo_email = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//input[@id="email"]')))
campo_email.send_keys('isaque@gmail.com')

input('')
driver.close()