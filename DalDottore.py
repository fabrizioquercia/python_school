import datetime

class Paziente:
    def __init__(self, nome, codice):
        self.nome = nome
        self.codice = codice
        

class ProntoSoccorso:
    def __init__(self):
        self.lista = []

    def aggiungi_paziente(self, paziente):
        pass
        







# funzione che ottiene l'oario e lo ritorna (fatta stand-alone)
def get_orario():
    orario = datetime.now()
    ora=orario.strftime("%H:%M")
    data=orario.strftime("%D")
    return (data + " " + ora)

