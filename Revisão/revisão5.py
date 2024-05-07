"""num = int(input("Digite um número: "))

calc = num % 2

if calc == 0:
    print(f"{num} é Par")
else:
    print(f"{num} é Impar")"""

resp = 's'

while resp == 's' or resp == 'S':
    num = int(input("Digite um número: "))
    calc = num % 2
    if calc == 0:
        print(f"{num} é Par")
    else:
        print(f"{num} é Impar")
    resp = input("Gostaria de digita outro número(S/N): ")