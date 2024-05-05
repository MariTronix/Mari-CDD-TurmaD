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