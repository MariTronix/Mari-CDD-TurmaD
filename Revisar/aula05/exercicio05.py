soma = 0
for x in range(1, 11):
    num = int(input(f"Digite {x}º número: "))
    soma = soma + num
media = soma / x
print(media)

#OU

soma = 0
for x in range(1, 11):
    num = int(input(f"Digite {x}º número: "))
    soma = soma + num
media = soma / 10
print(media)