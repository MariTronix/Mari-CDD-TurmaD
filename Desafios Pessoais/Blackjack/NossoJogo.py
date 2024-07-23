from Blackjack import *

compra = ComprarCarta()

decisao = 0

while decisao != 3:
    print("Boas vindas ao jogo de Blackjack!")
    rodada = int(input("Quer iniciar uma nova rodada? 1 - sim 2 - não: \n"))
    if rodada == 1:
        #Comprar das cartas pro usuario e computador

        cartaDoUsuario = compra.comprarCarta()
        cartaDoUsuario1 = compra.comprarCarta()

        while cartaDoUsuario[2] == "A" and cartaDoUsuario1[2] == "A":
            cartaDoUsuario = compra.comprarCarta()
            cartaDoUsuario1 = compra.comprarCarta()


        cartaDoComputador = compra.comprarCarta()
        cartaDoComputador1 = compra.comprarCarta()

        while cartaDoComputador[2] == "A" and cartaDoComputador1[2] == "A":
            cartaDoComputador = compra.comprarCarta()
            cartaDoComputador1 = compra.comprarCarta()

        #Soma da pontuação
        somaDoUsuario = (cartaDoUsuario[0] + cartaDoUsuario1[0])
        somaDoComputador = (cartaDoComputador[0] + cartaDoComputador1[0])


        print(f"Cartas do usuario: {cartaDoUsuario[1]} e {cartaDoUsuario1[1]}\nPontuação: {somaDoUsuario}")
        print(f"Carta do computador:{cartaDoComputador[1]}")

        decisao = int(input("Deseja comprar mais uma carta 1 - sim  2 - não: "))

        if decisao == 1:
            cartaDoUsuario2 = compra.comprarCarta()
            somaDoUsuario = (cartaDoUsuario[0] + cartaDoUsuario1[0] + cartaDoUsuario2[0])
            print(f"Suas cartas: {cartaDoUsuario[1]}, {cartaDoUsuario1[1]} e {cartaDoUsuario2[1]} \nPontuação: {somaDoUsuario}")
            print(f"Carta do computador:{cartaDoComputador[1]}\nPontuação: {cartaDoComputador[0]}")

            decisao = int(input("Deseja comprar mais uma carta 1 - sim  2 - não: "))

            if decisao == 1:
                cartaDoUsuario3 = compra.comprarCarta()
                somaDoUsuario = (cartaDoUsuario[0] + cartaDoUsuario1[0] + cartaDoUsuario2[0] + cartaDoUsuario3[0])

                if somaDoComputador < 15:
                    cartaDoComputador2 = compra.comprarCarta()
                    somaDoComputador = (cartaDoComputador[0] + cartaDoComputador1[0] + cartaDoComputador2[0])
                    if somaDoUsuario == 21 and somaDoComputador < 21:
                        print(f"Suas cartas: {cartaDoUsuario[1]}, {cartaDoUsuario1[1]}, {cartaDoUsuario2[1]} e {cartaDoUsuario3[1]} \nPontuação: {somaDoUsuario} ")
                        print(f"Cartas do computador: {cartaDoComputador[1]}, {cartaDoComputador1[1]} e {cartaDoComputador2[1]} \nPontuação: {somaDoComputador} ")
                        print("Usuario venceu")
                    elif somaDoComputador > 21:
                        print(f"Suas cartas: {cartaDoUsuario[1]}, {cartaDoUsuario1[1]}, {cartaDoUsuario2[1]} e {cartaDoUsuario3[1]} \nPontuação: {somaDoUsuario} ")
                        print(f"Cartas do computador: {cartaDoComputador[1]}, {cartaDoComputador1[1]} e {cartaDoComputador2[1]} \nPontuação: {somaDoComputador} ")
                        print("Usuario venceu")
                    elif somaDoUsuario > 21:
                        print(f"Suas cartas: {cartaDoUsuario[1]}, {cartaDoUsuario1[1]}, {cartaDoUsuario2[1]} e {cartaDoUsuario3[1]} \nPontuação: {somaDoUsuario} ")
                        print(f"Cartas do computador: {cartaDoComputador[1]}, {cartaDoComputador1[1]} e {cartaDoComputador2[1]} \nPontuação: {somaDoComputador} ")
                        print("Computador venceu")
                    elif somaDoUsuario > somaDoComputador:
                        print(f"Suas cartas: {cartaDoUsuario[1]}, {cartaDoUsuario1[1]}, {cartaDoUsuario2[1]} e {cartaDoUsuario3[1]} \nPontuação: {somaDoUsuario} ")
                        print(f"Cartas do computador: {cartaDoComputador[1]}, {cartaDoComputador1[1]} e {cartaDoComputador2[1]} \nPontuação: {somaDoComputador} ")
                        print("Usuario venceu")
                    elif somaDoUsuario < somaDoComputador:
                        print(f"Suas cartas: {cartaDoUsuario[1]}, {cartaDoUsuario1[1]}, {cartaDoUsuario2[1]} e {cartaDoUsuario3[1]} \nPontuação: {somaDoUsuario} ")
                        print(f"Cartas do computador: {cartaDoComputador[1]}, {cartaDoComputador1[1]} e {cartaDoComputador2[1]} \nPontuação: {somaDoComputador} ")
                        print("Computador venceu")
                    elif (somaDoUsuario == 21 and somaDoComputador == 21) or (somaDoUsuario == somaDoComputador):
                        print(f"Suas cartas: {cartaDoUsuario[1]}, {cartaDoUsuario1[1]}, {cartaDoUsuario2[1]} e {cartaDoUsuario3[1]} \nPontuação: {somaDoUsuario} ")
                        print(f"Cartas do computador: {cartaDoComputador[1]}, {cartaDoComputador1[1]} e {cartaDoComputador2[1]} \nPontuação: {somaDoComputador} ")
                        print("Empate")

                else:
                    if somaDoUsuario == 21 and somaDoComputador < 21:
                        print(f"Suas cartas: {cartaDoUsuario[1]}, {cartaDoUsuario1[1]}, {cartaDoUsuario2[1]} e {cartaDoUsuario3[1]} \nPontuação: {somaDoUsuario} ")
                        print(f"Cartas do computador: {cartaDoComputador[1]}, {cartaDoComputador1[1]} \nPontuação: {somaDoComputador} ")
                        print("Usuario venceu")
                    elif somaDoUsuario > 21:
                        print(f"Suas cartas: {cartaDoUsuario[1]}, {cartaDoUsuario1[1]}, {cartaDoUsuario2[1]} e {cartaDoUsuario3[1]} \nPontuação: {somaDoUsuario} ")
                        print(f"Cartas do computador: {cartaDoComputador[1]} e {cartaDoComputador1[1]} \nPontuação: {somaDoComputador} ")
                        print("Computador venceu")
                    elif somaDoUsuario > somaDoComputador:
                        print(f"Suas cartas: {cartaDoUsuario[1]}, {cartaDoUsuario1[1]}, {cartaDoUsuario2[1]} e {cartaDoUsuario3[1]} \nPontuação: {somaDoUsuario} ")
                        print(f"Cartas do computador: {cartaDoComputador[1]} e {cartaDoComputador1[1]} \nPontuação: {somaDoComputador} ")
                        print("Usuario venceu")
                    elif somaDoUsuario < somaDoComputador:
                        print(f"Suas cartas: {cartaDoUsuario[1]}, {cartaDoUsuario1[1]}, {cartaDoUsuario2[1]} e {cartaDoUsuario3[1]} \nPontuação: {somaDoUsuario} ")
                        print(f"Cartas do computador: {cartaDoComputador[1]} e {cartaDoComputador1[1]} \nPontuação: {somaDoComputador} ")
                        print("Computador venceu")
                    elif (somaDoUsuario == 21 and somaDoComputador == 21) or (somaDoUsuario == somaDoComputador):
                        print(f"Suas cartas: {cartaDoUsuario[1]}, {cartaDoUsuario1[1]}, {cartaDoUsuario2[1]} e {cartaDoUsuario3[1]} \nPontuação: {somaDoUsuario} ")
                        print(f"Cartas do computador: {cartaDoComputador[1]}, {cartaDoComputador1[1]} \nPontuação: {somaDoComputador} ")
                        print("Empate")

            elif decisao == 2:
                if somaDoComputador < 15:
                    cartaDoComputador2 = compra.comprarCarta()
                    somaDoComputador = (cartaDoComputador[0] + cartaDoComputador1[0] + cartaDoComputador2[0])

                    if somaDoUsuario == 21 and somaDoComputador < 21:
                        print(f"Suas cartas: {cartaDoUsuario[1]}, {cartaDoUsuario1[1]} e {cartaDoUsuario2[1]} \nPontuação: {somaDoUsuario} ")
                        print(f"Cartas do computador: {cartaDoComputador[1]}, {cartaDoComputador1[1]} e {cartaDoComputador2[1]} \nPontuação: {somaDoComputador} ")
                        print("Usuario venceu")
                    elif somaDoComputador > 21:
                        print(f"Suas cartas: {cartaDoUsuario[1]}, {cartaDoUsuario1[1]} e {cartaDoUsuario2[1]} \nPontuação: {somaDoUsuario} ")
                        print(f"Cartas do computador: {cartaDoComputador[1]}, {cartaDoComputador1[1]} e {cartaDoComputador2[1]} \nPontuação: {somaDoComputador} ")
                        print("Usuario venceu")
                    elif somaDoUsuario > 21:
                        print(f"Suas cartas: {cartaDoUsuario[1]}, {cartaDoUsuario1[1]} e {cartaDoUsuario2[1]} \nPontuação: {somaDoUsuario} ")
                        print(f"Cartas do computador: {cartaDoComputador[1]}, {cartaDoComputador1[1]} e {cartaDoComputador2[1]} \nPontuação: {somaDoComputador} ")
                        print("Computador venceu")
                    elif somaDoUsuario > somaDoComputador:
                        print(f"Suas cartas: {cartaDoUsuario[1]}, {cartaDoUsuario1[1]} e {cartaDoUsuario2[1]} \nPontuação: {somaDoUsuario} ")
                        print(f"Cartas do computador: {cartaDoComputador[1]}, {cartaDoComputador1[1]} e {cartaDoComputador2[1]} \nPontuação: {somaDoComputador} ")
                        print("Usuario venceu")
                    elif somaDoUsuario < somaDoComputador:
                        print(f"Suas cartas: {cartaDoUsuario[1]}, {cartaDoUsuario1[1]} e {cartaDoUsuario2[1]} \nPontuação: {somaDoUsuario} ")
                        print(f"Cartas do computador: {cartaDoComputador[1]}, {cartaDoComputador1[1]} e{cartaDoComputador2[1]} \nPontuação: {somaDoComputador} ")
                        print("Computador venceu")
                    elif (somaDoUsuario == 21 and somaDoComputador == 21) or (somaDoUsuario == somaDoComputador):
                        print(f"Suas cartas: {cartaDoUsuario[1]}, {cartaDoUsuario1[1]} e {cartaDoUsuario2[1]} \nPontuação: {somaDoUsuario} ")
                        print(f"Cartas do computador: {cartaDoComputador[1]}, {cartaDoComputador1[1]} e {cartaDoComputador2[1]} \nPontuação: {somaDoComputador} ")
                        print("Empate")
                else:
                    if somaDoUsuario == 21 and somaDoComputador < 21:
                        print(f"Suas cartas: {cartaDoUsuario[1]}, {cartaDoUsuario1[1]} e {cartaDoUsuario2[1]} \nPontuação: {somaDoUsuario} ")
                        print(f"Cartas do computador: {cartaDoComputador[1]} e {cartaDoComputador1[1]} \nPontuação: {somaDoComputador} ")
                        print("Usuario venceu")
                    elif somaDoUsuario > 21:
                        print(f"Suas cartas: {cartaDoUsuario[1]}, {cartaDoUsuario1[1]} e {cartaDoUsuario2[1]} \nPontuação: {somaDoUsuario} ")
                        print(f"Cartas do computador: {cartaDoComputador[1]} e {cartaDoComputador1[1]} \nPontuação: {somaDoComputador} ")
                        print("Computador venceu")
                    elif somaDoUsuario > somaDoComputador:
                        print(f"Suas cartas: {cartaDoUsuario[1]}, {cartaDoUsuario1[1]} e {cartaDoUsuario2[1]} \nPontuação: {somaDoUsuario} ")
                        print(f"Cartas do computador: {cartaDoComputador[1]} e {cartaDoComputador1[1]} \nPontuação: {somaDoComputador} ")
                        print("Usuario venceu")
                    elif somaDoUsuario < somaDoComputador:
                        print(f"Suas cartas: {cartaDoUsuario[1]}, {cartaDoUsuario1[1]} e {cartaDoUsuario2[1]} \nPontuação: {somaDoUsuario} ")
                        print(f"Cartas do computador: {cartaDoComputador[1]} e {cartaDoComputador1[1]} \nPontuação: {somaDoComputador} ")
                        print("Computador venceu")
                    elif (somaDoUsuario == 21 and somaDoComputador == 21) or (somaDoUsuario == somaDoComputador):
                        print(f"Suas cartas: {cartaDoUsuario[1]}, {cartaDoUsuario1[1]} e {cartaDoUsuario2[1]} \nPontuação: {somaDoUsuario} ")
                        print(f"Cartas do computador: {cartaDoComputador[1]} e {cartaDoComputador1[1]} \nPontuação: {somaDoComputador} ")
                        print("Empate")

        elif decisao == 2:
            if somaDoComputador < 15:
                cartaDoComputador2 = compra.comprarCarta()
                somaDoComputador = (cartaDoComputador[0] + cartaDoComputador1[0] + cartaDoComputador2[0])

                if somaDoUsuario == 21 and somaDoComputador < 21:
                    print(f"Suas cartas: {cartaDoUsuario[1]} e {cartaDoUsuario1[1]} \nPontuação: {somaDoUsuario} ")
                    print( f"Cartas do computador: {cartaDoComputador[1]}, {cartaDoComputador1[1]} e {cartaDoComputador2[1]} \nPontuação: {somaDoComputador} ")
                    print("Usuario venceu")
                elif somaDoComputador > 21:
                    print(f"Suas cartas: {cartaDoUsuario[1]} e {cartaDoUsuario1[1]} \nPontuação: {somaDoUsuario} ")
                    print(f"Cartas do computador: {cartaDoComputador[1]}, {cartaDoComputador1[1]} e {cartaDoComputador2[1]} \nPontuação: {somaDoComputador} ")
                    print("Usuario venceu")
                elif somaDoUsuario > 21:
                    print(f"Suas cartas: {cartaDoUsuario[1]} e {cartaDoUsuario1[1]} \nPontuação: {somaDoUsuario} ")
                    print(f"Cartas do computador: {cartaDoComputador[1]}, {cartaDoComputador1[1]} e {cartaDoComputador2[1]} \nPontuação: {somaDoComputador} ")
                    print("Computador venceu")
                elif somaDoUsuario > somaDoComputador:
                    print(f"Suas cartas: {cartaDoUsuario[1]} e {cartaDoUsuario1[1]} \nPontuação: {somaDoUsuario} ")
                    print(f"Cartas do computador: {cartaDoComputador[1]}, {cartaDoComputador1[1]} e {cartaDoComputador2[1]} \nPontuação: {somaDoComputador} ")
                    print("Usuario venceu")
                elif somaDoUsuario < somaDoComputador:
                    print(f"Suas cartas: {cartaDoUsuario[1]} e {cartaDoUsuario1[1]} \nPontuação: {somaDoUsuario} ")
                    print(f"Cartas do computador: {cartaDoComputador[1]}, {cartaDoComputador1[1]} e {cartaDoComputador2[1]} \nPontuação: {somaDoComputador} ")
                    print("Computador venceu")
                elif (somaDoUsuario == 21 and somaDoComputador == 21) or (somaDoUsuario == somaDoComputador):
                    print(f"Suas cartas: {cartaDoUsuario[1]} e {cartaDoUsuario1[1]} \nPontuação: {somaDoUsuario} ")
                    print("Cartas do computador: {cartaDoComputador[1]}, {cartaDoComputador1[1]} e {cartaDoComputador2[1]} \nPontuação: {somaDoComputador} ")
                    print("Empate")
            else:
                if somaDoUsuario == 21 and somaDoComputador < 21:
                    print(f"Suas cartas: {cartaDoUsuario[1]} e {cartaDoUsuario1[1]} \nPontuação: {somaDoUsuario} ")
                    print(f"Cartas do computador: {cartaDoComputador[1]} e {cartaDoComputador1[1]} \nPontuação: {somaDoComputador} ")
                    print("Usuario venceu")
                elif somaDoUsuario > 21:
                    print(f"Suas cartas: {cartaDoUsuario[1]} e {cartaDoUsuario1[1]} \nPontuação: {somaDoUsuario} ")
                    print(f"Cartas do computador: {cartaDoComputador[1]} e {cartaDoComputador1[1]} \nPontuação: {somaDoComputador} ")
                    print("Computador venceu")
                elif somaDoUsuario > somaDoComputador:
                    print(f"Suas cartas: {cartaDoUsuario[1]} e {cartaDoUsuario1[1]} \nPontuação: {somaDoUsuario} ")
                    print(f"Cartas do computador: {cartaDoComputador[1]} e {cartaDoComputador1[1]} \nPontuação: {somaDoComputador} ")
                    print("Usuario venceu")
                elif somaDoUsuario < somaDoComputador:
                    print(f"Suas cartas: {cartaDoUsuario[1]} e {cartaDoUsuario1[1]} \nPontuação: {somaDoUsuario} ")
                    print(f"Cartas do computador: {cartaDoComputador[1]} e {cartaDoComputador1[1]} \nPontuação: {somaDoComputador} ")
                    print("Computador venceu")
                elif (somaDoUsuario == 21 and somaDoComputador == 21) or (somaDoUsuario == somaDoComputador):
                    print(f"Suas cartas: {cartaDoUsuario[1]} e {cartaDoUsuario1[1]} \nPontuação: {somaDoUsuario} ")
                    print(f"Cartas do computador: {cartaDoComputador[1]} e {cartaDoComputador1[1]} \nPontuação: {somaDoComputador} ")
                    print("Empate")

    elif decisao == 2:
        print("Jogo Finalizado")