# Escreva um algoritmo que leia o número de litros vendidos e o
# tipo de combustível (codificado da seguinte forma: E-etanol,
# G-gasolina), calcule e imprima o valor a ser pago pelo cliente
# sabendo-se que o preço do litro da gasolina e R$ 5,80 e o preço
# do etanol é R$ 4,90

#Variáveis de litros e o tipo de combustível comprado
litro = float(input("Quantos litros de combustível: "))
tipo = input("Tipo de combustível (E - Etanol ou G - Gasolina): ")

#Variáveis que informa o valor dos combustíveis
etanol = 4.90
gasolina = 5.80

#decisão para saber qual calculo fazer
if tipo == 'E' or tipo == 'e':
    valor = litro * etanol
    print(f"Valor: R${valor}")
elif tipo == 'G' or tipo == 'g':
    valor = litro * gasolina
    print(f"Valor: R${valor}")
else:
    print("Esse tipo de combustível não existe")