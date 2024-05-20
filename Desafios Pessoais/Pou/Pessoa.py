class Pessoa():
    def __init__(self, nome, peso, idade, comendo = False, falando = False, dormindo = False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        self.dormindo = dormindo
    def comer(self, alimento):
        if self.comendo == False:
            self.comendo = True
            print(f"{self.nome} está comendo {alimento}")

        elif self.comendo == True:
            print(f"{self.nome} já está comendo")

    def pararDeComer(self):

        print(f"{self.nome} parou de comer")

    def falar(self):
        print(f"{self.nome} está falando")

    def pararDeFalar(self):
        print(f"{self.nome} parou de falar")

    def dormir(self):
        print(f"{self.nome} está dormindo")

    def acordou(self):
        print(f"{self.nome} acordou")
