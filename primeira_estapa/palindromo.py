def e_palindromo(palavra):
    palavra = palavra.lower()
    if palavra == palavra[::-1]:
        print('É um palindromo')
    else:
        print('Não é um palindromo')

e_palindromo("arara")  
e_palindromo("python") 
e_palindromo("ovo")    
e_palindromo("radar") 
e_palindromo("casa")  