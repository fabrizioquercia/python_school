from Strumento import  *

class Chitarra(Strumento):
    def __init__(self, nome, materiale, corde):
        super().__init__(nome, materiale)
        self.corde = corde

    def accordare(self):
        return f"Tutte le {self.corde} sono state accordate!"

class Pianoforte(Strumento):
    def __init__(self, nome, materiale, numero_tasti):
        super().__init__(nome, materiale)
        self.numero_tasti = numero_tasti

    def suona_accompagnamento(self):
        return f"Il piano, con i suoi splendidi {self.numero_tasti} tasti, accompagna in modo elegante!"

class Batteria(Strumento):
    def __init__(self,nome, materiale,numero_tamburi):
        super().__init__(nome, materiale)
        self.nome = nome
        self.numero_tamburi = numero_tamburi

    def sbatti_tamburi(self):
        return f"Il batterista colpisce uno dei suoi {self.numero_tamburi} simpatici ed allegri tamburi!"

class Violino(Strumento):
    def __init__(self,nome,materiale,numero_corde):
        super().__init__(nome,materiale)
        self.numero_corde = numero_corde

    def pizzica_violino(self):
        return f"Il violinista ha pizzicato tutte le {self.numero_corde} corde del suo portentoso violino!"
