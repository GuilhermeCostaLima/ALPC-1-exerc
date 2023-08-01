altura = float(input("Digite sua altura: "));
sexo = input("M ou F, qual o seu sexo? ");

if sexo == 'm' or sexo == 'M':
    peso = (72.7* altura) - 58
    # print(f'seu peso é {peso:.2f}')
else:
    peso = (62.1 * altura) - 44.7
    # print(f'seu peso é {peso:.2f}')
print(f'O peso ideal é {peso:.2f}')
