eleitores = int(input("Quantos eleitores em um municípios: "))

votosBrancos = int(input("Quantos votos em brancos: "))
votosNulos = int(input("Quantos votos nulos: "))
votosValidos = int(input("Quantos votos validos: "))

totalDeEleitores = votosBrancos + votosNulos + votosValidos

while totalDeEleitores != eleitores:
    votosValidos = int(input("Quantos votos validos: "))
    totalDeEleitores = votosBrancos + votosNulos + votosValidos

porcBrancos = 100 * (votosBrancos / eleitores)
porcNulos = 100 * (votosNulos / eleitores)
porcValidos = 100 * (votosValidos / eleitores)


print(f"Porcentagem de Brancos: {porcBrancos}%")
print(f"Porcentagem de Nulos: {porcNulos}%")
print(f"Porcentagem de Válidos: {porcValidos}%")