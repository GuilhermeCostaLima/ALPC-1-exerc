num1 = int(input("Digite um numero"))
num2 = int(input("Digite o numero final"))


for numero in range(num1, num2+1):
    if numero % 2 == 1:
        print(numero, end=" ")

    if numero % 2 == 0:
        print(numero, end=" ")

    print(f'{numero} {numero}')
