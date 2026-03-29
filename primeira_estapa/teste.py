nome = "João"          # string (texto)
idade = 25             # int (número inteiro)
altura = 1.75          # float (número decimal)
ativo = True           # bool (verdadeiro/falso)

print(nome, idade, altura, ativo)

# Lista — uma sequência de itens
linguagens = ["Python", "JavaScript", "Go"]
print(linguagens[0])        # Python
linguagens.append("Rust")   # adiciona ao final
print(len(linguagens))      # 4

# Dicionário — chave e valor (como um objeto JSON)
usuario = {
    "nome": "Ana",
    "idade": 28,
    "ativo": True
}
print(usuario["nome"])      # Ana
usuario["email"] = "ana@email.com"   # adiciona nova chave

def saudacao(nome):
    return f"Olá, {nome}! Bem-vindo ao backend."

print(saudacao("Carlos"))  # Olá, Carlos! Bem-vindo ao backend.


