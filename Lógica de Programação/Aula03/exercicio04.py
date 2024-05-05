# Ler o nome de 2 times e o número de gols
# marcados na partida (para cada time).
# Escrever o nome do vencedor. Caso não
# haja vencedor deverá ser impressa a palavra empate

#Variáveis para nomes do times e os gols delas.
timeDaCasa = input("Nome do time da casa: ")
golsDoTimeDaCasa = int(input("Quantos gols os time da casa fez:"))
timeDeFora = input("Nome do time de fora: ")
golsDoTimeDeFora = int(input("Quantos gols os time de fora fez:"))

#decisão para saber o vencendor ou empate.
if golsDoTimeDaCasa == golsDoTimeDeFora:
    print("Empate")
elif golsDoTimeDeFora < golsDoTimeDaCasa:
    print(f"{timeDaCasa} venceu")
else:
    print(f"{timeDeFora} venceu")