# Importacao de bibliotecas
import os

# laço de repetição
try:
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        
        # Entrada de dados
        nome = input("Informe o nome: ").strip() .title()
        idade = int(input("Informe a idade: "))
        cpf = input("Informe o CPF: ").strip()
        email = input("Informe o E-mail: ").strip().lower()

        os.system("cls" if os.name == "nt" else "clear")

        # Saída de dados
        print(f"Nome: {nome}.")
        print(f"Idade: {idade}.")
        print(f"CPF: {cpf}.")
        print(f"E-mail: {email}.")

        # menu
        print("\n1 - Informar dados do novo usuário")
        print("2 - Sair do programa")
        opcao = input("Informe a opção desejada: ").strip()

        match opcao:
            case "1":
                continue
            case "2":
                break
            case _:
                print("Opção inválida")
        

except:
    print("error")