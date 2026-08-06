import os
os.system("cls" if os.name=="nt" else "clear")


nomes = ["Ana", "Bruno", "Carla", "Daniel", "Elena", "Felipe", "Gabriela", "Hugo", "Isabela", "João", "Karina", "Lucas", 
         "Mariana", "Nicolas", "Olivia", "Pedro", "Quintino", "Rafaela", "Samuel", "Tatiana"]

nome = input("Informe o nome a ser separado: ").strip().title()
if nome in nomes:
    #variavel indice recebe a posicao do nome 
    indice = nomes.index(nome)
    
    #variável separado recebe esse indice
    nome_separado = nomes.pop(indice)
    
    #imprime a lsita sem o nome separado
    for nome in nomes:
        print(nome)
    #print("\n")
        #imprime o nome separado
    print(f"\nNome separado da lista: {nome_separado} ")
else:
    print("Nome não encontrado.")













