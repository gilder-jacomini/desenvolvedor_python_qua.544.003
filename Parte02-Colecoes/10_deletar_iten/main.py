import os

nomes = ["Ana", "Bruno", "Carla", "Daniel", "Elena", "Felipe", 
       "Gabriela", "Hugo", "Isabela", "João", "Karina", "Lucas", 
       "Mariana", "Nicolas", "Olivia", "Pedro", "Quintino", "Rafaela", 
       "Samuel", "Tatiana"]

os.system("cls" if os.name == "nt" else "clear")

# usuario informa nome a ser deletado
nome = input("Informe o nome a ser deletado: ").strip().title()

if nome in nomes:
    indice = nomes.index(nome)
    # apaga o iten da lista
    del(nomes[indice])
    for nome in nomes:
        print(nome)
else:
    print("Nome não encontrado.")