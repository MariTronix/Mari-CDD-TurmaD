from cadastroLogin import cadastro,login


#Cadastro

cadastro()

#Login
user = input("Digite o nome do seu usuário: ").capitalize()
senha = input("Digite sua senha: ")

print(login(user, senha))