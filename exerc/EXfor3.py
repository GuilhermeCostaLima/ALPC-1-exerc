# Faça um algoritmo que calcule a soma de todos os números ímpares dentro de uma faixa de valores determinada pelo usuário. 
# Um número é ímpar quando sua divisão por 2 não é exata, ou seja, o resto resultante da divisão inteira pelo número 2 tem valor 1. 
# Utilize a palavra resto como operador que calcula o resto da divisão de um numero por outro.


num1 = int(input("Digite o numero inicial: "))
num2 = int(input("Digite o numero final: "))

soma_impar = 0

print("______________________________\n")
print("Os numeros impares são")
for numero in range(num1, num2+1):

    if numero % 2 == 1:    
        soma_impar += numero
        print(numero, end=" ")
print("\n______________________________")  
print(f'A soma dos numeros impares é: {soma_impar}')




