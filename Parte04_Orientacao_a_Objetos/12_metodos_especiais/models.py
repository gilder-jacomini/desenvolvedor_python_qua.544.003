class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def __str__(self):
        return f"Olá, meu nome é {self.nome}, tenho {len(self)} anos e minha altura é {float(self):.2f}m 👍"

    def __len__(self):
        return (self.idade)

    def __float__(self):
        return self.altura