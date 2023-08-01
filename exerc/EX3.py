pessoas = 10
sexo_masc = 0
sexo_fem = 0
altura_maior = 0
altura_menor = 0
conta_voltas = 0
altura_mulher = 0

altura_do_maior = 0
altura_do_maior2 =0 

sexomaisalto = 0
for pessoa in range(pessoas):
    print(f'Pessoa: {pessoa+1}')
    
    conta_voltas += 1
    altura = float(input("Digite a altura: "))
    sexo = input("Digite o sexo: ")
    if altura > altura_maior:
        altura_maior = altura
        sexomaisalto = sexo
  
    if conta_voltas == 1:
        altura_menor = altura
    else:
        if altura < altura_menor:
            altura_menor = altura
        
   

    if sexo == "M" or sexo == "m":
        sexo_masc += 1
    else:
        sexo_fem += 1
        altura_mulher += altura

    if altura_maior == "M" or altura_maior == "m":
        altura_do_maior += 1 
    else:
        altura_do_maior2 += 1
    


media_mulher = altura_mulher / sexo_fem
print(f'A maior altura é: {altura_maior}')
print(f'A menor altura é: {altura_menor}')
print(f'A media de altura das mulheres é: {media_mulher}')
print(f'O numero de homens é: {sexo_masc}')
print(f'O sexo mais alto é: {sexomaisalto}')