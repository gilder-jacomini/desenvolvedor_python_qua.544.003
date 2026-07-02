# declaração de variáveis
nome = input("Informe o nome do aluno: ")
nota = float(input("Informe a nota do aluno - O valor deve estar entre 0 e 10: ").replace(",","."))

# varifica se a nota é válida
if nota >= 0 and nota <= 10:
    if nota >=7:
        print(f"{nome} está aprovado")
    elif nota >=5:
        print(f"{nome} Está de recuperação")
    else:
        print(f"{nome} está reprovado")
else:
    print(f"Nota de {nome} é inválida, por favor informe uma nota entre 0 e 10")
