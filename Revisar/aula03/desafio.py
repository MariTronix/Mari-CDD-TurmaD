hora1 = int(input("Primeira Hora: "))
minuto1 = int(input("Primeira minuto: "))
hora2 = int(input("Segunda Hora: "))
minuto2 = int(input("Segunda minuto: "))

if hora1 > 12:
    hora1 -= 12
if hora2 > 12:
    hora2 -= 12

hora = hora1 + hora2
minuto = minuto1 + minuto2

if minuto >= 60:
    minuto -= 60
    hora += 1

if hora > 12:
    hora -= 12

if minuto < 10 : print(f"{int(hora)}:0{minuto}")
else:print(f"{int(hora)}:{minuto}")