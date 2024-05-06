senhaSecreta = 123456
senha = int(input("Digite a senha: "))
x = 1

while senha != senhaSecreta:
    senha = int(input("Senha errada, Tente novamente: "))
    x+=1
    if x == 3 and senha != senhaSecreta:
        print("Senha Bloqueada")
        break

if senha == senhaSecreta:
    print("Login Realizado com sucesso")