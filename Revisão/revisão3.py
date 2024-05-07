idade = int(input("Digite sua idade: "))
mes = int(input("Qual mês vocês faz aniversario: (1/12): "))
anoAtual = 2024
mesAtual = 4
if mes <= mesAtual:
    ano = anoAtual - idade
    print("")
else:
    ano = anoAtual - idade - 1

print(f"Ano que nasceu é: {ano}")