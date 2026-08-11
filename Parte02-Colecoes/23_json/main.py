import os
import json
os.system("cls" if os.name == "nt" else "clear")

usuarios = []
abrir = ""

while True:
    print("1 - Gravar novo arquivo em json")
    print("2 - Grava em arquivo existente")
    print("3 - Ler arquivo em json")
    print("4 - Sair")
    opcao = input("Informe a opçaõ desejada: ")

    os.system("cls" if os.name == "nt" else "clear")

    if opcao == "1" or opcao == "2":
        usuario = {}
        usuario['nome'] = input("informe o nome: ").strip().title()
        usuario['email'] = input("Informe o e-mail: ").strip().lower()
        usuarios.append(usuario)

        match opcao:
            case "1":
                arquivo = input("Informe o nome do arquivo: ")
                # grava o arquivo na extenção .json
                with open(f"23_json/{arquivo}.json" , "w" , encoding="utf-8") as f:
                    json.dump(usuarios, f)

            case "2":
                if abrir:
                    with open(f"23_json/{abrir}.json" , "w" , encoding="utf-8") as f:
                        json.dump(usuarios, f)

    else:
        match opcao:
            case "3":
                abrir = input("Informe o nome do arquivo que deseja abrir: ")
                with open(f"23_json/{abrir}.json" , "r" , encoding="utf-8") as f:
                    usuarios = json.load(f)
                for usuario in usuarios:
                    for chave, valor in usuario.items():
                        print(f"{chave.capitalize()}: {valor}")

            case "4":
                break
            case _:
                print("Opção inválida")
                continue




         
