class PedraPapelTesoura:
    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.jogada1 = ""
        self.jogada2 = ""

    def resultado(self):

        decisao = 1
        rodadas = 1
        vitoria1 = 0
        vitoria2 = 0

        while decisao == 1:

            while rodadas != 4:

                if vitoria1 == 2 or vitoria2 == 2:
                    break

                print(f"Inicio da {rodadas}º rodada:")

                jogadaDoJogador1 = input(f"Qual é a sua {self.jogador1}?").lower()
                while jogadaDoJogador1 not in ["pedra", "papel", "tesoura"]:
                    jogadaDoJogador1 = input("Jogada inválida. Escreva Pedra, Papel e Tesoura: ").lower()

                jogadaDoJogador2 = input(f"Qual é a sua {self.jogador2}?").lower()
                while jogadaDoJogador2 not in ["pedra", "papel", "tesoura"]:
                    jogadaDoJogador2 = input("Jogada inválida. Escreva Pedra, Papel e Tesoura: ").lower()

                if jogadaDoJogador1 ==  jogadaDoJogador2:
                    print(f"Empate")
                    print(f"{self.jogador1} - {vitoria1} X {vitoria2} - {self.jogador2}")
                    
                elif jogadaDoJogador1 == "pedra" and jogadaDoJogador2 == "papel":
                    vitoria2 += 1
                    print(f"Papel venceu \n{self.jogador2} Venceu")
                    print(f"{self.jogador1} - {vitoria1} X {vitoria2} - {self.jogador2}")

                elif jogadaDoJogador1 == "pedra" and jogadaDoJogador2 == "tesoura":
                    vitoria1 += 1
                    print(f"Pedra venceu \n{self.jogador1} Venceu")
                    print(f"{self.jogador1} - {vitoria1} X {vitoria2} - {self.jogador2}")

                elif jogadaDoJogador1 == "papel" and jogadaDoJogador2 == "pedra":
                    vitoria1 += 1
                    print(f"Papel venceu \n{self.jogador1} Venceu")
                    print(f"{self.jogador1} - {vitoria1} X {vitoria2} - {self.jogador2}")

                elif jogadaDoJogador1 == "papel" and jogadaDoJogador2 == "tesoura":
                    vitoria2 += 1
                    print(f"Tesoura venceu \n{self.jogador2} Venceu")
                    print(f"{self.jogador1} - {vitoria1} X {vitoria2} - {self.jogador2}")

                elif jogadaDoJogador1 == "tesoura" and jogadaDoJogador2 == "pedra":
                    vitoria2 += 1
                    print(f"Pedra venceu \n{self.jogador2} Venceu")
                    print(f"{self.jogador1} - {vitoria1} X {vitoria2} - {self.jogador2}")

                elif jogadaDoJogador1 == "tesoura" and  jogadaDoJogador2 == "papel":
                    vitoria1 += 1
                    print(f"Tesoura venceu \n{self.jogador1} Venceu")
                    print(f"{self.jogador1} - {vitoria1} X {vitoria2} - {self.jogador2}")

                rodadas += 1

            else:
                if vitoria1 > vitoria2:
                    print(f"{self.jogador1} Venceu")

                elif vitoria2 == 3:
                    print(f"{self.jogador2} Venceu")

                else:
                    print("Empate no Jogo")

            decisao = int(input("Jogar novamente: 1- Sim 2-Não"))

            while decisao <= 0 or decisao > 2:
                decisao = int(input("Escolha: 1- Sim 2-Não"))

            if decisao == 1:
                vitoria1 = 0
                vitoria2 = 0
                rodadas = 1
            else:
                print("Saindo")