import json

def adicionar_produto():

    try:
        with open("store.json", "r") as file:
            dados = json.load(file)
    except FileNotFoundError:
        dados = []

    
    
    id_produto = int(input("Digite o ID do produto: "))
    title_produto = input("Digite o título do produto: ")
    price_produto = float(input("Digite o preço do produto: "))
    imagem_produto = input("Digite o caminho da imagem: ")

    
    novo_produto = {
        "id": id_produto,
        "title": title_produto,
        "price": price_produto,
        "image": imagem_produto 
    }


    dados.append(novo_produto)

    with open("store.json", "w") as file:
        json.dump(dados, file, indent=4)

    print(f"Produto {title_produto} adicionado com sucesso!")

adicionar_produto()
