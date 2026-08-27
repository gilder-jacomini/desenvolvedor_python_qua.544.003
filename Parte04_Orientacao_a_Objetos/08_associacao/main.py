from models import Endereco, Pessoa

def main():
    endereco = Endereco(uf="", cidade="")
    usuario = Pessoa(nome="", endereco=endereco)

    usuario.nome = input("Digite o nome do usuário: ").strip().title()
    usuario.endereco.uf = input("Digite a UF do endereço: ").strip().upper()
    usuario.endereco.cidade = input("Digite a cidade do endereço: ").strip().title()

    usuario.apresentar_endereco()


if __name__ == "__main__":
    main()