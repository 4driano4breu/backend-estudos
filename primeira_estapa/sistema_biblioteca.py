import json

class Livro:
    def __init__ (self, titulo, autor, ano, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = disponivel
    
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False
    
    def devolver(self):
        self.disponivel = True
    
    def detalhes(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        return f"{self.titulo} por {self.autor} ({self.ano}) - {status}"

biblioteca = []

def salvar_dados():
    dados = []
    for livro in biblioteca:
        dados.append({
            'titulo': livro.titulo,
            'autor': livro.autor,
            'ano': livro.ano,
            'disponivel': livro.disponivel
        })
    with open('biblioteca.json', 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def carregar_dados():
    try:
        with open('biblioteca.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
            for d in dados:
                biblioteca.append(Livro(d['titulo'], d['autor'], d['ano'], d['disponivel']))
    except FileNotFoundError:
        pass

def buscar_livro(titulo):
    for livro in biblioteca:
        if livro.titulo.lower() == titulo.lower():
            return livro
    return None

def cadastrar_livro(titulo, autor, ano):
    if buscar_livro(titulo):
        return f"Livro '{titulo}' já cadastrado."
    novo_livro = Livro(titulo, autor, ano)
    biblioteca.append(novo_livro)
    salvar_dados()
    return f"Livro '{titulo}' cadastrado com sucesso."

def listar_livros():
    if not biblioteca:
        return "Nenhum livro cadastrado."
    return "\n".join([livro.detalhes() for livro in biblioteca])

def remover_livro(titulo):
    for livro in biblioteca:
        if livro.titulo == titulo:
            biblioteca.remove(livro)
            return f"Livro '{titulo}' removido com sucesso."
    return f"Livro '{titulo}' não encontrado."


carregar_dados()

print(cadastrar_livro("1984", "George Orwell", 1949))
print(cadastrar_livro("Dom Casmurro", "Machado de Assis", 1899))
print(cadastrar_livro("1984", "George Orwell", 1949))  # duplicata

livro = buscar_livro("1984")
print(livro.emprestar())   # True
print(livro.emprestar())   # False — já emprestado

livro.devolver()
print(listar_livros())
print(remover_livro("Dom Casmurro"))
print(listar_livros())