import json

# Salvar lista em arquivo
def salvar_dados(lista, arquivo):
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)

# Carregar lista de arquivo
def carregar_dados(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []   # se o arquivo não existe ainda, começa com lista vazia