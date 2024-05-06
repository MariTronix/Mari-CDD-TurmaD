#Receba um número, do usuário e diga se ele e par ou ímpar

#Variável do número
num = int(input("Digite um numero: "))

#Calculo para saber se é par ou Ímpar
reslt = num % 2

#Decisão
if reslt == 0:
    print("Par")
else:
    print("Impar")