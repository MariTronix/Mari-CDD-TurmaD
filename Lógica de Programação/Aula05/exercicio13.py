numeros = []
pares = []
menor = 10000000000000000000000000
maior = -10000000000000000000000000
cont = 0
soma = 0

for x in range(6):
    num = int(input("Digite 1 número: "))
    numeros.insert(x,num)

for y in range(len(numeros)):
    if numeros[y] % 2== 0:
        pares.insert(y,numeros[y])

for z in range(len(numeros)):
    if numeros[z] < menor:
        menor = numeros[z]
    if numeros[z] > maior:
        maior = numeros[z]

for i in range(len(numeros)):
    soma += numeros[i]

media = soma / 6

for q in range(len(numeros)):
    if numeros[q] > media:
        cont += 1

print(pares)
print(menor,maior)
print(media, cont)