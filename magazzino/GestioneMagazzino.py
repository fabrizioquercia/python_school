import unittest


class GestioneMagazzino:

    def __init__(self, nome, prezzo, quantita):
        self.nome = nome
        self.prezzo = prezzo
        self.quantita = quantita

    def restock(self, quantita):
        if int(quantita) > 0:
            self.quantita += int(quantita)
            print("Sono stati aggiunti ", quantita, "pezzi")
            return True
        print("Impossibile aggiuntre: La quantita è minore di 0 o non è un numero positivo!")
        return False

    def vendi(self, quantita):
        if int(quantita) > 0 and self.quantita > int(quantita):
            self.quantita -= int(quantita)
            print(quantita, "pezzi sono stati venduti!")
            return True
        print("Vendita annullata; non vi erano quantità sufficienti o il valore immesso non è un numero positivo")
        return False
    

mouse = GestioneMagazzino("Mouse", 10, 2)

# aggiungo
print("PRODOTTO:", mouse.nome)
print("Prezzo iniziale: ", mouse.prezzo)
print("Quantità iniziale: ", mouse.quantita)
print()
n_restock =input("Quante unità fai di restock?")
mouse.restock(n_restock)
print("Quantità dopo restock: ", mouse.quantita)
print()
n_vendi = input("Quante unità vendere?")
mouse.vendi(n_vendi)
print("Quantità rimanente in magazzino dopo vendita: ", mouse.quantita)


class TestMagazzino(unittest.TestCase):

    def setUp(self):
        pass

