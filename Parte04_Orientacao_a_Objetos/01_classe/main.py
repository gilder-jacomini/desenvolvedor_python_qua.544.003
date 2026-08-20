# criação da classe pessoa

class Pessoa:
    # metodo construtor
    def __init__(self, nome, idade, email, altura):
        # atributos
        self.nome = nome
        self.idade = idade
        self.email = email
        self.altura = altura

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Email: {self.email}") 
        print(f"Altura: {self.altura} metros")

def main():
    # instanciar a classe (criar o objeto)
    usuario = Pessoa(nome="", idade=0, email="", altura=0.0)

    usuario.nome = input("informe o nome: ").strip() .title()
    usuario.idade = int(input("informe a idade: "))
    usuario.email = input("informe o e-mail: ").strip() .lower()
    usuario.altura = float(input("informe a altura em metros: ").replace(",","."))

    usuario.exibir_dados()

    
if __name__ == "__main__":
    main()