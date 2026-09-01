import os
from models import IConta, Conta, Pessoa

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    limpar()
    
    titular = Pessoa(
        nome=input("Digite o nome do titular: ").strip().title(),
        cpf=input("Digite o CPF do titular: ").strip()
    )
    # Criando uma instância de Conta
    conta = Conta(
        pessoa=titular,
        agencia="001",
        n_conta="12345-6",
        saldo=1000.0
        
    )

    print(f"Conta criada com sucesso para {conta.pessoa.nome}!")

    while True:
        print("\nEscolha uma opção:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Consultar dados")
        print("4. Gerar extrato")
        print("5. Sair")

        opcao = input("Opção: ")

        match opcao:
            case "1":
                valor = float(input("Digite o valor a depositar: "))
                conta.depositar(valor)
                print(f"Depósito de R${valor:.2f} realizado com sucesso!")
            case "2":
                valor = float(input("Digite o valor a sacar: "))
                conta.sacar(valor)
                print(f"Saque de R${valor:.2f} realizado com sucesso!")
            case "3":
                conta.consultar_dados()
            case "4":
                conta.gerar_extrato()
            case "5":
                print("Saindo do programa...")
                break
            case _:
                print("Opção inválida!")

if __name__ == "__main__":
    main()