x = 0

while x < 10000000:
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

    x +=1

    decisao = input(" Deseja realizar um novo cálculo: Sim ou não ")

    if decisao == "não" or decisao == "nao":
        break