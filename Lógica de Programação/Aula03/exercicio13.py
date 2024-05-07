#Receber um número do usuário e mostrar todos os
# números ímpares do intervalo de 1 até o número digitado

num = int(input("Digete um numero: "))
calc = num % 2 == 0

for x in range(1,num+1,2):
        print(x, end=" ")

#ou
num = int(input("Digite um número: "))

for x in range(1,num+1):
    if x % 2 == 1:
        print(x)