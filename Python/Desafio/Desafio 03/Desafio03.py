class JogoDaVelha():
    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.escolhaDoJogador1 = "X"
        self.escolhaDoJogador2 = "O"

    def resultado(self):
        matriz = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]

        listaDeJogada = []

        print(f"{self.jogador1} = X \n{self.jogador2} = O")
        for x in range(0, 3):
            for y in range(0, 3):
                print(matriz[x][y], end="")
            print()

            for rodada in range(9):

                # Jogador 1
                jogadaDoJogador1 = input(f"Escolha entre 1 e 9 \nQual é a sua jogada {self.jogador1}: ")
                while jogadaDoJogador1 in listaDeJogada:
                    jogadaDoJogador1 = input(
                        f"Essa jogada já foi escolhida. \nQual é a sua jogada {self.jogador1}: ")
                while jogadaDoJogador1 not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    jogadaDoJogador1 = input(
                        f"Jogada inválida, tente novamente. \nQual é a sua jogada {self.jogador1}: ")

                listaDeJogada.append(jogadaDoJogador1)
                print(listaDeJogada)

                # Verificar se o jogador 1 venceu
                if rodada >= 2:
                    if (matriz[0][0] == "X" and matriz[0][1] == "X" and matriz[0][2] == "X") \
                            or (matriz[1][0] == "X" and matriz[1][1] == "X" and matriz[1][2] == "X") \
                            or (matriz[2][0] == "X" and matriz[2][1] == "X" and matriz[2][2] == "X") \
                            or (matriz[0][0] == "X" and matriz[1][0] == "X" and matriz[2][0] == "X") \
                            or (matriz[0][1] == "X" and matriz[1][1] == "X" and matriz[2][1] == "X") \
                            or (matriz[0][2] == "X" and matriz[1][2] == "X" and matriz[2][2] == "X") \
                            or (matriz[0][0] == "X" and matriz[1][1] == "X" and matriz[2][2] == "X") \
                            or (matriz[0][2] == "X" and matriz[1][1] == "X" and matriz[2][0] == "X"):
                        print(f"{self.jogador1} Venceu")
                        print()
                        break
                elif rodada == 9:
                    print("Empate")

                #Posição da jogada do jogador 01

                if jogadaDoJogador1 == "1":
                    matriz[0][0] = self.escolhaDoJogador1
                elif jogadaDoJogador1 == "2":
                    matriz[0][1] = self.escolhaDoJogador1
                elif jogadaDoJogador1 == "3":
                    matriz[0][2] = self.escolhaDoJogador1
                elif jogadaDoJogador1 == "4":
                    matriz[1][0] = self.escolhaDoJogador1
                elif jogadaDoJogador1 == "5":
                    matriz[1][1] = self.escolhaDoJogador1
                elif jogadaDoJogador1 == "6":
                    matriz[1][2] = self.escolhaDoJogador1
                elif jogadaDoJogador1 == "7":
                    matriz[2][0] = self.escolhaDoJogador1
                elif jogadaDoJogador1 == "8":
                    matriz[2][1] = self.escolhaDoJogador1
                elif jogadaDoJogador1 == "9":
                    matriz[2][2] = self.escolhaDoJogador1

                for x in range(0, 3):
                    for y in range(0, 3):
                        print(matriz[x][y], end="")
                    print()

                # Jogador 2

                jogadaDoJogador2 = input(f"Qual é a sua jogada {self.jogador2}: ")

                while jogadaDoJogador2 in listaDeJogada:
                    jogadaDoJogador2 = input(f"Essa jogada já foi escolhida. \nQual é a sua jogada {self.jogador2}: ")
                while jogadaDoJogador2 not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    jogadaDoJogador2 = input(f"Jogada inválida, tente novamente. \nQual é a sua jogada {self.jogador2}: ")

                listaDeJogada.append(jogadaDoJogador2)
                print(listaDeJogada)

                # Verificar se o jogador 2 venceu

                if rodada >= 2:
                    if (matriz[0][0] == "O" and matriz[0][1] == "O" and matriz[0][2] == "O") \
                            or (matriz[1][0] == "O" and matriz[1][1] == "O" and matriz[1][2] == "O") \
                            or (matriz[2][0] == "O" and matriz[2][1] == "O" and matriz[2][2] == "O") \
                            or (matriz[0][0] == "O" and matriz[1][0] == "O" and matriz[2][0] == "O") \
                            or (matriz[0][1] == "O" and matriz[1][1] == "O" and matriz[2][1] == "O") \
                            or (matriz[0][2] == "O" and matriz[1][2] == "O" and matriz[2][2] == "O") \
                            or (matriz[0][0] == "O" and matriz[1][1] == "O" and matriz[2][2] == "O") \
                            or (matriz[0][2] == "O" and matriz[1][1] == "O" and matriz[2][0] == "O"):
                        print(f"{self.jogador2} Venceu")
                        print()
                    elif rodada == 9:
                        print("Empate")

                # Posição da jogada do jogador 02

                if jogadaDoJogador2 == "1":
                    matriz[0][0] = self.escolhaDoJogador2
                elif jogadaDoJogador2 == "2":
                    matriz[0][1] = self.escolhaDoJogador2
                elif jogadaDoJogador2 == "3":
                    matriz[0][2] = self.escolhaDoJogador2
                elif jogadaDoJogador2 == "4":
                    matriz[1][0] = self.escolhaDoJogador2
                elif jogadaDoJogador2 == "5":
                    matriz[1][1] = self.escolhaDoJogador2
                elif jogadaDoJogador2 == "6":
                    matriz[1][2] = self.escolhaDoJogador2
                elif jogadaDoJogador2 == "7":
                    matriz[2][0] = self.escolhaDoJogador2
                elif jogadaDoJogador2 == "8":
                    matriz[2][1] = self.escolhaDoJogador2
                elif jogadaDoJogador2 == "9":
                    matriz[2][2] = self.escolhaDoJogador2

                for x in range(0, 3):
                    for y in range(0, 3):
                        print(matriz[x][y], end="")
                    print()

        print("Jogo Finalizado")

p1 = JogoDaVelha("Mari", "Lipe")
p1.resultado()