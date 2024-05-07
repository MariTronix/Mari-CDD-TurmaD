#Ler um valor N e imprimir todos os valores inteiros
# entre 1 e N. Considere que o N será sempre maior que zero.

#Modifique o exercício anterior para aceitar somente valores maiores
# que 0 para N. Caso o valor informado não seja maior que 0, deverá ser lido um
# novo valor para N

"""num = int(input("Digite um número: "))

if num <= 0:
    print("Escolha um número maior q zero")
    num = int(input("Digite um número: "))
    for x in range(1,num+1):
        print(x, end=" ")
else:
    for x in range(1,num+1):
        print(x, end=" ")"""

#OU

for x in range(10000000000000000000000000):
    num = int(input("Digite um número: "))
    for n in range(1, num + 1):
        if num > 0:
            print(n)