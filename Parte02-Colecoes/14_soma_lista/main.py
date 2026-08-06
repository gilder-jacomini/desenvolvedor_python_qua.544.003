import os
os.system("cls" if os.name == "nt" else "clear")

numeros = [10, 15, 12, 8, 26, 100]

#soma todos os numeros da lista
soma = sum(numeros)

#retorna a quantidade de itens na lista
itens = len(numeros)

#imprime a qunatidade de itens que essa lista tem
print(f"Total da itens: {itens}")

#imprime o valor total da soma
print(f"Total da soma: {soma}")

#calcula a média
media = soma / itens

print(f"A média da lista é: {media}")













