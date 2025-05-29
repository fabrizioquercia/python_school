"""ESERCIZIO: In questo esercizio, dovrai implementare un sistema di gestione
delle emergenze ospedaliere utilizzando una pila con priorità. Il sistema dovrà essere
in grado di gestire i pazienti che arrivano al pronto soccorso in base alla gravità
della loro condizione e all’ordine di arrivo.
Ogni paziente ha un nome, una priorità medica e il tempo di arrivo.
I pazienti con condizioni più gravi devono essere trattati prima, mentre quelli con
stessa priorità vengono trattati in ordine di arrivo (FIFO per le stesse priorità).
Classificazione delle priorità:
• Codice Rosso (1): Emergenza critica, trattamento immediato.
• Codice Giallo (2): Urgenza alta, richiede attenzione rapida.
• Codice Verde (3): Caso moderato, può aspettare.
• Codice Bianco (4): Non urgente, trattamento opzionale.
Funzionalità richieste:
• Registrazione di un nuovo paziente, Inserimento nella coda in base alla priorità .
- Trattamento di un paziente, rimuovendolo dalla pila .
• Visualizzazione della lista di pazienti in attesa
"""
from datetime import datetime

class Paziente:
    def __init__(self, nome, codice,ora):
        self.nome = nome
        self.codice = codice
        self.tempo_arrivo = ora   

    def __str__(self):
        return f"{self.nome} (Codice: {self.codice}) è arrivato alle {self.tempo_arrivo}."

class Pila:
    def __init__(self):
        self.lista=[]

    def registrazione(self, nome, codice, ora):
        nuovo=Paziente(nome, codice, ora)
        if not self.lista:
            self.lista.append(nuovo)    #se la lista è vuota aggiunto direttamnete
        else:
            inserito=False
            i = 0  # Inizializzo un contatore
            for paziente in self.lista:
                if paziente.codice > codice:    #faccio il confronto tra i codici
                    self.lista.insert(i, nuovo) #inserisce mantiene priorità
                    inserito = True
                    break
                i += 1  # Incrementiamo il contatore ad ogni iterazione
            if not inserito:    #nuovo paziente ha una priorità inferiore o uguale a tutti i pazienti presenti nella lista.
                self.lista.append(nuovo)    #quindi aggiungo alla fine per priorità più bassa
        print(f"Paziente {nome} registrato con codice {codice} alle {nuovo.tempo_arrivo}.")


    def tratta_paziente(self):
        if not self.lista:
            print("Nessun paziente in attesa.")
            return
        paziente = self.lista.pop(0)    #toglie il primo
        print(f"Trattato: {paziente}")

    def visualizza_pazienti(self):
        if not self.lista:
            print("Nessun paziente in attesa.")
        else:
            print("Pazienti in attesa:")
            for p in self.lista:
                print(f"- {p}")

sala_attesa=Pila()
sala_attesa.registrazione("Giulio",2,"21:00")
sala_attesa.registrazione("Maria",1,"21:10")
sala_attesa.registrazione("Franco",4,"21:30")
sala_attesa.registrazione("Anna",2,"21:25")
sala_attesa.registrazione("Pina",3,"21:20")
sala_attesa.registrazione("Carla",4,"21:17")
sala_attesa.visualizza_pazienti()
sala_attesa.tratta_paziente()
sala_attesa.visualizza_pazienti()
