# Faça um programa que leia um número N que indica quantos valores inteiros e positivos devem ser lidos a seguir. Para cada número lido, mostre o valor lido e o fatorial desse valor.

n = int(input("Digite um numero de fatoriais: "))

fatorial = 1
resultado = 1

while fatorial <= n:
    print(fatorial, end=" ")
    resultado = resultado * fatorial
    fatorial = fatorial + 1
print(" = ", resultado)

     
    
    