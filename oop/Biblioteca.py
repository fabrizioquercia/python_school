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
        if esiste == False:
            self.libri.append(titolo)

    def verifica_esiste(self, titolo):
        if titolo in self.libri:
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
    
def bootstrap():
    versione = 1.0
    print("---------------------------------------------------")
    print("#####   \33[45m GESTIONE BIBLIOTECA (versione " + str(versione) + ") \033[0m  ##### ")
    print("---------------------------------------------------")



os.system("cls")
bootstrap()


ls = ["Errore di sistema", "Cocoon", "Asimov"]
#lista
B = Biblioteca(ls)
B.lista()
print()
libro = str( input("Aggiungi libro: ") )
esiste = False
if B.verifica_esiste(libro) == False:
    B.aggiungi(libro)
    B.lista()
else:
    print("esiste")

print()
B.lista()


