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
            self.comendo = True
            return (f"{self.nome} começou a comer {alimento}")
        elif self.comendo == True:
            return (f"{self.nome} está comendo, não pode comer {alimento} agora.")
        elif self.falando == True:
            return (f"{self.nome} está falando, não pode comer {alimento} agora.")
        elif self.dormindo == True:
            return (f"{self.nome} está dormindo, não pode comer {alimento} agora.")

    def pararDeComer(self):

        if self.comendo == True and self.falando == False and self.dormindo == False:
            self.comendo = False
            return (f"{self.nome} parou de comer")
        elif self.comendo == False and self.falando == False and self.dormindo == False:
            return (f"{self.nome} está fazendo nada")
        elif self.falando == True:
            return (f"{self.nome} não está comendo, está falando")
        elif self.dormindo == True:
            return (f"{self.nome} não está comendo, está dormindo")

    def falar(self):

        if self.comendo == False and self.falando == False and self.dormindo == False:
            self.falando = True
            return (f"{self.nome} começou a falar")
        elif self.falando == True:
            return (f"{self.nome} está falando")
        elif self.comendo == True:
            return (f"{self.nome} está comendo, não pode falar")
        elif self.dormindo == True:
            return (f"{self.nome} não pode falar, está dormindo")

    def pararDeFalar(self):
        if self.comendo == False and self.falando == True and self.dormindo == False:
            self.falando = False
            return (f"{self.nome} parou de falar")
        elif self.comendo == True:
            return (f"{self.nome} está comendo")
        elif self.dormindo == True:
            return (f"{self.nome} está dormindo")
        elif self.comendo == False and self.falando == False and self.dormindo == False:
            return (f"{self.nome} está fazendo nada")

    def dormir(self):
        if self.comendo == False and self.falando == False and self.dormindo == False:
            self.dormindo = True
            return (f"{self.nome} foi dormir")
        elif self.comendo == True:
            return (f"{self.nome} está comendo, não pode ir dormir")
        elif self.falando == True:
            return (f"{self.nome} está falando, não pode ir dormir")
        elif self.dormindo == True:
            return (f"{self.nome} já está dormindo")

    def acordar(self):
        if self.comendo == False and self.falando == False and self.dormindo == True:
            self.dormindo = False
            return (f"{self.nome} Acordou")
        elif self.comendo == True:
            return (f"{self.nome} está acordado e comendo")
        elif self.falando == True:
            return (f"{self.nome} está acordado e falando")
        elif self.comendo == False and self.falando == False and self.dormindo == False:
            return (f"{self.nome} está fazendo nada")

    def menu(self):

        cont = 0

        while cont != 7:
            cont = int(input("1 - Comer\n"
                             "2 - Para de comer\n"
                             "3 - Falar\n"
                             "4 - Para de falar\n"
                             "5 - Dormir\n"
                             "6 - Acorda\n"
                             "7 - Sair\n "))

            while cont < 0 or cont > 7:
                cont = int(input("Escolha uma dessas opções:\n"
                                 "1 - Comer\n"
                                 "2 - Para de comer\n"
                                 "3 - Falar\n"
                                 "4 - Para de falar\n"
                                 "5 - Dormir\n"
                                 "6 - Acorda\n"
                                 "7 - Sair\n "))

            if cont == 1:
                alimento = input("O que deseja comer? ")
                print(self.comer(alimento))
            elif cont == 2:
                print(self.pararDeComer())
            elif cont == 3:
                print(self.falar())
            elif cont == 4:
                print(self.pararDeFalar())
            elif cont == 5:
                print(self.dormir())
            elif cont == 6:
                print(self.acordar())
            elif cont == 7:
                print("Saindo")

class Conta():
    def __init__(self, numero, nome, tipo):
        self.nome = nome
        self.numero = numero
        self.tipo = tipo
        self.status = False
        self.saldo = 0.0

    def ativar(self):
        decisao = int(input("Gostaria de ativar sua conta 1 - sim "
                            "\n2 - não"))
        if decisao == 1:
            if self.status == False:
                self.status = True
                print("Conta ativada")
            else:
                print("Conta já está ativada")

    def desativar(self):
        decisao = int(input("Gostaria de desativar sua conta 1 - sim "
                            "\n2 - não"))
        if decisao == 1:
            if self.status == True:
                self.status = False
                print("Conta desativada")
            else:
                print("Conta já está desativada")

    def deposito(self, valor):
        if valor < 0:
            print("Error")
        elif self.status == True:
            self.saldo += valor
            print(f"Deposito com sucesso")
        else:
            print("Conta não está ativa")

    def verificarSaldo(self):
        if self.status == True:
            print(self.saldo)
        else:
            print("Conta não está ativa")

    def saca(self, valor):
        if valor < 0:
            print("Error")
        if self.status == True:
            if self.saldo >= valor and self.saldo != 0:
                self.saldo -= valor
                print("Saque com sucesso")
            elif self.saldo < valor:
                print(f"Saque negado, Saldo: {self.saldo} ")
