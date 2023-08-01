precodeproduto = float(input("Valor do produto:"));

if precodeproduto <= 50:
    percentual_aumento = (precodeproduto * 5) / 100
    percentual_final = percentual_aumento + precodeproduto
    # print(percentual_aumento);
else:
    if precodeproduto <= 100:
        percentual_aumento = (precodeproduto * 10) / 100
        percentual_final = percentual_aumento + precodeproduto
        # print(percentual_aumento);
    else:
        if precodeproduto >= 100:
            percentual_aumento = (precodeproduto * 15) / 100
            percentual_final = percentual_aumento + precodeproduto
            # print(percentual_aumento);

if percentual_final <= 80:
    print("barato");
else:
    if percentual_final <= 120:
        print("Normal");
    else:
        if percentual_final <= 200:
            print("Caro");
        else:
            print("Muito Caro");

