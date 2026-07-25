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

    opcao  = input("Informe o número da sala desejada: ")
    
    match opcao:
        case "2":
            i_min = 12    
        case "3":
            i_min = 14
        case "4":
            i_min = 16  
        case "5":
            i_min = 18
        case "6" :
            break
        case _:
            print("Opção Inválida")
            continue
        
    if (opcao == 2 and i < i_min) or (opcao == 3 and i < i_min) or (opcao == 4 and i < i_min) or (opcao == 5 and i< i_min):
        print("Idade não compatível com o filme, por favor escolha outra sala ou digite 6 para sair.")
    else:
        bilhete = "bilhete"
        with open(f"programa_01-02/arquivos/{bilhete}.txt", "w", encoding="utf-8") as f:
            f.write(opcao)
            print(f"O filem escolhido foi o da sala: {opcao}, Não esqueca a pipoca!!!")
         

    