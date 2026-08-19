# Utilizando o conceito de módulo, crei um módulo com funções que façam as seguintes ações
# Limpa o terminal
# Calcula a potência de um número informado pelo usuário elevado a outro numero informado pelo usuário
# Calcula a raiz quadrada de um número informado pelo usuário
# Calcula o volume de um recipente paralelepípedo
# Calcula o volume de um recipente cilíndrico
# Em seguida, faça um programa que o usuário escolha executar uma dessas funções ou sair do programa
from modulo import limpar, potencia, raiz, paralelepipedo, cilindrico
import os
def main():
    while True:
        print("1 - para limpar o terminal")
        print("2 - para calcular a potencia de um número")
        print("3 - para calcular a raiz quadrada de um número")
        print("4 - para calcular a o volume de um paralelepípedo")
        print("5 - para calcular a o volume de um cliclindro")
        print("6 - para sair")
        opcao  = input("Informe a opção desejada: ")

        match opcao:
            case "1":
                limpar()  
           
            case "2":
                base = int(input("Informe o valor da base: "))
                expoente = int(input("Informe o valor do expoente: "))
                print(f"O valor da potência é: {potencia(base,expoente)}")
                continue
            case "3":
               n = int(input("Informe o numero a ser calculado a raiz: "))
               print(f"O valor da raiz é: {raiz(n)}")
               continue
            case "4":
               a = int(input("Informe o valor da altura: "))
               l = int(input("Informe o valor da Largura: "))
               c = int(input("Informe o valor do comprimento: "))
               print(f"O valor do volume do paralelepipedo é: {paralelepipedo(a,l,c)}")
               continue
            case "5":
               r = int(input("Informe o valor do raio: "))
               h = int(input("Informe o valor da altura: "))
               print(f"O valor volume do cilindro é: {cilindrico(r,h)}")
               continue
            case "6":
               break
           
            case _:
               print("Opção inválida")


if __name__ == "__main__":
    main()