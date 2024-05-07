horaInicio = int(input("Hora de inicio: "))
horaFinal = int(input("Hora de final: "))

if horaInicio > horaFinal:
    total = 24 - horaInicio + horaFinal
    print(f"{total}horas")
elif horaInicio <= horaFinal:
    total = horaFinal-horaInicio
    print(f"{total}horas")