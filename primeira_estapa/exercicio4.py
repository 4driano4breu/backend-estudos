import json

ARQUIVO = 'estoque.json'

# ============== JSON ============== #
# Salvar lista em arquivo
def salvar_dados():
    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(produtos, f, ensure_ascii=False, indent=4)

# Carregar lista de arquivo
def carregar_dados():
    try:
        with open(ARQUIVO, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# Lista para armazenar produtos
produtos = carregar_dados()

# Função para CADASTRAR produtos
def cadastrar_produto(nome, preco, quantidade):
    produto = buscar_produto(nome)
    if produto:
        print(f'Produto {nome} já cadastrado')
    else:
        produto = {
            'nome': nome,
            'preco': preco,
            'quantidade': quantidade
        }
        produtos.append(produto)
        salvar_dados()
        print(f'Produto {nome} cadastrado com sucesso')

# Função para LISTAR produtos
def listar_produtos():
    for produto in produtos:
        print(f'Nome: {produto['nome']} | Preco: {produto['preco']} | Quantidade: {produto['quantidade']}')

# Função para BUSCAR produtos
def buscar_produto(nome):
    for produto in produtos:
        if produto['nome'] == nome:
            return produto

# Função para ADICIONAR estoque aos produtos
def adicionar_estoque(nome, quantidade):
    produto = buscar_produto(nome)
    if produto:
        produto['quantidade'] += quantidade
        salvar_dados()
    else:
        print(f'Produto {nome} não encontrado')

# Função para REMOVER estoque aos produtos
def remover_estoque(nome, quantidade):
    produto = buscar_produto(nome)
    if produto:
        if produto['quantidade'] >= quantidade:
            produto['quantidade'] -= quantidade
            salvar_dados()
        else:
            print(f'Quantidade {quantidade} é menor que {produto['quantidade']}, não foi possivel remover.')
    else:
        print(f'Produto {nome} não encontrado')

# Função para REMOVER produto
def remover_produto(nome):
    produto = buscar_produto(nome)
    if produto:
        produtos.remove(produto)
        salvar_dados()
        print(f'Produto {nome} removido com sucesso')
    else:
        print(f'Produto {nome} não encontrado')


cadastrar_produto("Arroz", 5.99, 100)
cadastrar_produto("Feijão", 8.50, 50)
cadastrar_produto("Macarrão", 3.75, 200)

listar_produtos()