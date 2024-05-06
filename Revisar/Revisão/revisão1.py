"""nota1 = float(input("Digite a primeira nota: "))

while nota1 < 0 or nota1 > 10:
    nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

while nota2 < 0 or nota2 > 10:
    nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print(f"A media do aluno é: {media}")"""

soma = 0
for x in range(1,3):
    nota = float(input(f"Digite a nota {x}º: "))
    while nota < 0 or nota > 10:
        nota = float(input(f"Digite a nota {x}º: "))
    soma += nota
media = soma / 2

if media >= 7:
    print(f"Aluno(a) Aprovado(a) \nMédia do aluno é: {media}")
elif media >= 4:
    print(f"Aluno(a) Recuperação \nMédia do aluno é: {media}")
else:
    print(f"Aluno(a) Reprovado(a) \nMédia do aluno é: {media}")