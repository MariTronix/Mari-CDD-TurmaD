class PedraPapelTesoura:
    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.jogada1 = ""
        self.jogada2 = ""

    def resultado(self):

        self.jogada1 = primeiraJogada.lower()
        self.jogada2 = segundaJogada.lower()

        if self.jogada1 not in ["pedra", "papel", "tesoura"] or self.jogada2 not in ["pedra", "papel", "tesoura"]:
            print("Jogada inválida. Tente novamente...")

        elif self.jogada1 ==  self.jogada2:
            print("Empate")

        elif self.jogada1 == "pedra" and self.jogada2 == "papel":
            print(f"Papel venceu \n{self.jogador2} Venceu")

        elif self.jogada1 == "pedra" and self.jogada2 == "tesoura":
            print(f"Pedra venceu \n{self.jogador1} Venceu")

        elif self.jogada1 == "papel" and self.jogada2 == "pedra":
            print(f"Papel venceu \n{self.jogador1} Venceu")

        elif self.jogada1 == "papel" and self.jogada2 == "tesoura":
            print(f"Tesoura venceu \n{self.jogador2} Venceu")

        elif self.jogada1 == "tesoura" and self.jogada2 == "pedra":
            print(f"Pedra venceu \n{self.jogador2} Venceu")

        elif self.jogada1 == "tesoura" and  self.jogada2 == "papel":
            print(f"Tesoura venceu \n{self.jogador1} Venceu")

p1 = PedraPapelTesoura("Mari", "Lipe")

p1.resultado()