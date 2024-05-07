# Imagine que queremos imprimir todas as letras de um nome.
# Então, faça um programa que receba um nome de uma pessoa e
# mostre letra por letra

#Variável para pedir um nome
nome = input("Digite um nome: ")

#for vai passar por cada letra do nome. end faz imprimir do lado
for x in nome:
    print(x, end=" ")