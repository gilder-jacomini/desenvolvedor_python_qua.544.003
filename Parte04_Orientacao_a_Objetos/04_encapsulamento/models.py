class Pessoa:
    def __init__(self,nome,cpf,email,telefone):
        self.__nome = nome
        self.__cpf = cpf 
        self.__email = email 
        self.__telefone = telefone

# colocando 1 undersocre fica protect
# colocando 2 undercore fica do tipo private, fica visivel somente dentro da classe

    # métodos de acesso
    # comecar pelo método get - acessa o valor do atributo
    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
            return self.__cpf
    
    @property
    def email(self):
            return self.__email
    
    @property
    def telefone(self):
            return self.__telefone

    # set = definir valor do atributo
    @nome.setter
    def nome(self, nome):
          self.__nome = nome

    @cpf.setter
    def cpf(self, cpf):
              self.__cpf = cpf

    @email.setter
    def email(self, email):
              self.__email = email

    @telefone.setter
    def telefone(self, telefone):
              self.__telefone = telefone
    