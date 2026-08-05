import os
# cria a lista com as cidades
cidades = [
    "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal",
    "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul",
    "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí",
    "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia",
    "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"
]

os.system("cls" if os.name == "nt" else "clear")

cidade = input("Informe a cidade a ser pesquisada: ").strip().title()

# mostra a posição do item na lista
if cidade in cidades:
    indice = cidades.index(cidade)
    print (f"A posição da cidade {cidade} é: {indice}")
    
else:
    print("Cidade não encontrada.")