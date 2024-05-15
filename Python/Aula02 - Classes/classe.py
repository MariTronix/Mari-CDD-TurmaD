class Pessoa():
    def __init__(self, nome, peso, idade, comendo = False, falando = False, dormindo = False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        self.dormindo = dormindo

    def comer(self, alimento):

        if self.comendo == False and self.falando == False and self.dormindo == False:
            print(f"{self.nome} está comendo {alimento}")
            self.comendo = True
        elif self.comendo == True and self.falando == False and self.dormindo == False:
            print(f"{self.nome} já está comendo")
        elif self.comendo == False and self.falando == True and self.dormindo == False:
            print(f"{self.nome} já está falando")
        elif self.comendo == False and self.falando == False and self.dormindo == True:
            print(f"{self.nome} está dormindo")

    def pararDeComer(self):

        print(f"{self.nome} parou de comer")
        self.comendo = False

    def falar(self):
        print(f"{self.nome} está falando")
        self.falando = True

    def ParaDeFalar(self):
        print(f"{self.nome} parou de falar")
        self.falando = False

    def dormir(self):
        print(f"{self.nome} foi dormir")
        self.dormindo = True

    def acordo(self):
        print(f"{self.nome} acordou")
        self.dormindo = False