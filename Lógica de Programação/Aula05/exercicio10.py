N = int(input("Qual é o tamanho do vetor:"))
A = []
B = []

soma = []

for y in range(N):
    a =  int(input("Digite um numero: "))
    A.insert(y,a)


for z in range(N):
    b = int(input("Digite um numero: "))
    B.insert(z,b)

for x in range(N):
    sum = A[x] + B[x]
    soma.insert(x,sum)

print(soma)