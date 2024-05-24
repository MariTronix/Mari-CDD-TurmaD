class JogoDaVelha():
    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.escolhaDoJogador1 = "X"
        self.escolhaDoJogador2 = "O"

    """def escolha(self):
        self.escolhaDoJogador1 = input(f"{self.jogador1}, você escolhe X  ou O: ").upper()
        while self.escolhaDoJogador1 not in ["X", "O", "0"]:
            self.escolhaDoJogador1 = input(f"{self.jogador1}, você escolhe X  ou O: ").upper()

        if self.escolhaDoJogador1 == "X":
            self.escolhaDoJogador2 = "O"
        else:
            self.escolhaDoJogador2 = "X"

        print(self.escolhaDoJogador1)
        print(self.escolhaDoJogador2)"""

    def resultado(self):

        matriz = [
            ["-","-","-"],
            ["-","-","-"],
            ["-","-","-"]
        ]

        for x in range(0, 3):
            for y in range(0, 3):
                print(matriz[x][y], end="")
            print()

        print("Linhas A,B e C e Colunas 1,2 e 3 \n Jogador 1 = X \n Jogador 2 = O")

        primeiraJogadaDo01 = input(f"Qual é a sua primeira jogada {self.jogador1}: ").upper()
        if primeiraJogadaDo01 in ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]:
            if primeiraJogadaDo01 == "A1":
                matriz[0].insert(0,"X")
            elif primeiraJogadaDo01 == "A2":
                matriz[0].insert(1,"X")
            elif primeiraJogadaDo01 == "A3":
                matriz[0].insert(2,"X")
            elif primeiraJogadaDo01 == "B1":
                matriz[1].insert(0, "X")
            elif primeiraJogadaDo01 == "B2":
                matriz[1].insert(1, "X")
            elif primeiraJogadaDo01 == "B3":
                matriz[1].insert(2, "X")
            elif primeiraJogadaDo01 == "C1":
                matriz[2].insert(0, "X")
            elif primeiraJogadaDo01 == "C2":
                matriz[2].insert(1, "X")
            elif primeiraJogadaDo01 == "C3":
                matriz[2].insert(2, "X")

        for x in range(0, 3):
            for y in range(0, 3):
                print(matriz[x][y], end=" ")
            print()

        primeiraJogadaDo02 = input(f"Qual é a sua primeira jogada {self.jogador2}")

        if primeiraJogadaDo01 in ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]:
            if primeiraJogadaDo02 == "A1":
                matriz[0].insert(0,"X")
            elif primeiraJogadaDo01 == "A2":
                matriz[0].insert(1,"X")
            elif primeiraJogadaDo02 == "A3":
                matriz[0].insert(2,"X")
            elif primeiraJogadaDo02 == "B1":
                matriz[1].insert(0, "X")
            elif primeiraJogadaDo02 == "B2":
                matriz[1].insert(1, "X")
            elif primeiraJogadaDo02 == "B3":
                matriz[1].insert(2, "X")
            elif primeiraJogadaDo02 == "C1":
                matriz[2].insert(0, "X")
            elif primeiraJogadaDo02 == "C2":
                matriz[2].insert(1, "X")
            elif primeiraJogadaDo02 == "C3":
                matriz[2].insert(2, "X")

        for x in range(0, 3):
            for y in range(0, 3):
                print(matriz[x][y], end=" ")
            print()

        segundaJogadaDo01 = input(f"Qual é a sua primeira jogada {self.jogador1}")
        if segundaJogadaDo01 == "A1":
            matriz[0].insert(0, "X")
        elif segundaJogadaDo01 == "A2":
            matriz[0].insert(1, "X")
        elif segundaJogadaDo01 == "A3":
            matriz[0].insert(2, "X")
        elif segundaJogadaDo01 == "B1":
            matriz[1].insert(0, "X")
        elif segundaJogadaDo01 == "B2":
            matriz[1].insert(1, "X")
        elif segundaJogadaDo01 == "B3":
            matriz[1].insert(2, "X")
        elif segundaJogadaDo01 == "C1":
            matriz[2].insert(0, "X")
        elif segundaJogadaDo01 == "C2":
            matriz[2].insert(1, "X")
        elif segundaJogadaDo01 == "C3":
            matriz[2].insert(2, "X")

        for x in range(0, 3):
            for y in range(0, 3):
                print(matriz[x][y], end=" ")
            print()

    segundaJogadaDo02 = input(f"Qual é a sua primeira jogada {self.jogador2}")






p1 = JogoDaVelha("Mari", "Lipe")
p1.resultado()