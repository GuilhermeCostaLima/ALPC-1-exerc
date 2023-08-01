# Faça um programa que leia um valor N inteiro e positivo. Calcule e mostre o valor de E, conforme a fórmula a seguir:
# E = 1 + 1/(1!) + 1/(2!) + 1/(3!) + ... + 1/(N!)

n = 0
e = 1

while n >= 0:
    if n >= 0:
        n = n + 1
        e = 1 + (1 / n)
    print(e)



n = int(input("Digite um valor inteiro e positivo: "))
e = 1
fatorial = 1

while n > 0:
    fatorial *= n
    e += 1 / fatorial
    n -= 1

print("O valor de E é:", e)




n = int(input("Digite um valor inteiro e positivo: "))

e = 1  # Inicializa o valor de E como 1
fatorial = 1
i = 1

# Calcula o valor de E usando a fórmula
while i <= n:
    fatorial *= i
    e += 1 / fatorial
    i += 1


# Exibe o resultado
print("O valor de E é:", e)

# while n > 0:
#     print(e)
#     e = 1 + 1
#     edois = e / n    
#     print(edois)    