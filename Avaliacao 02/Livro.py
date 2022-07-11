from Publicacao import Publicacao
idL = []


class Livro(Publicacao):
    def __init__(self, id="", dataPublicacao="", titulo=""):
        super().__init__(id, dataPublicacao)
        self.titulo = titulo
        self.__autor = None
        self.ultimo = None
        self.tamanho = 0

    def __str__(self):
        return 40 * "-" + "\n" + super().__str__() + "\nTitulo: " + self.titulo + "\nAutor: " + self.__autor + "\n" + 40 * "-" + "\n"

    def idVerif(self, id):
        for iD in idL:
            if iD == id:
                input("\nID já cadastrado, pressione ENTER para tentar novamente!")
                self.adicionar()

    def adicionar(self):
        print('\n_____Adição de Livros_____')
        id = input('Primeiramente, digite um ID : ')

        dia = input('Dia da publicação: ')
        mes = input('Mês da publicação: ')
        ano = input('Ano da publicação: ')
        data = f'{dia}/{mes}/{ano}'
        super().add(id, data)
        self.titulo = input('Título do Livro: ')
        self.__autor = input('Autor do Livro: ')
        self.idVerif(id)
        idL.append(id)
