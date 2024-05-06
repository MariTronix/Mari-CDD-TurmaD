n1 = float(input("Primeira nota: "))


while n1 < 0 or n1 > 10:
    n1 = float(input("Primeira nota: "))

n2 = int(input("Segunda nota: "))

while n2 < 0 or n2 > 10:
    n2 = int(input("Segunda nota: "))

media = (n1 + n2) / 2
print(media)