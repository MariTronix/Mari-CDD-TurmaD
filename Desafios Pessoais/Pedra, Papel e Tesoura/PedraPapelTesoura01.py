pedra = 1
papel = 2
tesoura = 3
x = 0

while x < 100:
    jogador1 = int(input("Escolha sua jogada: 1-Pedra 2-Papel 3-Tesoura: "))
    jogador2 = int(input("Escolha sua jogada: 1-Pedra 2-Papel 3-Tesoura: "))

    if (jogador1 <= 0 or jogador1 >= 4) or (jogador2 <= 0 or jogador2 >=4):
        print("Escolha entre 1-Pedra 2-Papel 3-Tesoura")
    else:
        if jogador1 == jogador2:
            print("Empate")
        elif (jogador1 - jogador2 == 1) or (jogador1 - jogador2 == -2) or (jogador1 - jogador2 == 1):
            print("Jogador 1 venceu")
        else:
            print("Jogador 2 venceu")
    decisao = int(input("Gostaria de continua 1-Sim  2-Não: "))

    if not(decisao == 1 or decisao == 2):
        print("Escolha entre 1-Sim ou 2-Não")

    if decisao == 2:
        x = x + 100
        print("Jogo Encerrado")