# importação de bibliotecas
import os

# limpeza de tela no terminal utilizando a biblioteca "os" importada acima
os.system("cls" if os.name == "nt" else "clear") 

try:
    while True:
        print("1 - Gravar arquivo")
        print("2 - Ler arquivo")
        print("3 - Sair")

        # a opção .trip() retira os espaços
        opcao = input("Informe a opção desejada: ").strip()

        os.system("cls" if os.name == "nt" else "clear") 

        match opcao:
            case "1":
                novo_texto = input("Informe o texto a ser gravado: ")
                nome_arquivo = input("Informe o nome do arquivo: ").strip()

                # grava novo arquivo, nesse caso a extenção está sendo setada para .txt
                with open(f"17_arquivos/arquivos/{nome_arquivo}.txt", "w", encoding="utf-8") as f:
                    f.write(novo_texto)
                    
            case "2":
                nome_arquivo = input("Digite o nome do arquivo: ").strip()
                try:
                    
                    with open(f"17_arquivos/arquivos/{nome_arquivo}.txt", "r", encoding="utf-8") as f:
                        conteudo = f.read()
                    print(conteudo)
                    continue

                except FileNotFoundError:
                    print("Arquivo não encontrado")
                continue

            case "3":
                print("Programa encerrado") 
                break
            
            case _:
                print("Opção Inválida")
                continue
                
        
except Exception as e:
    print(f"Alguma coisa deu errado, verifique!!! {e}")
          


