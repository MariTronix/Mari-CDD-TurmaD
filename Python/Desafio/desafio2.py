class PedraPaPelTesoura:
    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.jogada1 = ""
        self.jogada2 = ""

    def resultado(self, primeiraJogada, segundaJogada):

        self.jogada1 = primeiraJogada.lower()
        self.jogada2 = segundaJogada.lower()

        if self.jogada1 == "pedra" and self.jogada2 == "pedra":
            print("Empate")

        elif self.jogada1 == "pedra" and self.jogada2 == "papel":
            print(f"Papel venceu \n{self.jogador2} Venceu")

        elif self.jogada1 == "pedra" and self.jogada2 == "tesoura":
            print(f"Pedra venceu \n{self.jogador1} Venceu")

        elif self.jogada1 == "papel" and self.jogada2 == "pedra":
            print(f"Papel venceu \n{self.jogador1} Venceu")

        elif self.jogada1 == "papel" and self.jogada2 == "papel":
            print("Empate")

        elif self.jogada1 == "papel" and self.jogada2 == "tesoura":
            print(f"Tesoura venceu \n{self.jogador2} Venceu")

        elif self.jogada1 == "tesoura" and self.jogada2 == "pedra":
            print(f"Pedra venceu \n{self.jogador2} Venceu")

        elif self.jogada1 == "tesoura" and  self.jogada2 == "papel":
            print(f"Tesoura venceu \n{self.jogador1} Venceu")

        elif self.jogada1 == "tesoura" and  self.jogada2 == "tesoura":
            print("Empate")
        else:
            print("Tente novamente")