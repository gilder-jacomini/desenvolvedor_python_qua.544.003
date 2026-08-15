import os
os.system("cls" if os.name == "nt" else "clear")

somar = lambda a,b: a+b

def main():
    a = int(input("Informe o primeiro numero: "))
    b = int(input("Informe o segundo numero: "))
    print(f"O valor da soma é: {somar(a,b)}")
if __name__ == "__main__":
    main()