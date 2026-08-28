
import os
from models import Pessoa

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    limpar()

    usuario = Pessoa(nome="", idade=0, altura=0.0)
    usuario.nome = input("Digite seu nome: ").strip().title()
    usuario.idade = int(input("Digite sua idade: "))
    usuario.altura = float(input("Digite sua altura: ").replace(",", "."))

    limpar()

    print(usuario)
    print(len(usuario))
    print(float(usuario))

    del(usuario)  # Deletando o objeto da memória

if __name__ == "__main__":
    main()