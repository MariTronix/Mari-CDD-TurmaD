# Duas variáveis (A e B) possuem valores distintos (A=5 e B=10),
# crie um algoritmo que armazene esses dois valores nessas duas variáveis
# e efetua a troca dos valores de forma que a variável A passe a possuir o
# valor da variável B e que a variável passe a possuir o valor da variável A.
#  Por fim apresentar os valores trocados.

# as duas variáveis
a = 5
b = 10

#Criei uma nova variável e coloquei o valor de A, para conseguir modificar a variavel A
c = a

#A agora tem a valor de B
a = b

#B agora consegue o antigo valor de A que edtava guardado na nova variável.
b = c

#saida do resuldado
print(a,b)