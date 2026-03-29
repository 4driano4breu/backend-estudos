# Exercicio 2

# Lista para armazenar os Livros

livros = []

# Função para cadastrar Livros

def cadastrar_livro(titulo,autor,ano_publicacao):
    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano_publicacao": ano_publicacao,
        "disponivel": True
    }
    livros.append(livro)
    print(f'Livro {titulo} inserido com sucesso')

# Função para listar Livros

def listar_livros():
    for livro in livros:
        print(f'Titulo: {livro['titulo']} | Autor: {livro['autor']} | Ano de Publicação {livro['ano_publicacao']} | Está diponivel: {livro['disponivel']}')

# Função para buscar Livros

def buscar_livro(titulo):
    for livro in livros:
        if livro['titulo'] == titulo:
            return livro

# Função para emprestar Livros

def emprestar_livro(titulo):
    livro = buscar_livro(titulo)
    if livro:
        if livro['disponivel']:
            livro['disponivel'] = False
            print(f"Livro {titulo} emprestado com sucesso")
        else:
            print(f'Livro {titulo} não está diponivel no momento')
    else:
        print('Livro não encontrado')
  

# Função para devolver Livros

def devolver_livro(titulo):
    livro = buscar_livro(titulo)
    if livro:
        if not livro['disponivel']:
            livro['disponivel'] = True
            print(f"Livro {titulo} devolvido com sucesso")
        else:
            print(f'Livro {titulo} já está foi devolvido')
    else:
        print('Livro não encontrado')

# Função para remover Livros

def remover_livro(titulo):
    livro = buscar_livro(titulo)
    if livro:
        livros.remove(livro)
        print(f'Livro {titulo} removido com sucesso')
    else:
        print(f'Livro não encontrado')


cadastrar_livro("O Senhor dos Anéis", "Tolkien", 1954)
cadastrar_livro("1984", "George Orwell", 1949)
cadastrar_livro("Dom Casmurro", "Machado de Assis", 1899)

# Empréstimos
emprestar_livro("1984")
emprestar_livro("1984")        # já está emprestado

# Devolução
devolver_livro("1984")
devolver_livro("Dom Casmurro") # já está disponível

# Remoção
remover_livro("O Senhor dos Anéis")
remover_livro("Harry Potter")  # não existe

# Listagem final
listar_livros()


