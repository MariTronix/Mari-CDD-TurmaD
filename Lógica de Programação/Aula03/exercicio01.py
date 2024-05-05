# Receba 2 números do usuário e mostre eles em ordem crescente.

#Variáveis dos números
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))

# Decisão para colocar em ordem crescente.
if num1 > num2:
    print(num2,num1)
else:
    print(num1,num2)