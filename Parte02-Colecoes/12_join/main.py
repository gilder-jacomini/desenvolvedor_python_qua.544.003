import os
os.system("cls" if os.name == "nt" else "clear")

nomes = ["Maria","Paula","Amelia"]

# valor que separa os itens na variável
separador = " "

#juntar os valores 

nomes_juntos = separador.join(nomes)

# imprime os nomes juntos
print(nomes_juntos)
