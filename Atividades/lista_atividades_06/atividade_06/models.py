from abc import ABC, abstractmethod
from dataclasses import dataclass

class IConta(ABC):
    @abstractmethod
    def depositar(valor):
        pass

    @abstractmethod
    def sacar(valor):
        pass

    @abstractmethod
    def gerar_extrato():
        pass

    @abstractmethod
    def consultar_dados():
        pass
    

@dataclass
class Pessoa:
    nome: str
    cpf: str


@dataclass
class Conta(IConta):
    
    titular: Pessoa
    agencia: str
    n_conta: str
    saldo: float

    #métodos
    def depositar(self, valor):
        self.__saldo += valor
        return self.__saldo
    
    def sacar(self, valor):
        self.__saldo -= valor
        return self.__saldo

    def consultar_dados(self):
        print(f'Nome: {self.__titular.nome}')
        print(f'CPF: {self.__titular.cpf}')
        print(f'Agência: {self.__agencia}')
        print(f'Número da Conta: {self.__n_conta}')
        print(f'Saldo: {self.__saldo}')

    def gerar_extrato(self):
        nome_arquivo = f'{self.__titular.nome}.txt'
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(f'Nome: {self.__titular.nome}\n')
            arquivo.write(f'CPF: {self.__titular.cpf}\n')
            arquivo.write(f'Agência: {self.__agencia}\n')
            arquivo.write(f'Número da Conta: {self.__n_conta}\n')
            arquivo.write(f'Saldo: {self.__saldo}\n')
        print(f'Extrato gerado com sucesso no arquivo: {nome_arquivo}')



   
    