class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        if valor >= 0:
            saldo_ant = self.saldo
            self.saldo += valor
            print(f'Saldo Anterior: {saldo_ant} | Saldo Adicionado: {valor} | Saldo Atual: {self.saldo}')
        else:
            print("Favor informar um valor positivo")

    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo Indisponivel')
        elif valor < 0:
            print("Favor informar um valor positivo")
        else:
            saldo_ant = self.saldo
            self.saldo -= valor
            print(f'Saldo Anterior: {saldo_ant} | Saldo Removido: {valor} | Saldo Atual: {self.saldo}')

    def extrato(self):
        print(f'Titular: {self.titular} | Saldo: {self.saldo}')

conta1 = ContaBancaria("Ana")
conta2 = ContaBancaria("Carlos")

conta1.depositar(1000)
conta1.depositar(-50)    # valor inválido
conta1.sacar(200)
conta1.sacar(2000)       # saldo insuficiente
conta1.extrato()

conta2.depositar(500)
conta2.extrato()
    
        