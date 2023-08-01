preco = float(input("Qual o preço do produto? "))

valaumento=0
if preco <= 50:
    valaumento = (preco * 5)/100
else:
    #caminho do não 
    if preco > 50 and preco <= 100:
        valaumento = (preco * 10)/100
    else:
        perc=15
valaumento = (preco * 15)/100
novopreco = preco + valaumento
print(f'O novo preco é {novopreco:.2f}')

if novopreco <=80:
    print("Barato")
else:
    if novopreco > 80 and novopreco <= 120:
        print("Normal")
    else:
        if novopreco > 120 and novopreco <= 200:
            print("Caro")
        else:
            print("Muito Caro")