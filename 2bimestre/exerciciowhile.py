# numero = 0
# soma = 0
# while numero <= 100:
#     print(numero, end=" ")
#     soma = soma + numero
#     numero = numero + 1
# print(soma)
    




numero = 0
soma = 0
while numero <= 500:
    if numero % 2 == 0: #se conta resto da divisao por 2 é igual a zero entao
        print(numero, end=" ")
        soma = soma + numero
    numero = numero + 1
print(soma)   