num = int(input("Digite um número: "))
x = 1
while x <= num:
    count = 1
    while count <= x:
        print(x, end=" ")
        count += 1
    print()
    x += 1