class Cliente:
    def __init__(self, nome):
        self.nome = nome

    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome}"