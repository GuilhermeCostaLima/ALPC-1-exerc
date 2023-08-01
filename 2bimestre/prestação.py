# calcular valor da prestação em atraso

# formula: PRESTACAO = VALOR +(VALOR * (TAXA/100) * TEMPOEMDIAS)


valor = float(input("Valor da sua prestação? "));
taxa = float(input("Qual a taxa? "));
tempoemdias = float(input("Tempo do atraso? "));

PRESTACAO = valor + (valor * (taxa / 100) * tempoemdias);

print(f' Valor da prestação {PRESTACAO:.2f}');