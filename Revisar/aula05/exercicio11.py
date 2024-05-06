resposta = 's'
while resposta == 's':
    n1 = float(input("Primeira nota: "))
    while n1 < 0 or n1 > 10:
        n1 = float(input("Primeira nota: "))

    n2 = float(input("Segunda nota: "))
    while n2 < 0 or n2 > 10:
        n2 = float(input("Segunda nota: "))
    media = (n1 + n2) / 2
    print(media)
    resposta = input("Deseja continuar o cálculo(S/N): ")