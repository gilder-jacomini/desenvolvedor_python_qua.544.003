import os
import math

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def quadrilatero(b, h):
    return b*h

def triangulo(b, h):
    return (b*h) /2

def circulo(r):
    return math.pi*r**2

limpar()
while True:
    print("1- para calcular a area de um quadrilátero")
    print("2- para calcular a area de um triângulo")
    print("3- para calcular a area de um círculo")
    print("4- Sair")
    opcao = input("Informe a opçaõ desejada: ")

    limpar()

    match opcao:
        case "1":
            b = float(input("Informe o valor da base: ").replace(",","."))
            h = float(input("Informe o valor da altura: ").replace(",","."))
            print(f"A área do quadrilátero é: {quadrilatero(b,h)}.")
            continue

        case "2":
            b = float(input("Informe o valor da base: ").replace(",","."))
            h = float(input("Informe o valor da altura: ").replace(",","."))
            print(f"A área do triângulo é: {triangulo(b,h)}.")
            continue

        case "3":
            r = float(input("Informe o valor do raio: ").replace(",","."))
            print(f"A área do círculo é: {circulo(r):.2f}")
            continue

        case "4":
            break
        case _:
            print("Opção inválida")
    