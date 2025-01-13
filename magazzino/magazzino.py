#magazzino
class Prodotto():

    inventario = {"Prodotto 1 (Pizza)" : 0, 
                    "Prodotto 2 (Carne)": 0, 
                    "Prodotto 3 (Pesce)": 0}

    def __init__(self):
        self.nome = ""
        self.quantita = 0

    def aggiungi_scorta(self, nome):
        qty = int(input("Aggiungi quantità al prodotto " + nome +". Quanti ne aggiungo?: "))
        if int(qty) > 0:
            self.inventario[nome] += qty
        else:
            print("La quantità inserita non è un numero intero maggiore di 0, operazione non valida.")
    
    def rimuovi_scorta(self, nome):
        qty = int(input("Rimuovi quantità dal prodotto " + nome +". Quanti ne rimuovo?: "))
        if int(qty) > 0:
            if self.inventario[nome] >= qty:
                self.inventario[nome]-= qty
            else:
                self.inventario[nome] = 0
        else:
            print("La quantità inserita non è un numero intero maggiore di 0, operazione annullata.")
    
    def get_nome(self, indice):
        pass

    def lista_prodotti(self):
        i = 0
        for prodotto in self.inventario:
            if prodotto!= "":
                n = i+1

                print( str(n) + ")", prodotto, ", qt=", self.inventario[prodotto])

    def BootStrap():
        print()
        print("Operazioni su [Prodotto]:" )
        print("--------------------------------")
        print(" 1 - Stampa la lista dei prodotti")
        print(" 2 - Inserisci una quantità ad un prodotto")
        print(" 3 - Rimuovo quantità ad un prodotto")
        print(" 0 - Esci dal programma!")
        print("--------------------------------")


# AVVIO PROGRAMMA!!!
while True:
    P = Prodotto
    P.BootStrap()
    input_command_number = int(input("Cosa desideri fare? (inserisci il numero dell'operazione): "))
    print()
    if input_command_number > 0:
        match input_command_number:
            case 0: exit(0)
            case 1: P.lista_prodotti(self=P)
            case 2: 
                numero_prodotto_in_lista = str(input("Nome del prodotto?")) 
                nome_prodotto = P.inventario[numero_prodotto_in_lista]
                print(nome_prodotto)
                P.aggiungi_scorta(nome_prodotto)
            case 3: P.rimuovi_scorta()
            case _: exit()


