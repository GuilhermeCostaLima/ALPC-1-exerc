nome = input("Qual o seu nome: ")
sal = float(input("Qual o seu salario? "))
tempserv = int(input("Qual o seu tempo de servico? "))

#imposto
if sal < 200:
    print("Isento")
else:
    if sal > 200 and sal <= 450:
        impbase = sal - (sal * 3 / 100)
        # print(impbase)
    else:
        if sal >= 450 and sal <= 700:
            impbase = sal - (sal * 8 / 100)
            # print(impbase)
        else:
            if sal == 700:
                impbase = sal - (sal * 10 / 100)
                # print(impbase)
            else:
                if sal > 700:
                    impbase = sal - (sal * 12 / 100)
                    # print(impbase)
#gratificação
if sal > 500 and tempserv <= 3:
    grat = (sal * 2) / 100
    gratfinal = sal + 50
    # print(gratfinal)
else:
    if sal > 500 and tempserv > 3:
        grat = (sal * 3) / 100
        gratfinal = sal + 60
        # print(gratfinal)
    else:
        if sal <= 500 and tempserv < 3:
            grat = (sal * 5) / 100
            gratfinal = sal + 23
            # print(gratfinal)
        else:
            if sal <= 500 and tempserv < 6:
                grat = (sal * 6) / 100
                gratfinal = sal + 35
                # print(gratfinal)
            else:
                if sal <= 500 and tempserv > 6:
                    grat = (sal * 10) / 100
                    gratfinal = sal + 33
                    # print(gratfinal)
#auxilio alimentação
if tempserv <= 10 or tempserv > 10:
    aux = (sal * 4) / 100
else:
	aux = (sal * 6) / 100
# print(aux)

salliquido = (sal + gratfinal + aux) - impbase 
# print(salliquido)

print("Nome: ", nome)
print(f'Seu salario liquido é ${salliquido:.2f}')

