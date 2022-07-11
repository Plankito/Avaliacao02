from Publicacao import Publicacao
idR = []

class Revista(Publicacao):
    def __init__(self, id = "", dataPublicacao = ""):
        super().__init__(id, dataPublicacao)
        self.__preco = None

    def __str__(self):
        return 40*"-" + "\n" + super().__str__() + "\nPreço: R$" + self.__preco + "\n" + 40*"-" + "\n"

    def idVerif(self, id):
        for iD in idR:
            if iD == id:
                input("\nID já cadastrado, pressione ENTER para tentar novamente!")
                self.adicionar()

    def adicionar(self):
        print('\n_____Adição de Revistas_____')
        id = input('Primeiramente, digite um ID : ')
        data = input('Agora, a data de publicação: ')
        super().add(id, data)
        self.__preco = input('Preço da Revista: ')
        self.idVerif(id)
        idR.append(id)
