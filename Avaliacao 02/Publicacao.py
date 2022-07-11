class Publicacao:
    def __init__(self, id, dataPublicacao):
        self.id = id
        self.data = dataPublicacao

    def __str__(self):
            return "Id: " + self.id + "\nData da Publicação: " + self.data

    def add(self, id, data):
        self.id = id
        self.data = data

