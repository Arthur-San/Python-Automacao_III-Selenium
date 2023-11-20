from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 1 - acessando site

browser = webdriver.Firefox()
browser.get('https://registro.br')