import requests

print("Verificando endereço...")
cep = input("Digite o CEP: ")

if len(cep) != 8:
      print("cep invalido")
      exit()

consulta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
print(consulta.json())