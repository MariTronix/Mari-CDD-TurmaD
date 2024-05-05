soma = 0
x = 0

while x < 10:
    x += 1
    num = int(input(f"Digite {x}º numero: "))
    soma += num

media = soma / 10

print(media)