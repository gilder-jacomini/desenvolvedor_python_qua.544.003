# Utilizando o conceito de módulo, crei um módulo com funções que façam as seguintes ações
# Limpa o terminal
# Calcula a potência de um número informado pelo usuário elevado a outro numero informado pelo usuário
# Calcula a raiz quadrada de um mnúmero informado pelo usuário
# Calcula o volume de um recipente paralelepípedo
# Calcula o volume de um recipente cilíndrico
# Em seguida, faça um programa que o usuário escolha executar uma dessas funções ou sair do programa

import os
import math

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def potencia(b,e):
    return b**e

def raiz(n):
    return math.sqrt(n)
    
def paralelepipedo(a,b,c):
    return  a*b*c
    
def cilindrico(r):
    return math.pi*r**2



