class Veiculo:

    def __init__(self, marca, modelo, ano, ligado = False):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = ligado
    
    def ligar(self):
        if self.ligado:
            print('Veiculo já está ligado')
        else: 
            self.ligado = True
            print('Veiculo foi ligado com sucesso')

    def desligar(self):
        if not self.ligado:
            print('Veiculo já está desligado')
        else:
            self.ligado = False 
            print('Veiculo desligado com sucesso')
    
    def detalhes(self):
        status = "Ligado" if self.ligado else "Desligado"
        print(f'Marca: {self.marca} | Modelo: {self.modelo} | Ano: {self.ano} | Motor: {status}')
    
class Carro(Veiculo):

    def __init__(self, marca, modelo, ano, num_portas, ligado=False, ):
        super().__init__(marca, modelo, ano, ligado)
        self.num_portas = num_portas
    
    def detalhes(self):
        status = "Ligado" if self.ligado else "Desligado"
        print(f'Marca: {self.marca} | Modelo: {self.modelo} | Ano: {self.ano} | Motor: {status} | Numeros de Portas: {self.num_portas}')
    
class Moto(Veiculo):

    def __init__(self, marca, modelo, ano, cilindrada, ligado=False):
        super().__init__(marca, modelo, ano, ligado)
        self.cilindrada = cilindrada
    
    def detalhes(self):
        status = "Ligado" if self.ligado else "Desligado"
        print(f'Marca: {self.marca} | Modelo: {self.modelo} | Ano: {self.ano} | Motor: {status} | Cilindradas: {self.cilindrada}')
    
carro = Carro("Toyota", "Corolla", 2020, 4)
moto = Moto("Honda", "CB500", 2021, 500)

carro.ligar()
carro.ligar()     # já ligado
carro.detalhes()
carro.desligar()

moto.ligar()
moto.detalhes() 