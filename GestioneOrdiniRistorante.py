# Nodo base
class Nodo:                                # Nodo per la lista collegata, usato sia per la coda che per la pila
    def __init__(self, valore):            # Inizializza il nodo con un valore e un puntatore al nodo successivo
        self.valore = valore
        self.prossimo = None

# Coda FIFO con lista collegata
class CodaOrdini:                          # Coda per gli ordini, usata per la preparazione delle pizze
    def __init__(self):
        self.testa = None
        self.coda = None

    def aggiungi_ordine(self, nome):       # Aggiungi un nuovo ordine alla coda
        nuovo = Nodo(nome)
        if self.coda is None:              # Se la coda è vuota aggiungi il primo nodo 
            self.testa = self.coda = nuovo # Inizializza testa e coda
        else:
            self.coda.prossimo = nuovo     # Collega il nuovo nodo alla coda
            self.coda = nuovo

    def prossimo_ordine(self):             # Prepara il prossimo ordine dalla coda
        if self.testa is None:
            return None
        nome = self.testa.valore           # Salva il valore del nodo corrente
        self.testa = self.testa.prossimo   # Sposta la testa al nodo successivo
        if self.testa is None:             # Se la coda è vuota, resetta anche la coda
            self.coda = None
        return nome                        # Restituisce il nome dell'ordine preparato

    def mostra_ordini(self):               # Mostra tutti gli ordini nella coda
        corrente = self.testa              # Inizializza il nodo corrente alla testa della coda
        if not corrente:
            print("Nessun ordine in coda.")
        while corrente:                    # Itera fino alla fine della coda
            print(corrente.valore)
            corrente = corrente.prossimo 

# Pila LIFO con lista collegata
class PilaUrgenti:
    def __init__(self):
        self.top = None                     # Corrisponde alla cima della pila

    def aggiungi_urgente(self, nome):       # Aggiungi un nuovo ordine urgente alla pila
        nuovo = Nodo(nome)                  # Crea un nuovo nodo con il nome dell'ordine
        nuovo.prossimo = self.top           # Collega il nuovo nodo alla cima della pila
        self.top = nuovo

    def prepara_urgente(self):              # Prepara l'ordine urgente dalla cima della pila
        if self.top is None:
            return None
        nome = self.top.valore              # Salva il valore del nodo corrente
        self.top = self.top.prossimo        # Sposta la cima della pila al nodo successivo
        return nome

    def mostra_urgenti(self):               # Mostra tutti gli ordini urgenti nella pila
        corrente = self.top
        if not corrente:
            print("Nessun ordine urgente.")
        while corrente:
            print(corrente.valore)
            corrente = corrente.prossimo

# MAIN: test del programma
if __name__ == "__main__":
    coda = CodaOrdini()
    coda.aggiungi_ordine("Pizza Margherita")
    coda.aggiungi_ordine("Pasta al Pesto")
    coda.aggiungi_ordine("Pasta al Pomodoro")
    coda.aggiungi_ordine("Fonduta di Formaggio")
    coda.aggiungi_ordine("Pizza Capricciosa")

    urgenti = PilaUrgenti()
    urgenti.aggiungi_urgente("Pasta in Bianco")
    urgenti.aggiungi_urgente("Pizza Baby")

    print("Ordini normali:")
    coda.mostra_ordini()

    print("\nOrdini urgenti:")
    urgenti.mostra_urgenti()

    print("\nPreparazione urgente:")
    print(urgenti.prepara_urgente())

    print("\nProssimo ordine normale:")
    print(coda.prossimo_ordine())



