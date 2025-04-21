import time
import os

class Prodotto():

    inventario = {1: {"Prodotto 1 (Pizza)" : 0},
                2: {"Prodotto 2 (Carne)": 0},
                3: {"Prodotto 3 (Pesce)": 0},
                4: {"Prodotto 4 (Pasta)": 0},
                5: {"Prodotto 5 (Frutta)": 0},
            }
    
    inventario_virtuale = {}


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


    def s_nome_prodotto(nome:str, ln:int, sx:bool=False):
        len_nome = len(nome)
        s_nome = nome
        if len_nome < ln:
            n_spazi = (ln-len_nome)
            s_spazi = " " * (n_spazi-2)
            if sx==False:
                s_nome = s_nome + s_spazi
            else:
                s_nome = s_spazi + s_nome
        return s_nome


    def lista_prodotti(self):
        print(" :: Lista Prodotti [INVENTARIO] ::")
        print("------------------------------------------------------")
        print("|   N | Nome del Prodotto                      | Qta |")
        print("------------------------------------------------------")
        for key, value in self.inventario.items():
            sid = self.s_nome_prodotto(str(key), 6, True)
            for chiave,valore in value.items():
                snome = self.s_nome_prodotto(str(chiave), 40)
                sqt = self.s_nome_prodotto(str(valore), 5, True)
                print("|" + sid + " |", snome , "|", sqt, "|")
        print("------------------------------------------------------")
        '''cnt = len(self.inventario_virtuale)
        if cnt > 0:
            self.lista_prodotti_virtuali(self)
        '''

    def lista_prodotti_virtuali(self):
        print(" :: Lista Prodotti Virtuali (non sono salvati) ::")
        print("------------------------------------------------------")
        print("|   N | Nome del Prodotto                      | Qta |")
        print("------------------------------------------------------")
        for key, value in self.inventario_virtuale.items():
            sid = self.s_nome_prodotto(str(key), 6, True)
            for chiave,valore in value.items():
                snome = self.s_nome_prodotto(str(chiave), 40)
                sqt = self.s_nome_prodotto(str(valore), 5, True)
                print("|" + sid + " |", snome , "|", sqt, "|")
        print("--------------------------------------------")


    def BootStrap(self):
        dictat = {1:"Stampa la lista dei prodotti", 
                2: "Inserisci una quantità ad un prodotto", 
                3: "Rimuovo quantità ad un prodotto", 
                4: "Aggiungi un nuovo prodotto virtuale", 
                0: "Esci dal programma!"}
        print()
        print("Operazioni sui Prodotti:" )
        print("------------------------------------------")
        for key,value in dictat.items(): print(" " , key , "-" , value)
        print("------------------------------------------")



# AVVIO PROGRAMMA!!!
os.system("cls" if os.name=="nt" else "clear")

def RUN():
    esci = False
    while esci==False:
        P = Prodotto
        P.BootStrap(self=P)
        print()
        input_command_number = int(input("Cosa desideri fare? (inserisci il numero dell'operazione): "))
        print()
        
        
        if input_command_number > 0:
            match input_command_number:
                case 0:
                    esci = True
                    exit(0)
                    break
                case 1:
                    P.lista_prodotti(self=P)
                case 2:
                    numero_prodotto_in_lista = str(input("Nome del prodotto?")) 
                    nome_prodotto = P.inventario[numero_prodotto_in_lista]
                    print(nome_prodotto)
                    P.aggiungi_scorta(nome_prodotto)
                case 3:
                    P.rimuovi_scorta()
                case 4:
                    pass
                case _:
                    esci = True
                    exit()
                    break
        if esci==True:
            break


RUN()
