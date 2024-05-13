nomes = [0,0,0,0,0]
senha = [0,0,0,0,0]

for x in range(5):
    nomes[x]= int(input("Digite nome do usuário: "))
    senha[x]= int(input("Digite a senha: "))

for y in range(5):
    print(f"{nomes[y]} e {senha[y]}, estão no array[{y}]")