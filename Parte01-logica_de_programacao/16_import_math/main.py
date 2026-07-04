# importação das bibliotecas
import math
import os

#tratamento de exceção
try:
    while True:
        # entrada dos dados, sempre que tiver uma variável float é bom colocar o replace 
        r = float(input ("Informe o valor do raio: ").replace(",","."))

        # calcular a área do círculo
        area = math.pi * r**2

        #saida do dados
        print(f"Área do círculo é: {area:.2f}m².")

        #usuario decide se continua ou encerra o programa
        print("\n1 - Realizar outro cáuculo.")
        print("2 - Encerrar o programa.")

        opcao = input(f"informe a opção desjada ").strip()

        match opcao:
            case "1":
                continue
            case "2":
                break
            case _:
                print("Opção inválida")


except Exception as e:
    print(f"Não foi possível calcular. {e}")


