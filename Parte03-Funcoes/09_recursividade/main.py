import os
os.system("cls" if os.name == "nt" else "clear")

def fatorial(n):
    return 1 if n == 1 else n*fatorial(n-1)

def main():
    n = int(input("infome um numero inteiro: "))
    print(f"Fatorial de {n} é: {fatorial(n)}")

if __name__ == "__main__":
    main()