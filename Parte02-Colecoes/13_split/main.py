import os
os.system("cls" if os.name == "nt" else "clear")

# variável a ser separada
localidade = "Brasília - DF"

lista = localidade.split(" - ")

#saida da lista separada
for item in lista:
    print(item)


