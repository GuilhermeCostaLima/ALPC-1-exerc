omaiornum = 0
omenornum = 0
conta = 0
while True:
    num = int(input("Digite um numero: "))
    if num < 0:
        break
    if num > omaiornum:
        omaiornum = num
    #nunca misturar a logia do maior com o menor
    if conta == 0:
        omenornum = num 
    else:
        if num < omenornum:
            omenornum = num
    conta += 1

print("maior",omaiornum) 
print("menor",omenornum)