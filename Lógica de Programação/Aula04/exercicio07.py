soma = 0

for x in range(1,11):
    num = int(input(f"Digite {x}º numero: "))
    if num == 0:
        print("Digite um número maior q zero")
        for x in range(1, 11):
            num = int(input(f"Digite {x}º numero: "))
        soma += num
    else:
        soma += num

media = soma / x

print(media)