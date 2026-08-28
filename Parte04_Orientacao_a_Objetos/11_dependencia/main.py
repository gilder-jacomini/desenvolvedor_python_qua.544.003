import os
from models import Pedido

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    pedido = Pedido(valor1=0.0, valor2=0.0)

    limpar_tela()

    pedido.valor1 = float(input("Digite o primeiro valor: ").replace(',', '.'))
    pedido.valor2 = float(input("Digite o segundo valor: ").replace(',', '.'))

    limpar_tela()

    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")

    operador = input("Escolha a operação desejada (1-4): ").strip()
    print(pedido.calcular_total(operador=operador))

if __name__ == "__main__":
    main()