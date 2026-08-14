import modulo

modulo.limpar()
a = float(input("Informe o valor de 'a': ").replace(",","."))
b = float(input("Informe o valor de 'b': ").replace(",","."))

print(f"O valor da equação é: {modulo.equacao_primeiro_grau(a, b)}")