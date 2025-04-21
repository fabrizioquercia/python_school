class Strumento():
    def __init__(self, nome, materiale):
        self.nome = nome
        self.materiale = materiale

    def get_descrizione(self):
        return self.materiale

