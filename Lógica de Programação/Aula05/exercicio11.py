numeros = []
cont = 0

for x in range(10
               ):
    num = int(input("Digite numero: "))
    numeros.insert(x,num)

aleatorio = int(input("Mais 1 numero: "))

for x in numeros:
    if x == aleatorio:
        cont+=1
    print(x, end=" ")

print(f"numero {aleatorio} repete, {cont} vezes")
