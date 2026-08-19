# Usando recursividade, crie um programa onde o usuário informa um número inteiro e o programa 
# calcula a sequência Fibonacci até o número informado

import os
os.system("cls" if os.name == "nt" else "clear")

def fibonacci(n):
    # tratando a lista com os menores tamanhos possíveis
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0,1]
    # recursividade, pega a lista com os numeros anteriores (n-1)
    lista_anterior = fibonacci(n-1)
    # pega a lista com 2 passos atrás (n-2)
    lista_retrasada = fibonacci(n-2)
    # descobre o proximo num somando os ultimos elementos de cada lista
    proximo_numero = lista_anterior[-1] + lista_retrasada[-1]
    # retorna a lista anterior com o novo numero adicionado ao final da lista
    return lista_anterior + [proximo_numero]


def main():
    n = int(input("Informe a quantidade de numeros fibonacci deseja: "))
    print(f"a sequencia fibonacci é: {fibonacci(n)}")

if __name__ == "__main__":
    main()

# resolução do professor

def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

def main():
    n = int(input("Informe a quantidade de numeros fibonacci deseja: "))
    print(f"a sequencia fibonacci é: {fibonacci(n)}")

if __name__ == "__main__":
    main()