compras = int(input("Quantas maças: "))

if compras < 12:
    valor = compras * 1.30
elif compras >= 12:
    valor = compras * 1.00

print(valor)