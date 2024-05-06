notas = [0,0,0,0,0]
soma = 0
cont = 0

for x in range(5):
    notas[x] = float(input("Digite uma nota: "))

for y in range(5):
    soma = soma + float(notas[y])

media = soma/5

for z in range(5):
    if notas[z] >= media:
        cont += 1

print(f"A média da turma é {media}, e {cont} alunos estão aprovados")


