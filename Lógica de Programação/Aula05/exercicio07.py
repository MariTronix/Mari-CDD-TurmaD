nomes = ["","","","",""]
senha = ["","","","",""]

for x in range(5):
    nomes[x]= input("Digite nome do usuário: ")
    senha[x]= input("Digite a senha: ")

for y in range(5):
    print(f"{nomes[y]} e {senha[y]}, estão no array[{y}]")