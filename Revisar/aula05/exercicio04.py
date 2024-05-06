dentroIntervalo = 0
foraIntervalo = 0
for x in range(1, 11):
    num = int(input(f"Digite {x}º número: "))
    if num >= 10 and num <= 20:
        dentroIntervalo += 1
    elif num < 10 or num > 20:
        foraIntervalo += 1
print(f"Estão dentro do intervalor: {dentroIntervalo}º")
print(f"Estão fora do Intervalor: {foraIntervalo}")

#OU

dentroIntervalo = 0
foraIntervalo = 0
for x in range(1, 11):
    num = int(input(f"Digite {x}º número: "))
    if num >= 10 and num <= 20:
        dentroIntervalo += 1
    else:
        foraIntervalo += 1
print(f"Estão dentro do intervalor: {dentroIntervalo}º")
print(f"Estão fora do Intervalor: {foraIntervalo}")

#OU

dentroIntervalo = 0
foraIntervalo = 0
for x in range(1, 11):
    num = int(input(f"Digite {x}º número: "))
    if  10 >= num <= 20:
        intervalo += 1
    else:
        foraIntervalo += 1
print(f"Estão dentro do intervalor: {dentroIntervalo}º")
print(f"Estão fora do Intervalor: {foraIntervalo}")

#OU

dentroIntervalo = 0

for x in range(1, 11):
    num = int(input(f"Digite {x}º número: "))
    if  10 >= num <= 20:
        intervalo += 1
foraIntervalo = 10 - dentroIntervalo
print(f"Estão dentro do intervalor: {dentroIntervalo}º")
print(f"Estão fora do Intervalor: {foraIntervalo}º")