import math
import random

class ComprarCarta():
    def __init__(self):
        print()

    def comprarCarta(self):

        #Cria array de cartas
        cartas = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"];

        #Cria array de naipes
        naipes = ["♦️", "♥️", "♣️", "♠️"];

        #Sorteia uma carta
        numero = random.choice(cartas)

        #Sorteia um naipe
        naipe = random.choice(naipes)

        valor = 0

        #Verifica se é uma das letras e coloca o valor correspondente na variável valor

        if (numero == "A"):
          valor = 11
        elif (numero == "J" or numero == "Q" or numero == "K"):
          valor = 10
        # Se nao for uma das letras, só converte a string para número
        else:
          valor = int(numero)

      #Cria um objeto da carta com as propriedades que vamos precisar: texto e valor

        carta = numero + naipe
        return valor, carta, numero
