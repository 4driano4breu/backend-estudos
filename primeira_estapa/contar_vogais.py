def contar_vogais(texto):
    contador = 0
    for letra in texto:
        if letra in ['a', 'e', 'i', 'o', 'u']:
            contador += 1
    print(f'Quantidade de vogais: {contador}')

contar_vogais("python")       
contar_vogais("programacao")   
contar_vogais("aeiou")         
contar_vogais("rhythm")       
        
    
