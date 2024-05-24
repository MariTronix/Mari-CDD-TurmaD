class PedraPapelTesoura():
      def __init__(self, jogador1, jogador2):
          self.jogador1 = jogador1
          self.jogador2 = jogador2
          self.jogada1 = ""
          self.jogada2 = ""
          self.pontos_jogador1 = 0
          self.pontos_jogador2 = 0

      def resultado(self):
          rodadas=1
          while rodadas < 4:
              if self.pontos_jogador1 == 2:
                  print(f"{self.jogador1} Venceu o jogo")
                  break
              elif self.pontos_jogador2 == 2:
                  print(f"{self.jogador2} Venceu o jogo")
                  break

              print(f"Rodada {rodadas}º ")

              self.jogada1=input("Escolha Papel, Pedra ou Tesoura: ")
              self.jogada2=input("Escolha Papel, Pedra ou Tesoura: ")

              if self.jogada1 == self.jogada2:
                  rodadas += 1
                  print("Empate")
                  print((f"{self.jogador1} - {self.pontos_jogador1} X {self.pontos_jogador2} - {self.jogador2}"))

              elif (self.jogada1 == "pedra" and self.jogada2 == "tesoura") or (self.jogada1 == "papel" and self.jogada2 == "pedra") or (self.jogada1 == "tesoura" and self.jogada2 == "papel"):
                  self.pontos_jogador1 += 1
                  print(f"{self.jogador1} venceu essa rodada")
                  print((f"{self.jogador1} - {self.pontos_jogador1} X {self.pontos_jogador2} - {self.jogador2}"))
                  rodadas += 1

              elif (self.jogada2 == "pedra" and self.jogada1 == "tesoura") or (self.jogada2 == "papel" and self.jogada1 == "pedra") or (self.jogada2 == "tesoura" and self.jogada1 == "papel"):
                  self.pontos_jogador2 += 1
                  print(f"{self.jogador2} venceu essa rodada")
                  print((f"{self.jogador1} - {self.pontos_jogador1} X {self.pontos_jogador2} - {self.jogador2}"))
                  rodadas += 1

          else:
              if self.pontos_jogador1 == self.pontos_jogador2:
                  print("O jogo acabou empatado")

p1 = PedraPapelTesoura("Mari", "Lipe")
p1.resultado()

