from deep_translator import GoogleTranslator
import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def tradutor(texto):
    tradutor = GoogleTranslator(source='auto', target='pt')
    return tradutor.translate(texto)

def main():
    limpar()
    while True:
        print("0 - Sair do programa")
        print("1 - Traduzir texto para pt-BR")
        opcao = input("Escolha uma opção: ").strip()
        limpar()
        if opcao == "0":
            print("Saindo do programa...")
            break
        elif opcao == "1":
            try:
                texto = input("Digite o texto a ser traduzido: ")
                traducao = tradutor(texto)
                print(f"\n Texto traduzido: {traducao}\n")
                continue
            except Exception as e:
                print(f"Erro ao traduzir o texto: {e}")
        else:
            print("Opção inválida. Tente novamente.")
            continue




if __name__ == "__main__":
    main()