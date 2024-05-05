#Faça um programa para calcular a média de 2 notas e mostrar essa média e o nome do aluno.

# variavel para nomes
nome = input("Digite o nome do aluno(a): ")

#variavel para notas, float significa numeros reais
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))


#variavel do calculo da media
media = (n1 + n2) / 2

#resultado de saide de nome e media
print(f"{nome} com a média {media}")