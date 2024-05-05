x = 0
while x < 100:
    acao = input("Escolha Pedra ou Papel ou Tesoura: ")
    acao2 = input("Escolha Pedra ou Papel ou Tesoura: ")

    acao = acao.lower()
    acao2 = acao2.lower()

    if (acao == "pedra") and (acao2 == "pedra"):
        print("Empate")
    elif (acao == "pedra") and (acao2 == "papel"):
        print("Papel venceu")
    elif (acao == "pedra") and (acao2 == "tesoura"):
        print("Pedra venceu")
    elif (acao == "papel") and (acao2 == "pedra"):
        print("Papel venceu")
    elif (acao == "papel") and (acao2 == "papel"):
        print("Empate")
    elif (acao == "papel") and (acao2 == "tesoura"):
        print("Tesoura venceu")
    elif (acao == "Tesoura") and (acao2 == "pedra"):
        print("Pedra venceu")
    elif (acao == "Tesoura") and (acao2 == "papel"):
        print("Tesoura venceu")
    elif (acao == "Tesoura") and (acao2 == "tesoura"):
        print("Empate")
    else:
        print("Tente novamente")
    decisao = input("Deseja continuar?(Sim ou Não)")
    decisao = decisao.lower()

    if decisao == "não" or decisao == "nao":
        x += 100