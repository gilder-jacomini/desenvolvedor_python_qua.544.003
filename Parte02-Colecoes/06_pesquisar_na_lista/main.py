import os
cidades = [
    "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal",
    "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul",
    "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí",
    "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia",
    "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"
]

os.system("cls" if os.name == "nt" else "clear")

# informa o nome da cidade a ser pesquisado
cidade_pesquisada = input("Informe o nome da cidade a ser pesquisada: ").strip().title()

# retorna resultado

print(f"A cidade {cidade_pesquisada} foi encontrada(o) na pesquisa." if cidade_pesquisada in cidades else "Cidade não encontrada.")

    
