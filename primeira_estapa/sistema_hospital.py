import json

class Paciente:

    def __init__(self,nome,idade,internado = False):
        self.nome = nome
        self.idade = idade
        self.internado = internado

    def internar(self):
        if not self.internado:
            print(f'Paciente {self.nome} internado')
            self.internado = True
        else:
            print(f'Paciente já {self.nome} internado')
    
    def dar_alta(self):
        if self.internado:
            print(f'Alta Liberada ao paciente {self.nome}')
            self.internado = False
        else:
            print(f'Paciente {self.nome} não está internado')
    
    def detalhes(self):
        situacao = "Internado" if self.internado else "Não internado"
        print(f'Nome: {self.nome} | Idade: {self.idade} | Situação: {situacao}')
    
pacientes = []

def salvar_dados():
    dados = []
    for paciente in pacientes:
        dados.append({
            'nome': paciente.nome,
            'idade': paciente.idade,
            'internado': paciente.internado
        })
    with open('hospital.json', 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def carregar_dados():
    try:
        with open('hospital.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
            for d in dados:
                if not buscar_paciente(d['nome']):  # só adiciona se não existir
                    pacientes.append(Paciente(d['nome'], d['idade'], d['internado']))
    except FileNotFoundError:
        pass

def buscar_paciente(nome):
    for paciente in pacientes:
        if paciente.nome == nome:
            return paciente
    return None
    
def cadastrar_paciente(nome,idade):
    if buscar_paciente(nome):
        return f"Paciente '{nome}' já cadastrado."
    novo_paciente = Paciente(nome,idade)
    pacientes.append(novo_paciente)
    salvar_dados()
    return f"Paciente '{nome}' cadastrado com sucesso."

def listar_pacientes():
    if not pacientes:
        return "Nenhum paciente cadastrado."
    for paciente in pacientes:
        paciente.detalhes()
    return "Lista de pacientes exibida."

def remover_paciente(nome):
    paciente = buscar_paciente(nome)
    if paciente:
        pacientes.remove(paciente)
        salvar_dados()
        return f"Paciente '{nome}' removido com sucesso."
    return f"Paciente '{nome}' não encontrado."


carregar_dados()

print(cadastrar_paciente("Maria", 45))
print(cadastrar_paciente("João", 32))
print(cadastrar_paciente("Maria", 45))  # duplicata

paciente = buscar_paciente("Maria")
paciente.internar()
paciente.internar()    # já internado
paciente.dar_alta()
paciente.dar_alta()    # já tem alta

print(listar_pacientes())
print(remover_paciente("João"))
print(listar_pacientes())