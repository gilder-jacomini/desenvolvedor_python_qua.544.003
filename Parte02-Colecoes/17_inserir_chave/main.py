import os
os.system("cls" if os.name == "nt" else "clear")

# dicionario
usuario = {
    'nome': "Fulano", 
    'idade': 35,
    'email': "fulano@gmail.com",
    'cpf': "123.456.789.10"
}

# adiciona a chave telefone ao dicionario
usuario['telefone'] = input(f"Informe o telefone de {usuario.get('nome')}: ").strip()

os.system("cls" if os.name == "nt" else "clear")

# exibe o dicionário
for chave in usuario:
    print (f"{chave.capitalize()}: {usuario.get(chave)}")









