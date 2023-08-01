
#float = números decimais
valordolar = float(input("Digite o valor em dolar: "));
valorcota = float(input("Digite a cotação de hoje: "));

valorreais = valordolar * valorcota;

print(f'Valor em reais ${valorreais:.2f}');