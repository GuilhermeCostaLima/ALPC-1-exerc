salario_minimo = float(input("Digite o valor do salário mínimo: "))
quilowatt_valor = salario_minimo / 8
faturamento_geral = 0
consumidores_entre_500_e_1000 = 0

while True:
    quilowatts = float(input("Digite a quantidade de quilowatts gasta pelo consumidor (0 para encerrar): "))
    
    if quilowatts == 0:
        break
    
    tipo_consumidor = int(input("Digite o tipo do consumidor (1-Residencial, 2-Comercial, 3-Industrial): "))
    
    valor_a_pagar = quilowatts * quilowatt_valor
    
    if tipo_consumidor == 1:
        valor_a_pagar *= 1.05
    elif tipo_consumidor == 2:
        valor_a_pagar *= 1.10
    elif tipo_consumidor == 3:
        valor_a_pagar *= 1.15
    
    faturamento_geral += valor_a_pagar
    
    if 500 <= valor_a_pagar <= 1000:
        consumidores_entre_500_e_1000 += 1
    
    print(f"Valor a ser pago: R${valor_a_pagar:.2f}\n")
    
print(f"Faturamento geral da empresa: R${faturamento_geral:.2f}")
print(f"Quantidade de consumidores que pagam entre R$ 500,00 e R$ 1000,00: {consumidores_entre_500_e_1000}")
