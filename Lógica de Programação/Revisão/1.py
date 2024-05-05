sistema = 1

while sistema != 3:
    sistema = int(input("Deseja calcular 1-Triângulo \n "
                        "2- Quadrado \n "
                        "3- Sair "))
    while sistema <= 0 or sistema > 4:
        sistema = int(input("Opção errada \n "
                            "Deseja calcular 1-Triângulo \n "
                            "2- Quadrado \n "
                            "3- Sair "))
    if sistema == 1:
        base = float(input("Valor da base: "))
        altura = float(input("Valor da altura: "))
        area = (base * altura) / 2
        print(f"A área do triângulo é: {area}")
    elif sistema == 2:
        altura = float(input("Valor da altura: "))
        area = altura ** 2 #Ou altura * 4
        print(f"A área do quadrado é: {area}")