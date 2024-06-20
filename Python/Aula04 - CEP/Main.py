import requests, mysql.connector

print("Verificando endereço...")
nome = input("Nome: ")
cep = input("Digite o CEP: ")
link = f"https://viacep.com.br/ws/{cep}/json/"
requisicao = requests.get(link)
endereco = requisicao.json()
cep1 = endereco['cep']
logradouro = endereco['logradouro']
bairro = endereco['bairro']
localidade = endereco['localidade']
uf = endereco['uf']


banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="aulafinal"
)

curso = banco.cursor()
sql = "insert into endereco(nome,cep,logradouro,bairro,localidade,uf) values(%s,%s,%s,%s,%s,%s)"
data = (nome, cep1, logradouro, bairro, localidade, uf)
curso.execute(sql, data)
banco.commit()

curso = banco.cursor()
pesquisar = 'select * from endereco '
curso.execute(pesquisar)
resultado = curso.fetchall()
for x in resultado:
      print(x)+