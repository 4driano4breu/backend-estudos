🏋️ Exercício — Classe Produto
Crie uma classe Produto com:
Atributos (no __init__):

nome
preco
quantidade

Métodos:

detalhes() — imprime as informações do produto
adicionar_estoque(quantidade) — adiciona unidades
remover_estoque(quantidade) — remove unidades, se tiver suficiente. Se não, avisa.


Depois de criar a classe, testa assim:
pythonarroz = Produto("Arroz", 5.99, 100)
feijao = Produto("Feijão", 8.50, 50)

arroz.detalhes()
feijao.detalhes()

arroz.adicionar_estoque(50)
arroz.detalhes()

feijao.remover_estoque(200)  # não tem estoque suficiente
feijao.remover_estoque(20)
feijao.detalhes()