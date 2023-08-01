n = int(input("Digite um numero inteiro e positivo: "))

conta = 0

while conta < n:
    fatorial = int(input("digite o numero de fatoriais"))
    outraconta = 1
    resultado = 1
    while outraconta <= fatorial:
        print(outraconta)
        resultado = resultado * outraconta
        outraconta = outraconta + 1
    print(fatorial," = ", resultado)
    conta = conta + 1
