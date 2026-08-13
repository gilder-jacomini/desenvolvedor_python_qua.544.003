# Crie um programa que receba o nome de um aluno e três notas. O sistema deve calcular a média e informar se o aluno está aprovado 
# (média mínima 7,0) ou reprovado. Os dados devem ser gravados em um arquivo JSON. Ao final, o usuário deve escolher se deseja
# inserir as notas de outro aluno, que serão gravadas no mesmo arquivo JSON.
import json
import os
os.system("cls" if os.name == "nt" else "clear")


# Criando a lista
alunos = []
# laco de repetição para criar a inserção de alunos e notas/situação no json
while True:
    print("1- Gravar novo aluno/notas")
    print("2- Listar alunos/médias")
    print("3- Sair")
    opcao = input("Informe a opçaõ desejada: ").strip()
    
    os.system("cls" if os.name == "nt" else "clear")
    
    match opcao:
        case "1":
            # Cria um novo dicionário
            aluno = {}
            # recebe o nome do aluno
            aluno['nome'] = input("Informe o nome do aluno: ").strip().title()
            
            #recebe as notas e converte para float
            n01 = float(input ("Informe a 1ª nota: ").replace(",","."))
            n02 = float(input ("Informe a 2ª nota: ").replace(",","."))
            n03 = float(input ("Informe a 3ª nota: ").replace(",","."))
            
            #insere no dicionário "aluno" as notas
            aluno['n01'] = n01
            aluno['n02'] = n02
            aluno['n03'] = n03
            
            #calcula a média das notas
            media = (n01 + n02 + n03) / 3
            
            #adiciona a media no dicionario arredondando para o inteiro com 2 casas decimais
            aluno['media'] = round(media, 2)
            
            #adiciona a situação no dic, verificar se aprovado ou não
            aluno['situacao'] = "Aprovado" if media >= 7  else "Reprovado"
            
            # Adiciona o dicionário "aluno" na lista "alunos"
            alunos.append(aluno)
            
            # Grava os dados no arquivo .json
            with open(f"atividades_03/atividade.json" , "w" , encoding="utf-8") as f:
                json.dump(alunos, f)
            continue
            
        case "2":
            #Lista o alunos bem como sua media e se está aprovado/reprovado
            if not alunos:
                print("Não há nenhum aluno cadastrado")
            else:
                with open(f"atividades_03/atividade.json" , "r" , encoding="utf-8") as f:
                    alunos = json.load(f)
                for aluno in alunos:
                    for chave , valor in aluno.items():
                        print(f"{chave.capitalize()}: {valor}")
                print("-----")
            continue
        
        case "3":
            break
        
        case _:
            print("Opção inválida!")
            continue
