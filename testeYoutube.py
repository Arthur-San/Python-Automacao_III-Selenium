import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Carregar os dados do Excel
df = pd.read_excel(r'C:\Users\arthur\Desktop\ONE BIT CODE\Python-Automacao_III-Selenium\Pasta1.xlsx')

# Inicializar o navegador
driver = webdriver.Firefox()

# Iterar sobre os títulos na planilha
for titulo in df['Título']:
    try:
        # Abrir o YouTube
        driver.get('https://www.youtube.com/')

        # Localizar a barra de pesquisa
        search_box = driver.find_element(By.NAME, 'search_query')

        # Limpar a barra de pesquisa e inserir o título do vídeo
        search_box.clear()
        search_box.send_keys(titulo)

        # Pressionar Enter para realizar a busca
        search_box.send_keys(Keys.RETURN)

        # Aguardar um tempo para os resultados carregarem (pode ser ajustado conforme necessário)
        driver.implicitly_wait(5)

        # Aqui você pode adicionar lógica para lidar com os resultados da busca, como imprimir os resultados
        # Vamos imprimir o título de todos os vídeos encontrados, por exemplo
        video_titulos = driver.find_elements(By.CSS_SELECTOR, 'h3.title')
        if video_titulos:
            for video_titulo in video_titulos:
                print(f"Título do vídeo para '{titulo}': {video_titulo.text}")
        else:
            print(f"Nenhum vídeo encontrado para o título '{titulo}'.")

    except Exception as e:
        print(f"Erro ao buscar o título '{titulo}': {str(e)}")

# Fechar o navegador ao finalizar
driver.quit()
