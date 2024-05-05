noIntervalo = 0
foraDoIntervalo = 0

for x in range(1,11):
    num = int(input(f"Digite {x}º numero: "))

    if num >= 10 and num <= 20:
        noIntervalo += 1
    else:
        foraDoIntervalo += 1

print(noIntervalo)
print(foraDoIntervalo)