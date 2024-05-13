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

def estoque(produto,quantidade, preco):

    produtos = [], valorunitario = [], valortotal = []

    for x in range(5):
        produtos.insert(x,produto)
    for y in range(5):
        valorunitario.insert(y,quantidade)

def somar(*x):
    soma = 0
    for y in x:
        soma += y
    print(soma)

def texto(argumento):
    letra = len(argumento)
    for x in argumento:
        if x in ".,!? ":
            letra = letra - 1
        print(x, end="")
    print(letra)
    for y in range(letra-1,-1,-1):
        print(argumento[y], end="")

    print(argumento[::-1])

def numero_unicos(*num):

    nova_lista =set(num)

    """for x in num:
        if x not in nova_lista:
            nova_lista.append(x)"""

    print(nova_lista)

def numero_primo(num):
    if num == 1:
        return (f"{num} não é primo")

    elif num == 2:
        return (f"{num} é primo")

    else:
        for x in range(2,num):
            if (num % x == 0):
                return num, "não é primo"
        return num, "É primo"