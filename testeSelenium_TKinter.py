import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
# from threading import Thread

#limpa terminal quando executa
os.system('cls')

class CRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD App")

        # Dicionário para armazenar os dados
        self.data_dict = {}

        # Interface de usuário
        self.label_bluebird = tk.Label(root, text="Bluebird:")
        self.label_bluebird.pack(pady=10)
        self.entry_bluebird = tk.Entry(root)
        self.entry_bluebird.pack(pady=10)

        self.label_loja = tk.Label(root, text="Loja:")
        self.label_loja.pack(pady=10)
        self.entry_loja = tk.Entry(root)
        self.entry_loja.pack(pady=10)
        
        self.listbox = tk.Listbox(root)
        self.listbox.pack(pady=10)

        self.add_button = tk.Button(root, text="Adicionar", command=self.add_item)
        self.add_button.pack(pady=5)

        self.show_button = tk.Button(root, text="Mostrar Itens", command=self.show_items)
        self.show_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Atualizar", command=self.update_item)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Excluir", command=self.delete_item)
        self.delete_button.pack(pady=5)

        # Botão para executar o Selenium
        self.selenium_button = tk.Button(root, text="Executar Selenium", command=self.run_selenium)
        self.selenium_button.pack(pady=10)

        # Configurando a geometria da janela
        root.geometry("400x600")

    def add_item(self):
        bluebird = self.entry_bluebird.get()
        loja = self.entry_loja.get()

        if bluebird and loja:
            self.data_dict[bluebird] = loja
            self.clear_entries()
            self.show_items()
            messagebox.showinfo("Sucesso", "Item adicionado com sucesso!")

    def show_items(self):
        self.listbox.delete(0, tk.END)
        for bluebird, loja in self.data_dict.items():
            self.listbox.insert(tk.END, f"{bluebird} - {loja}")

    def update_item(self):
        bluebird = self.entry_bluebird.get()
        loja = self.entry_loja.get()

        if bluebird and loja:
            if bluebird in self.data_dict:
                self.data_dict[bluebird] = loja
                self.clear_entries()
                self.show_items()
                messagebox.showinfo("Sucesso", "Item atualizado com sucesso!")
            else:
                messagebox.showwarning("Aviso", "Bluebird não encontrado.")
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos.")

    def delete_item(self):
        bluebird = self.entry_bluebird.get()

        if bluebird:
            if bluebird in self.data_dict:
                del self.data_dict[bluebird]
                self.clear_entries()
                self.show_items()
                messagebox.showinfo("Sucesso", "Item excluído com sucesso!")
            else:
                messagebox.showwarning("Aviso", "Bluebird não encontrado.")
        else:
            messagebox.showwarning("Aviso", "Preencha o campo Bluebird.")

    def clear_entries(self):
        self.entry_bluebird.delete(0, tk.END)
        self.entry_loja.delete(0, tk.END)

    def run_selenium(self):
        # Inicializar o navegador (neste exemplo, usaremos o Chrome)
        driver = webdriver.Firefox()

        # Abrir o site desejado
        driver.get('https://www.mercadolivre.com.br/')

        # Iterar sobre os dados do dict
        for index in self.data_dict:
            print('Pesquisando: ', index, self.data_dict[index])

            # Localizar elementos no site e interagir com eles (exemplo: preenchimento de formulário)
            barra_pesquisa = driver.find_element(By.XPATH, '/html/body/header/div/div[2]/form/input') 

            # Utilize row['Nome do Dispositivo'] para acessar os dados do DataFrame
            barra_pesquisa.send_keys(index)  # digita notebook (chave)
            time.sleep(1)
            barra_pesquisa.send_keys(self.data_dict[index])  # digita nitro (valor da chave)
            time.sleep(1)
            barra_pesquisa.send_keys(Keys.ENTER)        
            # Aguardar um tempo para os resultados carregarem (ajuste conforme necessário)
            time.sleep(5)
            
            # Clicar no anuncio
            anuncio = driver.find_elements(By.XPATH, f'//*[contains(@title, "{self.data_dict[index]}")]')
            for x in anuncio:
                # Aguardar 5 segundos (ou o tempo necessário)
                time.sleep(5)

                # Clicar no anúncio
                anuncio.click()

            try:
                # Limpar a caixa de pesquisa usando o método clear()
                barra_pesquisa = driver.find_element(By.XPATH, '//*[@id="cb1-edit"]')
                barra_pesquisa.click()
                barra_pesquisa.clear() # Clique após a limpeza da caixa de pesquisa
            except:
                barra_pesquisa = driver.find_element(By.XPATH, '//*[@class="nav-search-input"]')
                barra_pesquisa.click()
                barra_pesquisa.clear() # Clique após a limpeza da caixa de pesquisa

            
            

            time.sleep(3)

        # Fechar o navegador ao finalizar
        driver.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDApp(root)
    root.mainloop()
