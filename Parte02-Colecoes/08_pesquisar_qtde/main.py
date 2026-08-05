import os
# cria a lista com as cidades
paises = [
    "Brasil", "Argentina", "Portugal", "Japão", "Canadá",
    "Brasil", "Argentina", "Portugal", "Japão", "Canadá",
    "França", "Itália", "Alemanha", "Espanha", "México",
    "Estados Unidos", "Chile", "Colômbia", "Austrália", "China","Brasil",
    "México", "Irã"
]

os.system("cls" if os.name == "nt" else "clear")

pais = input("Informe o nome do País a ser pesquisado: ").strip().title()

# retornar a qtde de itens que tem dentro da lista

qtde = paises.count(pais)
print(f"{pais} Foi encontrado {qtde} vezes na lista ")