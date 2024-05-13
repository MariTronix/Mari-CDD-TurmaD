"""nomes = ["","","","",""]

for x in range(5):
    nomes[x] = input(f"Digite um nome: ")

for y in range(5):
    print(f"{nomes[y]}", end=" ")
"""
    #OU

alunos = int(input("Quantos alunos tem na turma:"))

nomes = []

for x in range(alunos):
    nomes.insert(x,input("Digite um nome: "))

for y in range(alunos):
    print(f"{nomes[y]}, sua array é: {y}", end=",")
