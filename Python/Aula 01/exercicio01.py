def cadastro():
    nomes = ["","","","",""]
    senha = ["","","","",""]

    for x in range(5):
        nomes[x]= input("Digite nome do usuário: ")
        senha[x]= input("Digite a senha: ")

    for y in range(5):
        print(f"{nomes[y]} e {senha[y]}, estão no array[{y}]")

def imprime_nome(nome):
    print(f"Nome: {nome}")


def numeros(numero):
    for x in range(numero+1):
        for y in range(x):
            print(x, end=" ")
        print()

def piramide(num):
    for x in range(1,num+1):
        for y in range(1,x+1):
            print(y, end=" ")
        print()

def contagem(texto):
    vogal = 0
    espaco = 0
    for x in texto:
        if x in "aeiouAEIOU":
            vogal += 1
        if x == " ":
            espaco += 1
    print(vogal)
    print(espaco)
    print(len(texto))

def valorTotal(nome, quantidade, preco):
    total = quantidade * preco
    print(f"Valor total do {nome} é {total}")
