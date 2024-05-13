nomes = ["a","b","c","d","e"]
senhas = ["a","b","c","d","e"]


#Cadastro

def cadastro():

    for x in range(5):
        nome = input("Digite nome do usuário: ").capitalize()
        while nome in nomes:
            nome = input("Esse usuário ja exixste. Digite outro nome do usuário: ").capitalize()
        nomes.insert(x, nome)

        senha = input("Digite a senha: ")
        senhas.insert(x, senha)

#Login

def login(user, senha):
    
    cont = 0
    contSenha = 1 

    for z in range(5):
        if login == nomes[z]:
            while senha != senhas[z]:
                contSenha += 1
                senha = input("Senha invalida! Digite sua senha novamente: ")
                if contSenha == 3:
                    print("Bloqueado")
                    break
            if senha == senhas[z]:
                return(f"Login efetuado com sucesso, Seja Bem vindo(a): {login.capitalize()}")

        else:
            cont += 1
            if cont == 5:
                return("Usuário não existe")