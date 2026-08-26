import os
from models import Filho


def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    limpar()

    zezinho = Filho(
        nome="", cpf="", email="", telefone="", profissao="",
        peso=0.0, altura=0.0, olhos="", cabelo=""
    )

# entrada dos dados
    zezinho.nome = input("Informe o nome: ").strip().title()
    zezinho.cpf = input("Informe o CPF: ").strip()
    zezinho.email = input("Informe o E-mail: ").strip().lower()
    zezinho.telefone = input("Informe o Telefone: ").strip()
    zezinho.profissao = input("Informe o Profissão: ").strip()
    zezinho.peso = float(input("Informe o Peso em kg: ").replace(",","."))
    zezinho.altura = float(input("Informe o Altura em metros: ").replace(",","."))
    zezinho.olhos = input("Informe a cor dos Olhos: ").strip()
    zezinho.cabelo = input("Informe a cor do cabelo: ").strip()

    limpar()
        
    zezinho.exibir_dados()        
    zezinho.mostrar_fisico()

if __name__ == "__main__":
    main()
