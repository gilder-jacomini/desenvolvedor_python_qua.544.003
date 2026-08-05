import os
nomes = ["Fulano","Alex","Eduardo","Cicrano","Beltrano"]

os.system("cls" if os.name == "nt" else "clear")

# ordena a lista
nomes.sort()

for nome in nomes:
    print(nome)