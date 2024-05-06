nomes = ["","","","",""]

for x in range(5):
    nomes[x] = input(f"Digite um nome:")

for y in range(5):
    print(f"{nomes[y]} = array[{y}]", end=" ")

# OU
nomes = ["","","","",""]

for x in range(5):
    nomes[x] = input(f"Digite um nome:")

for y in range(5):
    print(nomes[y], y)