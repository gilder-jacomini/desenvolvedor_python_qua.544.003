import os
os.system("cls" if os.name == "nt" else "clear")

# dicionario
usuario = {
    'nome': "Fulano", 
    'idade': 35,
    'email': "fulano@gmail.com",
    'cpf': "123.456.789.10"
}

# 1ª forma de mostrar os dados - risco de crachar caso peça dado que não existe mas aceita alterações
print(f"Nome: {usuario['nome']}")
print(f"Idade: {usuario['idade']}")
print(f"Email: {usuario['email']}")
print(f"CPF: {usuario['cpf']}")
print("\n")

# 2ª forma de mostrar os dados - não cracha mas não altera os itens
print(f"Nome: {usuario.get('nome')}")
print(f"Idade: {usuario.get('idade')}")
print(f"Email: {usuario.get('email')}")
print(f"CPF: {usuario.get('cpf')}")
print("\n")

# 3ª forma de mostrar os dados - laço de repetição
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")

