#Faça um código para ler a senha de um usuário
# e apos 3 tentativas erradas, sair do programa,
# informando que a senha etá bloqueada

"""pin = 1234
x = 0

while x < 3:
    senha = input("Digite sua senha: ")
    if senha != pin:
        x += 1
        print("Tente novamente")
    else:
        break
print("Senha bloaqueada")"""

#OU

pin = 1234
x = 0
senha = int(input("Digite a senha: "))

while senha != pin:
    x += 1
    senha = int(input("Senha incorreta, tente novamente: "))

    if x == 2:
        print("Muitas tentativas!! Senha bloqueadas")
        break
else:
    print("Login efeituado")