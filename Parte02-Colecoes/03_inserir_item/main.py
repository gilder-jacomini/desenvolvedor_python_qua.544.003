# biblioteca OS
import os

# usuario insere itens na lista
nomes = []

# limpa o console
os.system("cls" if os.name == "nt" else "clear")

while True:    
    nome = input("Informe um nome: ").strip().title()
    
    # insere nome na lista
    nomes.append(nome)
    
    print("Deseja inserir mais um nome? ")
    print("'S' para sim")
    print("'Qaulquer outro valor para não")
    opcao = input("Sua resposta: ").strip()
    
    os.system("cls" if os.name == "nt" else "clear")
    
    match opcao:
        case "s":
            continue
        case _:
            break
        
print("Lista de nomes:\n")
for i, nome in enumerate(nomes, start =1):
    print(f"{i}° nome: {nome}")

