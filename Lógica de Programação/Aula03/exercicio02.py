#Faça um código que receba as 3 notas de um aluno e
# verifique se ele está aprovado ou reprovado.
# Considere que a média para aprovação é 7,0.

#Variáveis para notas.
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a segunda nota:"))

#variável para calcular a média
media = (nota1 + nota2 + nota3) / 3

#Decição para saber se o aluno foi aprovado ou reprovado e saida do resultado
if media >= 7:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")