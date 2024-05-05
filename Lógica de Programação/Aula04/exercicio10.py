num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
x = 0

while x < 100000:
    if num2 == 0:
        print("Numero diferente de zero")
        num2 = int(input("Digite um numero: "))
    else:
        break

divisao = num1 / num2
print(f" resultado de {num1} / {num2} é: {divisao}")