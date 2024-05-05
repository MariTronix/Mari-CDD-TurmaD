#Altere o código anterior e acrecente a
# opção de aluno em recuperação, caso sua média
# seja menor q 7,0 e maior que 4,0.


#Variáveis para notas.
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a segunda nota:"))

#variável para calcular a média
media = (nota1 + nota2 + nota3) / 3

#Decição para saber se o aluno foi aprovado ou reprovado e saida do resultado
if media >= 7:
    print("Aluno aprovado")
elif media >= 4:
    print("Aluno em recuperação")
else:
    print("Aluno reprovado")