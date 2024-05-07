#Ler valores e escrever quantos desses valores são negativos

negativo = 0
for x in range(1, 11):
    num = int(input(f"Digite {x}º numero: "))
    if num < 0:
        negativo +=1
print(negativo)
