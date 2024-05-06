x = 0
soma = 0
while x < 10:
    x += 1
    num = int(input(f"Digite {x} número: "))
    soma = soma + num
media = soma / x
print(media)

#OU

x = 0
soma = 0
while x < 10:
    num = int(input(f"Digite um número: "))
    soma = soma + num
    x += 1
media = soma / 10
print(media)