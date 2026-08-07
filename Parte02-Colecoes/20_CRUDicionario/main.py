import os
os.system("cls" if os.name == "nt" else "clear")

# criar uma lista
usuarios = []

# informe a opção desejada
while True:
    print("1 - Para Cadastrar novo usuário")
    print("2 - Para Listar usuários")
    print("3 - Para atualizar um usuário")
    print("4 - Para deletar um usuário")
    print("5 - Para Sair\n")
    opcao = input("Informe a opção desejada: ").strip()

    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1":
            #criar novo dicionario
            usuario = {}
            usuario['nome'] = input("Informe o nome do usuário: ").strip().title()
            usuario['cpf'] = input("Informe o cpf do usuário: ").strip()
            usuario['email'] = input("Informe o email do usuário: ").strip().lower()
            
            # adiciona o dicionário a lista
            usuarios.append(usuario)
            os.system("cls" if os.name == "nt" else "clear")
            continue
        case "2":
            # Lista os usuários cadastrados
            for usuario in usuarios:
                for chave, valor in usuario.items():
                    print(f"{chave.capitalize()}: {valor}")
                print(f"{'-'*40}")
            continue
        case "3":
            
            while True:
                valor = input("Informa o nome do usuário: ")
                if valor in usuario:
                    chave = input("Informa o campo a ser alterado: ").strip().lower()
                    if chave in usuario:
                        usuario[chave] = input(F"Informe o novo valor para {chave}: ").strip()
                    else:
                        print("Chave não encontrada")
                    
            # TODO fazer a parte de alterar o usuáro
            pass
        case "4":
            # TODO Excluir usuário
            pass
        case "5":
            break
        case _:
            print("Opção não encontrada")
            continue
    