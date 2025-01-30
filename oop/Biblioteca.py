import os

class Biblioteca():

    def __init__(self, libri):
        self.libri = libri

    def lista(self):
        cnt = len(self.libri)
        print("---------------------------")
        print(f" I Nostri Libri: {cnt}")
        print("---------------------------")
        for l in self.libri:
            print(f"> {l}")
        print("---------------------------")

    def aggiungi(self, titolo):
        esiste = self.verifica_esiste(titolo)
        if esiste == True:
            self.libri.append(titolo)

    def verifica_esiste(self, titolo):
        for l in self.libri:
            if l == titolo: 
                return True
        return False

    def verifica_disponibile(self, titolo):
        t = f"Il libro {l}"
        for l in self.libri:
            if l == titolo: 
                t  = t + " esiste!"
                break
            else:
                t = t +" NON esiste!"
        return t


os.system("cls")

while True:

    ls = ["Errore di sistema", "Cocoon", "Asimov"]
    #lista
    B = Biblioteca(ls)
    B.lista()

