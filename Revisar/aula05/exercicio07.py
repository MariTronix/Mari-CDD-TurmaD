alunos= int(input("Quantos alunos tem na sala? "))
x = 0
soma = 0
while x < alunos:
    x += 1
    notas = float(input(f"Notas do aluno {x}º: "))
    soma += notas

media = soma / alunos
print(media)