# importacao da biblioteca
import time
import os
# Limpa a tela
os.system("cls" if os.name == "nt" else "clear")
# tratamento de exceção
try:
    # Entrada de dados
    n = int(input("Informe um número inteiro: "))

    # Limpa a tela
    os.system("cls" if os.name == "nt" else "clear")

    # contagem
    while n >=0:
        print(f"{n}...")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        n -= 1
    print("BOOOOOM!!!!!!💣")


except Exception as e:
    print(f"Não foi possível iniciar a contagem. {e}")