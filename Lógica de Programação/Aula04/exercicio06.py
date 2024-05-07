#Ler 10 valores, calcular e escrever a média aritmética
# desses valores lidos.

# Modifique o exercício anterior parar aceitar somente
# maiores que 0 para N. Caso o valor informado (para N)
# não seja maior que 0, deverá ser lido um novo valor para N.

soma = 0

for x in range(1,11):
    num = int(input(f"Digite {x}º numero: "))
    soma += num

media = soma / x

print(media)
