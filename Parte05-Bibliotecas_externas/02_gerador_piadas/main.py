import pyjokes
from deep_translator import GoogleTranslator
import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def gerar_piada():
    tradutor = GoogleTranslator(source='auto', target='pt')
    piada = pyjokes.get_joke()
    return tradutor.translate(piada)

def main():
    limpar()
    while True:
        print("0 - Sair")
        print("1 - Gerar piada")
        opcao = input("Escolha uma opção: ")
        limpar()
        if opcao == "0":
            break
        elif opcao == "1":
            piada = gerar_piada()
            print(piada)
            continue
        else:
            print("Opção inválida. Tente novamente.")
            continue


    
if __name__ == "__main__":
    main()
