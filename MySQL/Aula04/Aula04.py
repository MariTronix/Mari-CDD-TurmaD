import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="aulafinal"
)


"""meucurso.close()
banco.close()"""

"""nome1= "Jão"
telefone1 = "69696969696"
curso = banco.cursor()
sql = "insert into alunos(nome,telefone) values (%s,%s)"
data = (nome1,telefone1)
curso.execute(sql,data)
banco.commit()"""

"""meucurso = banco.cursor()
pesquisar = 'select * from alunos;'
meucurso.execute(pesquisar)
resultado = meucurso.fetchall()
for x in resultado:
    print(x)"""


cont = 1

while cont != 3:
    cont = int(input("\nMenu: \n"
                     "1 - Mostrar tabela alunos \n"
                     "2 - Inserir um aluno \n"
                     "3 - Sair do sistema: \n"
                     ""
                     ))

    if cont == 1:
        curso = banco.cursor()
        pesquisar = 'select * from alunos;'
        curso.execute(pesquisar)
        resultado = curso.fetchall()
        for x in resultado:
            print(x)

    elif cont == 2:
        nome = input("Nome do aluno: ")
        telefone = input("Telefone do aluno: ")
        curso = banco.cursor()
        sql = "insert into alunos(nome,telefone) values (%s,%s)"
        data = (nome, telefone)
        curso.execute(sql, data)
        banco.commit()

    elif cont == 3:
        curso.close()
        banco.close()
        print("Sistema Finalizado")

    else:
        print("Opção invalida, tente novamente")