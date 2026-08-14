import modulo as m

def main():
    m.limpar()

    nome = input("Informe seu nome: ").strip().title()
    idade = int(input("Informe sua idade: "))
    print(f"{nome} {m.maioridade(idade)}")

if __name__ == "__main__":
    main()