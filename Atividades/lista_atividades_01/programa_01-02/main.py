# Importação de bibliotecas
import os
# Entrada de dados
os.system("cls" if os.name == "nt" else "clear")

nome = input("Informe seu nome: ").strip() .title()
idade = int(input("Informe sua idade: "))
os.system("cls" if os.name == "nt" else "clear")

while True:
    
    

    print("Filmes em cartaz:")
    print("Sala 1: A Volta Dos Que Não Foram. (livre)")
    print("Sala 2: A Roda Quadrada. (12 anos)")
    print("Sala 3: As tranças do Rei Careca. (14 anos)")
    print("Sala 4: Poeira em Alto Mar. (16 anos)")
    print("Sala 5: A Vingança do Frango Assassino. (18 anos)")
    print("Digite 6 para sair")

    opcao  = input("Informe o número da sala desejada: ")
    
    match opcao:
        case "2":
            print("Idade abaixo da permitida para esse filme")
            idade_min = 12
            continue
        case "3":
            print("Idade abaixo da permitida para esse filme")
            idade_min = 14
            continue
        case "4":
            print("Idade abaixo da permitida para esse filme")
            idade_min = 16
            continue    
        case "5":
            print("Idade abaixo da permitida para esse filme")
            idade_min = 18
            continue
        case "6" :
            break
        case _:
            bilhete = "bilhete"
            with open(f"programa_01-02/arquivos/{bilhete}.txt", "w", encoding="utf-8") as f:
                f.write(opcao)
                print(f"O filem escolhido foi o da sala: {opcao}, Não esqueca a pipoca!!!")
         

    