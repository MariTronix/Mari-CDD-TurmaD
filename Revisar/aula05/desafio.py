"""num = int(input("Digite um numero: "))

for x in range(1,num+1):
    for z in range(x):
        print(x, end=" ")"""

#OU

num = int(input("Digite um numero: "))

for x in range(1,num+1):
    print(x * str(x), end=" ")