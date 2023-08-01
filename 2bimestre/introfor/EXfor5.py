'''
Faça um algoritmo que calcule a média de todas as turmas de uma escola. Considere como entradas o número de turmas e o número de alunos de cada turma. 
A média de cada turma deve ser apresentada, além da média geral, que será o resultado da média das turmas.
'''

turma1 = int(input("Numero de turmas existentes: "))

somarmedias = 0
for contaturma in range(turma1):
    print("Turma", contaturma+1)
    alunos = int(input("Numero de alunos da turma: "))
    soma = 0
    for contaluno in range(alunos):
        print("Aluno", contaluno + 1)
        nota = float(input("Digite a nota: "))
        soma += nota
    media = soma / alunos
    print("A media dos alunos é:", media)
    somarmedias += media
media2 = somarmedias / turma1
print("media de todas as turmas é", media2)
