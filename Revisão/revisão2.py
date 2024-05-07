"""num = int(input("Digite um numero: "))

if num < 0:
    print(f"{num} é negativo")
else:
    print(f"{num} é positivo")"""


decisao = 's'

while decisao == "s" or decisao == "S":
    num = int(input("Digite um numero: "))
    while num == 0:
        num = int(input("Digite um numero: "))
    if num < 0:
        print(f"{num} é negativo")
    else:
        print(f"{num} é positivo")
    decisao = input("Deseja digitar numero de novo: (S/N): ")