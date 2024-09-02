num = int(input("Digite um número: "))
fibo = [1,1]

for x in range(2,num+1):

    pS = x - 1
    sS = x - 2
    pV = fibo[pS] + fibo[sS]
    fibo.insert(x,pV)
    print(fibo[x])
    
    if(fibo[x] >= num):
        break

