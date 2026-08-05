import os

nomes = ["Ana", "Bruno", "Carla", "Daniel", "Elena", "Felipe", 
       "Gabriela", "Hugo", "Isabela", "João", "Karina", "Lucas", 
       "Mariana", "Nicolas", "Olivia", "Pedro", "Quintino", "Rafaela", 
       "Samuel", "Tatiana"]

os.system("cls" if os.name == "nt" else "clear")
# usuario informa nome a ser alterado
nome_antigo = input("Informe o nome a ser alterado: ").strip().title()

# armazena a posição do nome na lista caso exista
if nome_antigo in nomes:
    indice = nomes.index(nome_antigo)
    nomes[indice] = input("Informe o novo nome: ").strip().title()
    print("Nome alterado com sucesso")
    for nome in nomes:
        print(nome)
    
else:
    print("Nome não encontrado") 
    
