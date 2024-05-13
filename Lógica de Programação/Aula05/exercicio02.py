alunos = int(input("Quantos alunos tem na turma:"))

nomes = []

for x in range(alunos):
    nomes.insert(x,input("Digite um nome: "))

nome = input("Nome do Aluno: ").lower()

if nome in nomes:
    print(f"O aluno {nome} está na lista!")
else:
    print(f"O aluno {nome} não está na lista.")