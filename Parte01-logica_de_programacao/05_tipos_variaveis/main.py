# declarando variaveis

# todo input retorna uma string
nome = input("Informe seu nome: ").title()

# definindo a variavel para o formato desejado
idade = int(input("Informe sua idade: "))

# o comando replace substitui um termo pelo desejado
altura = float(input("Informe sua altura: ").replace(",","."))

# saída de dados

print(f"Seu nome é {nome}. {type(nome)}")
print(f"Sua idade é {idade} anos {type(idade)}.")
print(f"Sua altura é {altura}m {type(altura)}.")