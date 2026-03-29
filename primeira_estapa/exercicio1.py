# Lista para armazenar os usuários
usuarios = []

# Função para cadastrar um novo usuário
def cadastrar_usuario(nome, email, idade):
    print("=== Cadastro de Usuários ===")
    usuario = {
        "nome": nome,
        "email": email,
        "idade": idade
    }
    usuarios.append(usuario)
    print(f"Usuário {nome} adicionado com sucesso")

# Função para listar todos os usuários
def listar_usuarios():
    print("=== Usuários cadastrados ===")
    for usuario in usuarios:
        print(f"- Nome: {usuario['nome']} | Email: {usuario['email']} | Idade: {usuario['idade']}")

# Função buscar usuário por nome
def buscar_usuario(nome):
    for usuario in usuarios:
        if usuario["nome"] == nome:
            return usuario
        
# Função para atualizar e-mail de um usuário
def atualizar_email(nome, novo_email):
    print(f'=== Aletração de E-mail ===')
    usuario = buscar_usuario(nome)
    if usuario:
        print(f"E-mail antigo: {usuario["email"]}")
        usuario["email"] = novo_email
        print(f"E-mail Atual: {usuario["email"]}")
    else:
        print(f"Impossivel alterar o e-mail pois o nome {nome} não existe")

# Função para deletar usuários
def deletar_usuario(nome):
    print(f'=== Remoção de Usuário ===')
    usuario = buscar_usuario(nome)
    if usuario:
        usuarios.remove(usuario)
        print(f"Usuário {nome} removido com sucesso")
    else:
        print(f"Impossivel remover usuário {nome} pois o mesmo não existe")     

# Teste

cadastrar_usuario("Alice", "alice@email.com", 25)
cadastrar_usuario("Bob", "bob@email.com", 30)
cadastrar_usuario("Charlie", "charlie@email.com", 35)

atualizar_email("Bob", "bob_novo@email.com")
deletar_usuario("Charlie")
deletar_usuario("Zé")

listar_usuarios()