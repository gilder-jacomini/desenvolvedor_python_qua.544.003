import os

# cria a lista
nomes = ["Fulano","Alex","Eduardo","Cicrano","Beltrano"]

os.system("cls" if os.name == "nt" else "clear")

nomes.sort(reverse=True)

for nome in nomes:
    print(nome)


