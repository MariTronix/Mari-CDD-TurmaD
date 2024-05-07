#Ler uma variável de número inteiro e mostrar a tabuada
# de multiplicação desse número.

num = int(input("Digite um numero: "))
print(f"Tabuada do {num} é:")

for x in range(1,11):
    mult = num * x
    print(f"{num} * {x}: {mult} ")