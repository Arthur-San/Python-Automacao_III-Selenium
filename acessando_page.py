from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import time

# versão do selenium '4.15.2'

# 1 - utilizando o WebDriver

browser = webdriver.Firefox()

browser.get('https://www.amazon.com/')
browser.maximize_window()

# ofertas_dia = browser.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/div[3]/div/a[4]/div[1]/span[2]')

# ofertas_dia.click()

# criar_conta = browser.find_element(By.XPATH, '//*[@id="a-autoid-1-announce"]')
# time.sleep(2)
# criar_conta.click()

# 2 - Acessando elementos numa página
elem = browser.find_element(By.ID, 'twotabsearchtextbox')
pyautogui.hotkey('ctrl', 'f')
pyautogui.hotkey('$')
pyautogui.hotkey('ENTER')


