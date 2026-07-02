#declaracao de variaveis
nome = input("informe seu nome: ")
telefone = input("Informe seu telefone: ")

# saida de dados

# 1 forma de concatenar
print("Olá",nome, ", seu telefone é:", telefone, ".")       

# 2 forma de concatenar
print("Olá "+ nome +  ", seu telefone é: " + telefone + ".")       

# 3 forma de concatenar
print("Olá {}, seu telefone é: {}." .format(nome, telefone))       

# 4 forma de concatenar
print(f"Olá {nome}, seu telefone é: {telefone}.")