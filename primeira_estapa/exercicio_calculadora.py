
while True:
    try:
        n1 = float(input('Digite um numero:'))
        n2 = float(input('Digite outro numero:'))
        break
    except ValueError:
        print("Isso não é um número! Tente de novo.")

while True:
    operador = (input('Qual a operação? (+, -, *, /)'))
    if operador == "+":
        print(n1 + n2)
        break
    elif operador == "-":
        print(n1 - n2)
        break
    elif operador == "*":
        print(n1 * n2)
        break
    elif operador == "/":
        try:
            print(n1 / n2)
            break
        except ZeroDivisionError:
            print('Não é possível dividir por zero! Tente de novo.')
    else:
        print('Isso não é um operador válido tente novamente')
