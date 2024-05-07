#Escreva um algoritmo para ler 10 números e ao final
# da leitura escrevaer a soma total dos 10 números lidos

soma = 0
for x in range(1,11):
    num = int(input(f"Digite {x}º numero: "))
    soma += num
print(soma)