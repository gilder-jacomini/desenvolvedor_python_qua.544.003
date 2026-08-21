import os
from models import PessoaFisica, PessoaJuridica




def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    limpar()
    #instanciando objetos
    usuario = PessoaFisica(nome="", cpf="", email="", telefone="", endereco="")
    empresa = PessoaJuridica(razao_social="", nome_fantasia="", cnpj="", email="", telefone="", endereco="")

    usuario.nome = input("Informe o nome do usuário: ").strip().title()
    usuario.cpf = input("Informe o CPF do usuário: ").strip()
    usuario.email = input("Informe o E-mail do usuário: ").strip().lower()
    usuario.telefone = input("Informe o Telefone do usuário: ").strip()
    usuario.endereco = input("Informe o Endereço do usuário: ")

    limpar()
    empresa.razao_social = input("Informe a Razão Social: ").strip()
    empresa.nome_fantasia = input("Informe a Nome Comercial: ").strip()
    empresa.cnpj = input("Informe o CNPJ: ").strip()
    empresa.email = input("Informe o E-mail da empresa: ").strip().lower()
    empresa.telefone = input("Informe o Telefone da empresa: ").strip()
    empresa.endereco = input("Informe o Endereço da empresa: ")

    # saida dos dados
    limpar()
    usuario.exibir_dados()
    empresa.exibir_dados()

if __name__ == "__main__":
    main()