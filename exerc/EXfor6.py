salminimo = float(input("Valor do salario minimo: "))
quilowatts = salminimo / 8
faturamento = 0
consumidores = 0


while True:
    watts = float(input("Digite o consumo de quilowatts: "))
    
    if watts == 0:
        break

    consumidor = int(input("Qual o tipo do consumido, 1-Residencial / 2-Comercial / 3-Industrial "))

    apagar = quilowatts * watts

    if consumidor == 1:
        apagar = (apagar * 5) / 100
    else:
        if consumidor == 2:
            apagar = (apagar * 10) / 100
        else:
            if consumidor == 3:
                apagar = (apagar * 15) / 100

    faturamento += apagar

    if apagar >= 500 and apagar <= 1000:
        consumidores += 1
    else:
        if apagar < 500:
            print(f'Consumidores abaixo de 500: {consumidor}')
        else:
            print(f'Consumidores entre 500 e 1000: {consumidor}')
    print(f'Valor a pagar: R${apagar}')

print(f'Faturamento: R${faturamento}')
# print(f'Consumidores entre 500 e 1000: {consumidor}')
