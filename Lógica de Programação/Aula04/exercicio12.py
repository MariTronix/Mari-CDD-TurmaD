#Escreva um código para ler as notas de 1a. e 2a. avaliações
# de um aluno, calcule e imprima a média desse aluno. Só devem
# ser aceitos valores válidos, durante a leitura, (0 a 10)
# para cada nota.

nota1 = int(input("Nota da primeira avaliação: "))
nota2 = int(input("Nota da segunda avaliação: "))

if nota1 < 0 or nota1 > 10:
    print("Notas de 0 a 10")
    nota1 = int(input("Nota da primeira avaliação: "))

if nota2 < 0 or nota2 > 10:
    print("Notas de 0 a 10")
    nota2 = int(input("Nota da segunda avaliação: "))

soma = nota1 + nota2
media = soma / 2
print(media)