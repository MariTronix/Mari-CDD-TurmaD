num = int(input("Digite um número: "))
print(f"A tabuada de {num} é:")

for x in range(1,11):
    multi = num * x
    print(f"{num}X{x}= {multi}")