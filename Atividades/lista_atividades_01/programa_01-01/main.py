"""
Como fazer a conta Use o peso em quilos (kg).Use a altura em metros (m).Multiplique a altura por ela mesma.
Divida o peso por esse valor da altura.O que o resultado significa para adultos
Menor que 18,5: Abaixo do peso.
Entre 18,5 e 24,9: Peso normal ou ideal.
Entre 25,0 e 29,9: Sobrepeso.
30,0 ou mais: Obesidade (graus I, II ou III)
"""
import math
import os

try:
    os.system("cls" if os.name == "nt" else "clear")
# Entrada de dados    
    nome = input("Informe o nome: ").strip().title()
    peso = float(input("Informe o peso em kilos: ").replace(",","."))
    altura = float(input("Informe o altura em metros ").replace(",","."))    

    imc = peso / (altura **2) 

    if imc < 18.5:
        print(f"O imc: {imc:.2f} = Abaixo do peso.")
    elif imc > 18.5 or imc < 24.9:
        print(f"O imc: {imc:.2f} = Peso normal ou ideal.")
    elif imc > 25 or imc < 29.9:
        print(f"O imc: {imc:.2f} = Sobrepeso.")
    elif imc > 30:
        print(f"O imc: {imc:.2f} = Obesidade (graus I, II ou III).")
       

except Exception as e:
    print("Algo deu errado verifique o código")        
