import json

class Carro:
    def __init__(self,marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
carros = [
    Carro("Toyota", "Corolla", 2020),
    Carro("Honda", "Civic", 2019),
    Carro("Ford", "Mustang", 2022)
]

def salvar(lista_carros):
    dados = []
    for carro in lista_carros:
        dados.append({
            'marca': carro.marca,
            'modelo': carro.modelo,
            'ano': carro.ano,
        })
    with open("carros.json", "w", encoding='utf-8') as f:
        json.dump(dados, f)

def carregar():
    try:
        with open("carros.json", "r", encoding='utf-8') as f:
            dados = json.load (f)
            carros_carregados = []
            for dado in dados:
                carros_carregados.append(Carro(dado['marca'], dado['modelo'], dado['ano']))
            return carros_carregados
    except FileNotFoundError:
        return []

salvar(carros)

carros_carregados = carregar()
for carro in carros_carregados:
    print(f'{carro.marca} {carro.modelo} ({carro.ano})')