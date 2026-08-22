import os
from models import PessoaFisica, PessoaJuridica

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    usuario = PessoaFisica(nome="",cpf="", email="", telefone="")
    empresa = PessoaJuridica(nome_fantasia="",cnpj="", email="", telefone="")
    limpar()

    usuario.nome = input("Informe o nome do usuário: ").strip().title()
    usuario.cpf = input("Informe o cpf do usuário: ").strip()
    usuario.email = input("Informe o E-mail do usuário: ").strip().lower()
    usuario.telefone = input("Informe o telefone do usuário: ").strip()

    limpar()

    empresa.nome_fantasia = input("Informe o nome Comercial da empresa: ").strip().title()
    empresa.cnpj = input("Informe o  CNPJ da empresa: ").strip()
    empresa.email = input("Informe o E-mail da empresa: ").strip().lower()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()

    limpar()
    print(f"Nome do usário: {usuario.nome}")
    print(f"CPF do usário: {usuario.cpf}")
    print(f"email do usário: {usuario.email}")
    print(f"Telefone do usário: {usuario.telefone}")
    print(f"Nome da empresa: {empresa.nome_fantasia}")
    print(f"CNPJ da empresa: {empresa.cnpj}")
    print(f"E-mail da empresa: {empresa.email}")
    print(f"Telefone da empresa: {empresa.telefone}")

if __name__ == "__main__":
    main()