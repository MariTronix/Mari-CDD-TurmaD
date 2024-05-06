a = ["","","","","","","","","",""]
m = ["","","","","","","","","",""]

for x in range(10):
    a[x] = int(input("Digite o número: "))

x = int(input("Digite um numero do multiplicador: "))

for y in range(10):
    m[y] = a[y] * x

for z in range(10):
    print(f"Multiplicação de {a[z]} X {x} = {m[z]}")