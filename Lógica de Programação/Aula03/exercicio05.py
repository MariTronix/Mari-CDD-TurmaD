litro = float(input("Quantos litros de combustível: "))
tipo = input("Tipo de combustível (E - Etanol ou G - Gasolina): ")

etanol = 4.90
gasolina = 5.80

if tipo == 'E' or tipo == 'e':
    valor = litro * etanol
    print(valor)
elif tipo == 'G' or tipo == 'g':
    valor = litro * gasolina
    print(valor)
else:
    print("Esse tipo de combustível não existe")