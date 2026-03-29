class Produto:
    def __init__(self,nome,preco,quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def detalhes(self):
        print(f'Nome: {self.nome} | Preco: {self.preco} | Quantidade: {self.quantidade}')
    
    def adicionar_estoque(self, quantidade):
        quantidade_ant = self.quantidade
        self.quantidade += quantidade
        print(f'Adicionado: {quantidade} | Anterior: {quantidade_ant} |  Total: {self.quantidade} ')

    def remover_estoque(self, quantidade):
        if self.quantidade >= quantidade:
            self.quantidade -= quantidade
            print(f'Quantidade Removida: {quantidade} | Quantidade Atual: {self.quantidade}')
        else:
            print(f'Não foi possivel remover, quantidade maior que o estoque')

produtos = []

def cadastrar_produto(nome, preco, quantidade):
    produto = Produto(nome, preco, quantidade)
    produtos.append(produto)
    print(f'Produto {nome} cadastrado com sucesso')

def listar_produtos():
    for produto in produtos:
        produto.detalhes()
    
cadastrar_produto("Macarrão", 3.75, 200)
cadastrar_produto("Leite", 4.50, 80)

listar_produtos()