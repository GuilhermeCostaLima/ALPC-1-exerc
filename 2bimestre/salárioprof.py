horastrab = float(input("Horas trabalhadas no dia: "));
valorhora = float(input("Valor da hora aula: "));

horasmes = horastrab * 30

salario = horasmes * valorhora

print(f'Salário bruto de ${salario:.2f}');

inss = float(input("Desconto do INSS: "));

desc = (salario * inss) / 100

salariototal = salario - desc

print(f'Seu salário final será de ${salariototal:.2f}');