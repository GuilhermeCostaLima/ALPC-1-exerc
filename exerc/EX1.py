aluno = 0
nota1 = 0
nota2 = 0
reprovado = 0
exame = 0
aprovado = 0

for nota in range(aluno,6):
    if aluno > 6:
        break
    else:
        aluno += 1  
        print(f'Aluno #{aluno}')
        nota1 = float(input("digite a primeira nota: " ))
        nota1 == nota1
        nota2 = float(input("digite a segunda nota: "))
        nota2 == nota2
        media = (nota1 + nota2) / 2
        print(f'média do aluno #{aluno} = {media}')

        if media <= 3:
            print(f'REPROVADO :(')
            reprovado += 1
        else:
            if 3 < media < 7:
                print("EXAME :/")
                exame += 1
            else:
                print("APROVADO \o/\o/\o/")
                aprovado += 1
                
print(f'O numero de aprovados: {aprovado}')
print(f'O numero de alunos em exame: {exame}')
print(f'O numero de reprovados: {reprovado}')