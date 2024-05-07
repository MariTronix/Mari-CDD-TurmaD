decisao = 1
while decisao != 3:
    decisao = int(input("Qual gostaria de calcula \n"
                        "(1)-Triangulo \n"
                        "(2)-Quadrado \n"
                        "(3)-Sair do sistema: "))
    if decisao < 1 or decisao > 3:
        print("Opção invalida")
    if decisao == 1:
        base = float(input("Valor da base do triangulo: "))
        altura = float(input("Valor da altura do triangulo: "))
        area = (base * altura) / 2
        print(area)
    elif decisao == 2:
        lado= float(input("Valor da lado do quadrado: "))
        area = lado ** 2
        print(area)