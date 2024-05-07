nomes = ["mari","lud","joão","izair","lipe"]
senhas = ["123","456","789","012","345"]
decisao = int(input("1 - Realizar o login \n "
                    "2 - Sair: "))
while decisao == 1:

    login = input("Digite o nome do seu usuário: ")

    for x in range(5):
        if login == nomes[x]:
            senha = input("Digite sua senha: ")
            for y in range(5):
                if x == y:
                    while senha != senhas[y]:
                        print("Senha errada")
                        senha = input("Digite sua senha novamente: ")
                    while senha == senhas[y]:
                        print("Login efetuado com sucesso")
                        decisao = 0
                        break
            break
        elif x == 4:
            print("Usuário não existe")
            decisao = int(input("1 - Tenta efetuar o login nova \n"
                                "2 - Sair"))