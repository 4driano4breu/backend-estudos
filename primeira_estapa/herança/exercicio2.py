class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def detalhes(self):
        print(f'Nome: {self.nome} | Salario: {self.salario}')
    
    def aumentar_salario(self, percentual):
        self.salario += (percentual / 100) * self.salario
        print(f'Salario atual: {self.salario}')


class Gerente(Funcionario):

    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento
    
    def detalhes(self):
        print(f'Nome: {self.nome} | Salario: {self.salario} | Departamento: {self.departamento}')

class Desenvolvedor(Funcionario):
        
    def __init__(self, nome, salario, linguagens):
        super().__init__(nome, salario)
        self.linguagens = linguagens

    def detalhes(self):
        print(f'Nome: {self.nome} | Salario: {self.salario} | Linguagens: {self.linguagens}')
    
class Estagiario(Funcionario):
        
    def __init__(self, nome, salario, curso):
        super().__init__(nome, salario)
        self.curso = curso

    def detalhes(self):
        print(f'Nome: {self.nome} | Salario: {self.salario} | Curso: {self.curso}')

    def aumentar_salario(self, percentual):
        if percentual > 10:
            print(f'Não é possivel aumentar {percentual}% do salário')
        else:
            super().aumentar_salario(percentual)

gerente = Gerente("Ana", 8000, "TI")
dev = Desenvolvedor("Carlos", 6000, "Python")
estagiario = Estagiario("João", 1500, "Ciência da Computação")

gerente.detalhes()
gerente.aumentar_salario(15)
gerente.detalhes()

dev.aumentar_salario(20)
dev.detalhes()

estagiario.aumentar_salario(5)    # pode
estagiario.aumentar_salario(15)   # não pode
estagiario.detalhes()