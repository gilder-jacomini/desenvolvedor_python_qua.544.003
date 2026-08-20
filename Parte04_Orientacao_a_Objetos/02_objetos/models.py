# criando a classe
class Pessoa:
    # método construtor
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

    def apresentar(self):
        return f"Ola, meu nome é: {self.nome}, e tenho: {self.idade} anos"

    def cumprimentar(self, nome):
        return f"Prazer em te conhecer, {nome}, meu email é: {self.email} e meu telefone é: {self.telefone}."