soma = 0

for x in range (1,11):
    num = int(input(f"Digite {x}º número: "))
    if num % 2 != 0:
        soma += num
print(soma)