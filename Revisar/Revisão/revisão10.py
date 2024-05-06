ano = int(input("Digite o ano do seu aniversario: "))
mes = int(input("Digite o mês do seu aniversario: "))
dia = int(input("Digite o dia do seu aniversario: "))

anoAtual = 2024
mesAtual = 4
diaAtual = 24

if mes < mesAtual:
    idade = anoAtual - ano
elif mes == mesAtual:
    if dia <= diaAtual:
        idade = anoAtual - ano
    else:
        idade = anoAtual - ano - 1
else:
    idade = anoAtual - ano - 1

dif = mesAtual - mes

if dif == 0:
    if dia <= diaAtual:
        meses = 0
    else:
        meses = 11
elif dif < 0:
    meses = 12 + dif
elif dif > 0:
    meses = dif

dias = dia - diaAtual

if dias < 0:
    meses -= 1
    dias +=30

print(f"{idade} anos, {meses} meses e {dias} dias")