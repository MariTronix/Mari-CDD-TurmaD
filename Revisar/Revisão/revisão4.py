"""n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))

if n1 > n2:
    if n1 > n3:
        print(f"{n1} é o maior")
    else:
        print(f"{n3} é o maior")
elif n2 > n3:
    print(f"{n2} é o maior")
else:
    print(f"{n3} é o maior")"""

calc = 0
for x in range(1,4):
    n = int(input(f"Digite {x}º número: "))
    if n > calc:
        calc = n
print(f"Maior número é: {calc}")