import time
import schedule
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as uc
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

    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotSelectableException,
            ElementNotSelectableException
        ]
    )

    return driver, wait

#driver.maximize_window()
driver, wait = iniciar_driver()

driver.get('https://www.google.com/travel/flights')



""" voo = wait.until(uc.visibility_of_element_located((By.XPATH, '')))

voo = driver.find_element(By.XPATH,'')

voo = wait.until(uc.visibility_of_any_elements_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/ol/li[1]/div/div[1]'))) """

voo = wait.until(uc.element_to_be_clickable((By.XPATH, '')))

voo.click()

input('')