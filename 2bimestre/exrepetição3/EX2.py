# Definindo as constantes
NUM_TIMES = 5
NUM_JOGADORES = 11

# Variáveis para armazenar os resultados
jogadores_menor_idade = 0
soma_idades_time = 0
soma_alturas = 0
jogadores_mais_80kg = 0

# Loop pelos times e jogadores
for i in range(NUM_TIMES):
    print(f"Time {i+1}")
    soma_idades_time_time = 0

    for j in range(NUM_JOGADORES):
        idade = int(input(f"Idade do jogador {j+1}: "))
        peso = float(input(f"Peso do jogador {j+1} (em kg): "))
        altura = float(input(f"Altura do jogador {j+1} (em metros): "))

        if idade < 18:
            jogadores_menor_idade += 1

        soma_idades_time_time += idade
        soma_alturas += altura

        if peso > 80:
            jogadores_mais_80kg += 1

    media_idades_time = soma_idades_time_time / NUM_JOGADORES
    print(f"Média de idades do Time {i+1}: {media_idades_time}\n")

media_alturas = soma_alturas / (NUM_TIMES * NUM_JOGADORES)
percentagem_mais_80kg = (jogadores_mais_80kg / (NUM_TIMES * NUM_JOGADORES)) * 100

print(f"Quantidade de jogadores com idade inferior a 18 anos: {jogadores_menor_idade}")
print(f"Média das alturas de todos os jogadores do campeonato: {media_alturas:.2f} metros")
print(f"Percentagem de jogadores com mais de 80 quilos: {percentagem_mais_80kg:.2f}%")
