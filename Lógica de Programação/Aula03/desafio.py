# Pedir ao usuário as horas e os minutos

hora1 = int(input("Primeira Hora: "))
minuto1 = int(input("Primeira minuto: "))
hora2 = int(input("Segunda Hora: "))
minuto2 = int(input("Segunda minuto: "))

#Transforma as horas de entrada em 12 horas.

if hora1 > 12:
    hora -= 12

if hora2 > 12:
    hora -= 12

# Fazer a soma das horas e minutos.

horas = hora1 + hora2
minutos = minuto1 + minuto2

# Se os minutos forem maior que 60, adicionar 1 hora na variável horas e diminuir 60 minutos

if minutos >= 60:
    minutos -= 60
    horas += 1

# Ver se a hora continua em 12 horas, depois da soma de horas e adicinando os minutos

if horas > 12:
   horas -= 12
elif horas < 12:
    horas += 12

# Fazer a saída para minutos menores de 10, ter um retorno de um 0 em string, se não voltar os minutos normal.

if minutos < 10:
    print(f"{int(horas)}:0{minutos}")
else:
    print(f"{int(horas)}:{minutos}")