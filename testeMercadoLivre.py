from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
import time
import os

# limpando terminal anterior
os.system('cls')

dict_bluebird = {'notebook': ' nitro', 'tv':' samsung', 'iphone': ' 14'}

# adicionar Bluebirds ao dicionário
# while True:
    # # chave = input("Digite a chave/nome Bluebird (ou 'sair' para encerrar): ")
    
    # if chave.lower() == 'sair':
    #     break
    
    # valor = input("Digite o valor/loja: ")
    # dict_bluebird[chave] = valor
    
# ...

# Inicializar o navegador (neste exemplo, usaremos o Chrome)
driver = webdriver.Firefox()

# Abrir o site desejado
driver.get('https://www.mercadolivre.com.br/')

# Iterar sobre os dados do dict
for index in dict_bluebird:
    
    print('Pesquisando: ', index, dict_bluebird[index])

    # Localizar elementos no site e interagir com eles (exemplo: preenchimento de formulário)
    barra_pesquisa = driver.find_element(By.XPATH, '/html/body/header/div/div[2]/form/input') 
    
    # Utilize row['Nome do Dispositivo'] para acessar os dados do DataFrame
    barra_pesquisa.send_keys(index)  # digita notebook (chave)
    time.sleep(2)
    barra_pesquisa.send_keys(dict_bluebird[index])  # digita nitro (valor da chave)
    time.sleep(2)
    barra_pesquisa.send_keys(Keys.ENTER)        
    # Aguardar um tempo para os resultados carregarem (ajuste conforme necessário)
    time.sleep(2)

    # Limpar a caixa de pesquisa usando o método clear()
    barra_pesquisa = driver.find_element(By.XPATH, '//*[@id="cb1-edit"]')

    # Clique após a limpeza da caixa de pesquisa
    barra_pesquisa.click()
    barra_pesquisa.clear()
    
    time.sleep(5)

# Fechar o navegador ao finalizar
# driver.quit()

