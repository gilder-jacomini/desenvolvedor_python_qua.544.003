from modulo import limpar, somar, subtrair

def main():
    limpar()

    a = int(input("Informe o valor de a: "))
    b = int(input("Informe o valor de b: "))
    limpar()
    print(f"O valor da soma é: {somar(a,b)}")
    print(f"O valor da subtração é: {subtrair(a,b)}")

if __name__ == "__main__":
    main()