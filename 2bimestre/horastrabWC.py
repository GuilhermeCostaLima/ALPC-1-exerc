numhoras = int(input("Digite o numero de horas trab"))
valsalmin = float(input("Digite o valor do salario minimo"))
numhorasextras = int(input("Digite o num de horas extras"))
valhora = valsalmin / 8
print("Valor de hora e ", valhora)
valhoraextra = valsalmin / 4
print("Valor de hora extra e ", valhoraextra)
salbruto = numhoras * valhora
print("O salario bruto e ", salbruto)
tothoraextra = valhoraextra * numhorasextras
print("O total das horas extras e ", tothoraextra)
salarioreceber = salbruto * tothoraextra
print("O salario a receber e ", salarioreceber)