idade1 = 0
idade2 = 0
idade3 = 0
idade4 = 0
idade5 = 0

for idade in range(1,16):
    idadepessoas = int(input("Qual a idade: "))

    if idadepessoas <= 15:
        idade1 += 1 
    if idadepessoas >= 16 and idadepessoas <= 30:
        idade2 += 1
    if idadepessoas >= 31 and idadepessoas <= 45:
        idade3 += 1
    if idadepessoas >= 46 and idadepessoas <= 60:
        idade4 += 1
    if idadepessoas >= 61:
        idade5 += 1

if idade1 == 1:
    print(f'Tem ({idade1} pessoa) na faixa etária de até 15 anos')
    percidade = (idade1 * idade) / 100
    print(f'O percentual é: {percidade}%')
else:
    print(f'Tem ({idade1} pessoas) na faixa etária de até 15 anos')
    percidade = (idade1 * idade) / 100
    print(f'O percentual é: {percidade}%')
if idade2 == 1:
    print(f'Tem ({idade2} pessoa) na faixa etária de 16 a 30 anos')
    percidade = (idade2 * idade) / 100
    print(f'O percentual é: {percidade}%')
else:
    print(f'Tem ({idade2} pessoas) na faixa etária de 16 a 30 anos')
    percidade = (idade2 * idade) / 100
    print(f'O percentual é: {percidade}%')
if idade3 == 1:
    print(f'Tem ({idade3} pessoa) na faixa etária de 31 a 45 anos')
    percidade = (idade3 * idade) / 100
    print(f'O percentual é: {percidade}%')
else:
    print(f'Tem ({idade3} pessoas) na faixa etária de 31 a 45 anos')
    percidade = (idade3 * idade) / 100
    print(f'O percentual é: {percidade}%')
if idade4 == 1:
    print(f'Tem ({idade4} pessoa) na faixa etária de 46 a 60 anos')
    percidade = (idade4 * idade) / 100
    print(f'O percentual é: {percidade}%')
else:
    print(f'Tem ({idade4} pessoas) na faixa etária de 46 a 60 anos')
    percidade = (idade4 * idade) / 100
    print(f'O percentual é: {percidade}%')
if idade5 == 1:
    print(f'Tem ({idade5} pessoa) com 61 ou acima')
    percidade = (idade5 * idade) / 100
    print(f'O percentual é: {percidade}%')
else:
    print(f'Tem ({idade5} pessoas) com 61 ou acima')
    percidade = (idade5 * idade) / 100
    print(f'O percentual é: {percidade}%')
