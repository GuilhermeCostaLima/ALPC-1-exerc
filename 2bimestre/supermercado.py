precoproduto = float(input("Preço do produto: "))
vendmensal = float(input("Valor da venda média mensal: "))

if vendmensal < 500 and precoproduto < 30:
    aument = (precoproduto * 12)/100
    aumentotal = precoproduto + aument
    print(f'Reajuste de ${aumentotal:.2f}')
else:
    if vendmensal >= 500 and vendmensal < 1600 and precoproduto >= 30 and precoproduto < 80:
        aument = (precoproduto * 15)/100
        aumentotal = precoproduto + aument
        print(f'Reajuste de ${aumentotal:.2f}')
    else:
        if vendmensal >= 1600 and precoproduto >= 80:
            dimi = (precoproduto * 25)/100
            dimitotal = precoproduto - dimi
            print(f'Reajuste de ${dimitotal:.2f}')