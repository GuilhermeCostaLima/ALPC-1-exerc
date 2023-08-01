n = int(input("Digite um numero para saber o seu fatorial: "))

if n < 0:
    print("valor invalido")
else:
    fatorial = 1
    resultado = 1

for fatorial in range(1,n + 1):
    print(fatorial, end=" ")
    resultado *= fatorial
    fatorial += 1
    
print(f'\n{n}! = {resultado}')



# Correção Walter

fat = int(input("Digite um numero"))

if fat < 0:
    print("Valor invalido")
else:
    cont = fat
    resultado = 1
    while cont > 0:
        resultado *= cont
        cont -= 1
    print(f'\n{fat}! = {resultado}')
    