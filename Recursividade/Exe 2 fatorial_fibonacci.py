def fibonacci(posicao):
    if posicao <= 0:
        print("Deve ser um número positivo")
    elif posicao == 1:
        return 0
    elif posicao == 2:
        return 1
    else:
       return  fibonacci(posicao-1) + fibonacci(posicao-2)

print(fibonacci(8))