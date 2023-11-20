import tkinter as tk
from tkinter import messagebox

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

        # Configurando a geometria da janela
        root.geometry("400x600")

    def add_item(self):
        bluebird = self.entry_bluebird.get()
        loja = self.entry_loja.get()

        if bluebird and loja:
            self.data_dict[bluebird] = loja
            self.clear_entries()
            messagebox.showinfo("Sucesso", "Item adicionado com sucesso!")

    def show_items(self):
        self.clear_entries()
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


if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDApp(root)
    root.mainloop()
