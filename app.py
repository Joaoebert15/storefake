import json
import tkinter as tk
from tkinter import messagebox

def adicionar_produto():
    try:
        with open("store.json", "r") as file:
            dados = json.load(file)
    except FileNotFoundError:
        dados = []

    id_produto = entry_id.get()
    title_produto = entry_title.get()
    price_produto = entry_price.get()
    imagem_produto = entry_image.get()

    if not id_produto or not title_produto or not price_produto:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos obrigatórios.")
        return

    try:
        id_produto = int(id_produto)
        price_produto = float(price_produto)
    except ValueError:
        messagebox.showerror("Erro", "ID e preço devem ser números válidos.")
        return

    novo_produto = {
        "id": id_produto,
        "title": title_produto,
        "price": price_produto,
        "image": imagem_produto
    }

    dados.append(novo_produto)

    with open("store.json", "w") as file:
        json.dump(dados, file, indent=4)

    messagebox.showinfo("Sucesso", f"Produto {title_produto} adicionado com sucesso!")
    limpar_campos()

def limpar_campos():
    entry_id.delete(0, tk.END)
    entry_title.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_image.delete(0, tk.END)

# Criação da interface gráfica
root = tk.Tk()
root.title("Adicionar Produto")

tk.Label(root, text="ID do Produto:").grid(row=0, column=0, padx=50, pady=10)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1, padx=50, pady=5)

tk.Label(root, text="Título do Produto:").grid(row=1, column=0, padx=50, pady=10)
entry_title = tk.Entry(root)
entry_title.grid(row=1, column=1, padx=50, pady=5)

tk.Label(root, text="Preço do Produto:").grid(row=2, column=0, padx=50, pady=10)
entry_price = tk.Entry(root)
entry_price.grid(row=2, column=1, padx=50, pady=10)

tk.Label(root, text="Caminho da Imagem:").grid(row=3, column=0, padx=50, pady=5)
entry_image = tk.Entry(root)
entry_image.grid(row=3, column=1, padx=50, pady=5)

btn_add = tk.Button(root, text="Adicionar Produto", command=adicionar_produto)
btn_add.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
