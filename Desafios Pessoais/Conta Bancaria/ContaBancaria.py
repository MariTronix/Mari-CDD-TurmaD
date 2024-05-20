class ContaBancaria():
    def __init__(self, numero, saldo, nome, tipo, depositar = True, sacar = True, verificarSaldo = True, status = True, ativarConta = False):
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        self.tipo = tipo
        self.status = status
        self.depositar = depositar
        self.sacar = sacar
        self.verificarSaldo = verificarSaldo
        self.ativarConta = ativarConta

    def deposito(self, valor):
        if self.status == True:
            self.saldo += valor

    def sacar(self, valor):
        if self.status == True:
            if self.saldo > valor:
                self.saldo -= valor
            elif self < valor:
                print(f"Saque negado, Saldo: {self.saldo} ")

    def verificarSaldo(self):
        if self.saldo == True:
            print(self.saldo)

    def ativacao(self,decisao):
        if self.status == True:
            decisao = int(input("Gostaria de desativar sua conta 1 - sim 2 - não"))
            if decisao == 1:
                if self.saldo == 0:
                    self.status == False
                elif self.saldo > 0:
                    print("Não pode desativa com dinheiro na conta")
                elif self.saldo < 0:
                    print("Não pode desativa com conta negativa")