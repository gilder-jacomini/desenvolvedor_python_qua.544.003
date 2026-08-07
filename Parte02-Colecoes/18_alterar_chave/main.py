import os
os.system("cls" if os.name == "nt" else "clear")

# dicionario
usuario = {
    'nome': "Fulano", 
    'idade': 35,
    'email': "fulano@gmail.com",
    'cpf': "123.456.789.10"
}

# usuario informa qual chave deseja alterar
chave = input("Informa o nome da chave: ").strip().lower()

# verificar se a chave existe
if chave in usuario:
    #se sim o usuário informa novo valor para a chave
    usuario[chave] = input(f"Informe o novo valor para a {chave}: ").strip()
    
    # exibe o dicionário com a chave alterada
    for chave in usuario:
        print(f"{chave.capitalize()}: {usuario.get(chave)}")
        
    # outra forma de exibir
    for chave, valor in usuario.items():
        print (f"{chave.capitalize()}: {valor}")
    
else:
    print("Chave não encontrada.")
    














