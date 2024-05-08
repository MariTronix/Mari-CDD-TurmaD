nomes = ["","","","",""]
senhas = ["","","","",""]
opcao = 0
cont = 0

while opcao != 3:
    opcao = int(input("Escolha sua opção: \n"
                      "1 - Cadastro\n"
                      "2 - Login \n"
                      "3 - Sair"))

    if opcao == 1:
        for x in range(5):
            nomes[x] = input("Digite nome do usuário: ")
            senhas[x] = input("Digite a senha: ")

    elif opcao == 2:
        login = input("Digite o nome do seu usuário: ")
        senha = input("Digite sua senha: ")
        for z in range(5):
            if login == nomes[z]:
                        while senha != senhas[z]:
                            print("Senha errada")
                            senha = input("Digite sua senha novamente: ")
                        if senha == senhas[z]:
                            print("Login efetuado com sucesso")
            else:
                cont += 1
                if cont == 5:
                    print("Usuário não existe")