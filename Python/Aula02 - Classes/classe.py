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
            print(f"{self.nome} começou a comendo {alimento}")
            self.comendo = True
        elif self.comendo == True and self.falando == False and self.dormindo == False:
            print(f"{self.nome} já está comendo, não pode comer {alimento} agora.")
        elif self.comendo == False and self.falando == True and self.dormindo == False:
            print(f"{self.nome} está falando, não pode comer {alimento} agora.")
        elif self.comendo == False and self.falando == False and self.dormindo == True:
            print(f"{self.nome} está dormindo, não pode comer {alimento} agora.")

    def pararDeComer(self):

        if self.comendo == True and self.falando == False and self.dormindo == False:
            print(f"{self.nome} parou de comer")
            self.comendo = False
        elif self.comendo == False and self.falando == False and self.dormindo == False:
            print(f"{self.nome} está fazendo nada")
        elif self.comendo == False and self.falando == True and self.dormindo == False:
            print(f"{self.nome} não está comendo, está falando")
        elif self.comendo == False and self.falando == False and self.dormindo == True:
            print(f"{self.nome} não está comendo, está dormindo")

    def falar(self):

        if self.comendo == False and self.falando == False and self.dormindo == False:
            print(f"{self.nome} começou a falando")
            self.falando = True
        elif self.comendo == True and self.falando == False and self.dormindo == False:
            print(f"{self.nome} está comendo, não pode falar")
        elif self.comendo == False and self.falando == True and self.dormindo == False:
            print(f"{self.nome} já está falando")
        elif self.comendo == False and self.falando == False and self.dormindo == True:
            print(f"{self.nome} não pode falar, está dormindo")

    def pararDeFalar(self):
        if self.comendo == False and self.falando == True and self.dormindo == False:
            print(f"{self.nome} parou de falar")
            self.falando = False
        elif self.comendo == True and self.falando == False and self.dormindo == False:
            print(f"{self.nome} já está comendo")
        elif self.comendo == False and self.falando == False and self.dormindo == False:
            print(f"{self.nome} está fazendo nada")
        elif self.comendo == False and self.falando == False and self.dormindo == True:
            print(f"{self.nome} está dormindo")

    def dormir(self):
        if self.comendo == False and self.falando == False and self.dormindo == False:
            print(f"{self.nome} foi dormir")
            self.dormindo = True
        elif self.comendo == True and self.falando == False and self.dormindo == False:
            print(f"{self.nome} já está comendo, não pode ir dormir")
        elif self.comendo == False and self.falando == True and self.dormindo == False:
            print(f"{self.nome} já está falando, depois que parar de falar. Pode ir dormir")
        elif self.comendo == False and self.falando == False and self.dormindo == True:
            print(f"{self.nome} já está dormindo")

    def acorda(self):
        if self.comendo == False and self.falando == False and self.dormindo == True:
            print(f"{self.nome} Acordou")
            self.dormindo = False
        elif self.comendo == True and self.falando == False and self.dormindo == False:
            print(f"{self.nome} já está acordado e comendo")
        elif self.comendo == False and self.falando == True and self.dormindo == False:
            print(f"{self.nome} já está acordado e falando")
        elif self.comendo == False and self.falando == False and self.dormindo == False:
            print(f"{self.nome} está fazendo nada")