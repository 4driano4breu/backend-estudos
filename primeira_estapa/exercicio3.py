# Lista para armazenar produtos
produtos = []

# Função para CADASTRAR produtos
def cadastrar_produto(nome, preco, quantidade):
    produto = {
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade
    }
    produtos.append(produto)
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
    else:
        print(f'Produto {nome} não encontrado')

# Função para REMOVER estoque aos produtos
def remover_estoque(nome, quantidade):
    produto = buscar_produto(nome)
    if produto:
        if produto['quantidade'] >= quantidade:
            produto['quantidade'] -= quantidade
        else:
            print(f'Quantidade {quantidade} é menor que {produto['quantidade']}, não foi possivel remover.')
    else:
        print(f'Produto {nome} não encontrado')

# Função para REMOVER produto
def remover_produto(nome):
    produto = buscar_produto(nome)
    if produto:
        produtos.remove(produto)
        print(f'Produto {nome} removido com sucesso')
    else:
        print(f'Produto {nome} não encontrado')

# Cadastros
cadastrar_produto("Arroz", 5.99, 100)
cadastrar_produto("Feijão", 8.50, 50)
cadastrar_produto("Macarrão", 3.75, 200)

# Adicionar estoque
adicionar_estoque("Arroz", 50)
adicionar_estoque("Café", 10)        # não existe

# Remover estoque
remover_estoque("Feijão", 20)
remover_estoque("Feijão", 200)       # quantidade maior que o estoque
remover_estoque("Café", 5)           # não existe

# Remover produto
remover_produto("Macarrão")
remover_produto("Café")              # não existe

# Listagem final
listar_produtos()
     