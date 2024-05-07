nomes = ["","","","",""]
senha = ["","","","",""]

for x in range(5):
    nomes[x]= input("Digite nome do usuário: ")
    senha[x]= input("Digite a senha: ")

nome = input("Digite nome do usuário: ")

for x in range(5):
    if nome == nomes[x]:
        senha = input("Digite a senha:")
        for y in range(5):
            if x == y:
                while senha != senhas[y]:
                    senha = input("Digite a senha novamente: ")
                if senha == senhas[y]:
                    print("Login realizado")
else:
    print("Usuário não existe")