#Receber 10 números do usuário e mostre a soma de todos os
# números ímapres

soma = 0

for x in range (1,11):
    num = int(input(f"Digite {x}º número: "))
    if num % 2 != 0:
        soma += num
print(soma)