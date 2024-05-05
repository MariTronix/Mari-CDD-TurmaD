ano = int(input("Digite o ano do seu aniversario: "))
mes = int(input("Digite o mês do seu aniversario: "))
dia = int(input("Digite o dia do seu aniversario: "))

anoAtual = 2024
mesAtual = 4
diaAtual = 28

if mes < mesAtual:
    idade = anoAtual - ano
elif mes == mesAtual and dia > diaAtual:
    idade = anoAtual - ano - 1
elif mes == mesAtual and dia <= diaAtual:
    idade = anoAtual - ano
elif mes > mesAtual:
    idade = anoAtual - ano - 1

dif = mesAtual - mes

if dif == 0 and dia <= diaAtual:
    meses = 0
elif dif == 0 and dia > diaAtual:
    meses = 11
elif dif < 0:
    meses = 12 + dif
elif dif > 0:
    meses = dif

dias = dia - diaAtual
print(dias)

diasPositivo = dias * -1

print(f"{idade} anos, {meses} meses, {diasPositivo} dias")