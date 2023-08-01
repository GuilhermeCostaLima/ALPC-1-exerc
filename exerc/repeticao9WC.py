soma = 0
contador = 0
omaior = 0
omenor = 0
soma_pares = 0
conta_par = 0
while True:
    numero = int(input("Digite um numero: "))
    if numero == 30000:
        break
    if numero % 2 == 0:
        #numero par
        conta_par += 1
        soma_pares += numero

    soma += numero
    contador += 1
    if numero > omaior:
        omaior = numero
    #nunca misturar a logica do menor com a do maior
    if contador == 1:
        omenor = numero
    else:
        if numero < omenor:
            omenor = numero
    
    
print(f'Soma: {soma}')
print(f'Quantidade é: {contador}')
print("Sua média é:",soma / contador)
print("O maior numero é:", omaior)
print("O menor numero é:", omenor)
if conta_par > 0:
    mediapares = soma_pares / conta_par
print(f'A media dos pares é: {mediapares:.2f}')
print(f'A soma dos pares é: {soma_pares:.2f}')
contimpar = contador - conta_par
percimpar = (contimpar * 100) / contador
print(f'O perc de impares é: {percimpar:.2f}')
