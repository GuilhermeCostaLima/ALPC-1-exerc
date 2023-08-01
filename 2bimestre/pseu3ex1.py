horas_trab_mes = float(input("Quantas horas trabalhadas no mês? "))
salmin = float(input("Qual o salário mínimo? "))
turno_de_trablho = input("Qual o seu turno? ")

if turno_de_trablho == "M" or turno_de_trablho == "m":
    valorcoef = (horas_trab_mes * 10)/100
    saltotal = salmin - valorcoef    
else: 
    if turno_de_trablho == "V" or turno_de_trablho == "v":
        valorcoef = (horas_trab_mes * 15)/100
        saltotal = salmin - valorcoef
    else:
        if turno_de_trablho == "N" or turno_de_trablho == "n":
            valorcoef = (horas_trab_mes * 12)/100
            saltotal = salmin - valorcoef
            
categoria = input("Qual a sua categoria? ")

if categoria == "O" or categoria == "o":
    if saltotal < 300:
        impostbruto = (saltotal * 3)/100
        imp_feito = saltotal - impostbruto
    else:
        if saltotal >=300:
            impostbruto = (saltotal * 5)/100
            imp_feito = saltotal - impostbruto
if categoria == "G" or categoria == "g":
    if saltotal < 400:
        impostbruto = (saltotal * 4)/100
        imp_feito = saltotal - impostbruto
    else:
        if saltotal >= 400:
            impostbruto = (saltotal * 6)/100
            imp_feito = saltotal - impostbruto

if turno_de_trablho == "N" or turno_de_trablho == "n" and horas_trab_mes >= 80:
    gratificação = saltotal + 50
else:
    gratificação = saltotal + 30

if categoria == "O" or categoria == "o":
