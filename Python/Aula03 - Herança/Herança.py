class Animal():
    def __init__(self,nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"O {self.nome} foi comer...")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)

    def miar(self):
        print(f"O {self.nome} foi miando ...")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def late(self):
        print(f"O {self.nome} foi latir")

class Coelho(Animal):
    def __init__(self,nome, cor):
        super().__init__(nome, cor)

    def pula(self):
        print(f"O {self.nome} foi pular")

class Vaca(Animal):
    def __init__(self,nome, cor):
        super().__init__(nome, cor)

    def mugi(self):
        print(f"O {self.nome} Muuuuuuuuuuuuuuuuuu")

class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(Forma):
    def __init__(self):
        super().__init__()

    def calculaArea(self, altura, base):
        self.area =  base * altura
        print(self.area)

    def calculaPerimetro(self,altura, base):
        self.perimetro = 2*(base + altura)
        print(self.perimetro)

class Triangulo(Forma):
    def __init__(self):
        super().__init__()

    def calculaArea(self, base, altura):
        self.area =  (base * altura) / 2
        print(self.area)

    def calculaPerimetro(self, altura):
        self.perimetro = altura * 3
        print(self.perimetro)


