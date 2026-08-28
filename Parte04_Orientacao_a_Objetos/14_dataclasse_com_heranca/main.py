import os
from models import PessoaFisica, PessoaFisica, PessoaJuridica

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():

    limpar()

    usuario = PessoaFisica(nome="",cpf="",profissao="",idade=0,salario=0.0,telefone="",email="")
    empresa = PessoaJuridica(razao_social="",nome_fantasia="",cnpj="",valor_de_mercado=0.0,telefone="",email="")

    usuario.nome = input("Digite o nome do usuário: ").strip().title()
    usuario.cpf = input("Digite o CPF do usuário: ").strip()
    usuario.profissao = input("Digite a profissão do usuário: ").strip().title()
    usuario.idade = int(input("Digite a idade do usuário: ").strip())
    usuario.salario = float(input("Digite o salário do usuário: ").replace(",","."))
    usuario.telefone = input("Digite o telefone do usuário: ").strip()
    usuario.email = input("Digite o email do usuário: ").strip().lower()

    empresa.razao_social = input("Digite a razão social da empresa: ").strip().title()
    empresa.nome_fantasia = input("Digite o nome fantasia da empresa: ").strip().title()
    empresa.cnpj = input("Digite o CNPJ da empresa: ").strip()
    empresa.valor_de_mercado = float(input("Digite o valor de mercado da empresa: ").replace(",","."))
    empresa.telefone = input("Digite o telefone da empresa: ").strip()
    empresa.email = input("Digite o email da empresa: ").strip().lower()

    print(usuario)
    print(empresa)  
    del usuario
    del empresa

    
if __name__ == "__main__":
    main()  