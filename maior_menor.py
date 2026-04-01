def maior_menor(lista):
    maior = lista[0]
    menor = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    
    print(f'Maior: {maior} | Menor: {menor}')
    
maior_menor([3, 1, 7, 2, 9, 4])    # Maior: 9 | Menor: 1
maior_menor([100, 50, 200, 75])     # Maior: 200 | Menor: 50
maior_menor([-5, -1, -10, -3])      # Maior: -1 | Menor: -10