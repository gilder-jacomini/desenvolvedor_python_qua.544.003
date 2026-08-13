# Importação de bibliotecas
import os
# Entrada de dados
os.system("cls" if os.name == "nt" else "clear")

nome = input("Informe seu nome: ").strip() .title()
i = int(input("Informe sua idade: "))
os.system("cls" if os.name == "nt" else "clear")

while True:
    
    print("Filmes em cartaz:")
    print("Sala 1: A Volta Dos Que Não Foram. (livre)")
    print("Sala 2: A Roda Quadrada. (12 anos)")
    print("Sala 3: As tranças do Rei Careca. (14 anos)")
    print("Sala 4: Poeira em Alto Mar. (16 anos)")
    print("Sala 5: A Vingança do Frango Assassino. (18 anos)")
    print("Digite 6 para sair")
    print("\n")

    opcao  = input("Informe o número da sala desejada ou 6 para sair: ")
    
    match opcao:
        case "1":
            id_min = 0
            filme = "A Volta Dos Que Não Foram. (livre)"
        case "2":
            id_min = 12    
            filme = "A Roda Quadrada. (12 anos)"
        case "3":
            id_min = 14
            filme = "As tranças do Rei Careca. (14 anos)"
        case "4":
            id_min = 16  
            filme = "Poeira em Alto Mar. (16 anos)"
        case "5":
            id_min = 18
            filme = "A Vingança do Frango Assassino. (18 anos)"
        case "6" :
            break
        case _:
            print("Opção Inválida")
            
        
    if (opcao == "2" and i < id_min) or (opcao == "3" and i < id_min) or (opcao == "4" and i < id_min) or (opcao == "5" and i< id_min):
        print(f"Sua idade é: {i}")
        print("Idade não compatível com o filme, por favor escolha outra sala ou digite 6 para sair.")
        print("\n")
    else:
        bilhete = "bilhete"
        with open(f"programa_01-02/arquivos/{bilhete}.txt", "w", encoding="utf-8") as f:
            f.write(f"{opcao}, {filme}")
            print(f"O filem escolhido foi o da sala: {opcao}, Não esqueca a pipoca!!!")
            print("\n")

            break
            # encerra o loop

    