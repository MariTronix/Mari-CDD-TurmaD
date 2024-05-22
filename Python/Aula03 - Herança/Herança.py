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


class Ingresso():
    def __init__(self, valor):
        self.valor = valor

    def imprime(self):
        print(f"Valor do ingresso: {self.valor}")

class Vip(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)
    def imprime(self):
        vip = self.valor * (100/50)
        print(f"Valor do vip é {vip}")


class Atleta():
    def __init__(self,peso, aposentado = False):
        self.peso = peso
        self.aposentado = aposentado
        self.aquecimento = False

    def aposentar(self):
        if self.aposentado == False:
            self.aposentado = True
            print("Atleta aposentado")

    def aquecer(self):
        if self.aquecimento == False and self.aposentado == False:
            self.aquecimento = True
            print("Atleta aquecido")
        elif self.aquecimento == False and self.aposentado == True:
            print("Atleta Aposentado")
        elif self.aquecimento == True:
            print("Atleta já está aquecido ")

class Corredor(Atleta):
    def __init__(self, peso, aposentado):
        super().__init__(peso, aposentado)

    def correr(self):
        if self.aquecimento == True and self.aposentado == False:
            print("Corredor começou a correr")
        elif self.aquecimento == False:
            print("Corredor não aqueceu")
        elif self.aposentado == True:
            print("Corredor aposentado")
        else:
            print("ERRO")


class Nadador(Atleta):
    def __init__(self, peso, aposentado):
        super().__init__(peso, aposentado)

    def nadar(self):
        if self.aquecimento == True and self.aposentado == False:
            print("Nadador começou a correr")
        elif self.aquecimento == False:
            print("Nadador não aqueceu")
        elif self.aposentado == True:
            print("Nadador aposentado")
        else:
            print("ERRO")

class Ciclista(Atleta):
    def __init__(self, peso, aposentado):
        super().__init__(peso, aposentado)

    def pedalar(self):
        if self.aquecimento == True and self.aposentado == False:
            print("Ciclista começou a correr")
        elif self.aquecimento == False:
            print("Ciclista não aqueceu")
        elif self.aposentado == True:
            print("Ciclista aposentado")
        else:
            print("ERRO")

class TriAtleta(Corredor,Nadador,Ciclista):
    def __init__(self, peso):
        super().__init__(peso)

class CEP():
    def __init__(self):
