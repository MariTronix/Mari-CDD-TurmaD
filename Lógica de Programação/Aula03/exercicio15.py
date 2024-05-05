alunos = int(input("Quantos alunos na sala:"))
soma = 0

for x in range(1,alunos+1):
    nota = float(input(f"Nota do {x}º aluno(a): "))
    soma += nota

media = soma / alunos
print(media)