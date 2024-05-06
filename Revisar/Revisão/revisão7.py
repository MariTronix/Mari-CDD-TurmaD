soma = 0

for x in range(1,5):
    n = float(input(f"Digite {x} nota: "))
    soma += n

media = soma / 4
print(f"A media é : {media}")