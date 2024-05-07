#Faça um código que receba o número de alunos de uma sala
# de aula e depois solicite as notas desses alunos, no final,
# mostre a média aritmétrica da turma

alunos = int(input("Quantos alunos na classe: "))
x = 0
soma = 0

while x < alunos:
    x += 1
    nota = float(input(f"Nota do {x}º alunos: "))
    soma += nota

media = soma / alunos
print(media)