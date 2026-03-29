class Aluno:

    def __init__(self, nome):
        self.nome = nome
        self.notas = []
    
    def adicionar_nota(self, nota):
        if nota < 0 or nota > 10:
            print('Nota inválidada! Não foi adicionada')
        else:
            self.notas.append(nota)
            print(f'Nota adicionada: {nota}')

    def media(self):
        if not self.notas:
            print('Nenhuma nota cadastrada')
            return None
        return sum(self.notas) / len(self.notas) 

    def situacao(self):
        media = self.media()
        if media is None:
            return
        if media >= 7:
            print(f'{self.nome} Aprovado')
        elif media >= 5:
            print(f'{self.nome} Recuperação')
        else:
            print(f'{self.nome} Reprovado')

    def boletim(self):
        print(f'Nome: {self.nome}')
        print(f'Notas: {self.notas}')
        print(f'Média: {self.media()}')
        self.situacao()

aluno1 = Aluno("João")
aluno2 = Aluno("Maria")

aluno1.adicionar_nota(8)
aluno1.adicionar_nota(7)
aluno1.adicionar_nota(6)
aluno1.adicionar_nota(11)   # nota inválida
aluno1.boletim()

aluno2.adicionar_nota(4)
aluno2.adicionar_nota(3)
aluno2.boletim()

aluno3 = Aluno("Pedro")
aluno3.media()              # sem notas

        