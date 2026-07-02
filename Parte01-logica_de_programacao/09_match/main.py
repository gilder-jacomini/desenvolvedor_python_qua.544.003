# declaração de variáveis
valor1 = float(input("Informe o primeiro número: ").replace(",","."))
valor2 = float(input("Informe o segundo número: ").replace(",","."))

#menu
print("Escolha a operação:")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = input("informe a opção desejada: ").strip()

match opcao:
    case "1": 
        print(f"{valor1} + {valor2} = {valor1 + valor2}")
    case "2":
        print(f"{valor1} - {valor2} = {valor1 - valor2}")
    case "3":
        print(f"{valor1} * {valor2} = {valor1 * valor2}")
    case "4":
        print(f"{valor1} / {valor2} = {valor1 / valor2}")
    case _:
        print("opção inválida, você deve escolher entre: 1 para Somar, 2 para Subtrair, 3 para Multiplicar ou 4 para Dividir.")