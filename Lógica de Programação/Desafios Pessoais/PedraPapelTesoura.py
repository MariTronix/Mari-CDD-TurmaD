x = 0
while x < 100:
    acao = input("Escolha Pedra ou Papel ou Tesoura: ")
    acao2 = input("Escolha Pedra ou Papel ou Tesoura: ")
    if (acao == "Pedra" or acao == "pedra" or acao == "PEDRA") and (acao2 == "Pedra" or acao2 == "pedra" or acao2 == "PEDRA"):
        print("Empate")
    elif (acao == "Pedra" or acao == "pedra" or acao == "PEDRA") and (acao2 == "Papel" or acao2 == "papel" or acao2 == "PAPEL"):
        print("Papel venceu")
    elif (acao == "Pedra" or acao == "pedra" or acao == "PEDRA") and (acao2 == "Tesoura" or acao2 == "tesoura"):
        print("Pedra venceu")
    elif (acao == "Papel" or acao == "papel" or acao == "PAPEL" ) and (acao2 == "Pedra" or acao2 == "pedra" or acao2 == "PEDRA"):
        print("Papel venceu")
    elif (acao == "Papel" or acao == "papel" or acao == "PAPEL") and (acao2 == "Papel" or acao2 == "papel" or acao2 == "PAPEL"):
        print("Empate")
    elif (acao == "Papel" or acao == "papel" or acao2 == "PAPEL") and (acao2 == "Tesoura" or acao2 == "tesoura" or acao2 == "TESOURA"):
        print("Tesoura venceu")
    elif (acao == "Tesoura" or acao == "Tesoura" or acao == "TESOURA") and (acao2 == "Pedra" or acao2 == "pedra" or acao2 == "PEDRA"):
        print("Pedra venceu")
    elif (acao == "Tesoura" or acao == "Tesoura" or acao == "TESOURA") and (acao2 == "Papel" or acao2 == "papel" or acao2 == "PAPEL"):
        print("Tesoura venceu")
    elif (acao == "Tesoura" or acao == "Tesoura" or acao == "TESOURA") and (acao2 == "Tesoura" or acao2 == "tesoura" or acao2 == "TESOURA"):
        print("Empate")
    else:
        print("Tente novamente")
    decisao = input("Deseja continuar?(Sim ou Não)")
    if decisao == "Não" or decisao == "NÃO" or decisao == "nao" or decisao == "Nao":
        x += 100