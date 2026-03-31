numeros = list(range(1, 101))

for numero in numeros:
    if not numero % 3 and not numero % 5:
        print("FizzBuzz")
    elif not numero % 3 :
        print("Fizz")
    elif not numero % 5:
        print("Buzz")
    else:
        print(f'{numero}')