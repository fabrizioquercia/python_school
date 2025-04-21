class Nodo:   
    def __init__(self, dato):        
        self.dato = dato
        self.prossimo = None

class ListaLinkata:    
    def __init__(self):
        self.testa = None
        
    def aggiungi_inizio(self, dato):
        nuovo_nodo = Nodo(dato) 
        # Il nuovo nodo punta alla testa
        nuovo_nodo.prossimo = self.testa
        # La testa ora è il nuovo nodo
        self.testa = nuovo_nodo
    
    def aggiungi_fine(self, dato):
        nuovo_nodo = Nodo(dato)
        if not self.testa:
            # Se la lista è vuota, il nuovo nodo è la testa
            self.testa = nuovo_nodo
            return None
        nodo_corrente = self.testa
        while nodo_corrente.prossimo:  # Scorre fino all'ultimo nodo
            nodo_corrente = nodo_corrente.prossimo
        # Aggiungi il nuovo nodo alla fine
        nodo_corrente.prossimo = nuovo_nodo
    
    def rimuovi(self, dato):
        nodo_corrente = self.testa
         # Se la testa è il nodo da rimuovere
        if nodo_corrente and nodo_corrente.dato == dato: 
            self.testa = nodo_corrente.prossimo
            return None
        while nodo_corrente and nodo_corrente.prossimo:
            # Se il nodo successivo è quello da rimuovere
            if nodo_corrente.prossimo.dato == dato: 
                nodo_corrente.prossimo = nodo_corrente.prossimo.prossimo
                return None
            nodo_corrente = nodo_corrente.prossimo

    def stampa_lista(self):
        nodo_corrente = self.testa
        while nodo_corrente:
            print(nodo_corrente.dato, end=" -> ")
            nodo_corrente = nodo_corrente.prossimo
        # Fine lista
        print("None")
        
    def trova(self, dato):
        nodo_corrente = self.testa
        while nodo_corrente:
            if nodo_corrente.dato == dato:
            # Restituisce il nodo se trovato
                return nodo_corrente
            nodo_corrente = nodo_corrente.prossimo
       # Nodo non trovato
        return None


# Creiamo una lista linkata
lista = ListaLinkata()

# Aggiungiamo dei nodi alla lista
lista.aggiungi_fine(10)
lista.aggiungi_fine(20)
lista.aggiungi_fine(30)

print("Lista dopo aggiunta alla fine:")
lista.stampa_lista()  # Uscita: 10 -> 20 -> 30 -> None

# Aggiungiamo un nodo all'inizio
lista.aggiungi_inizio(5)

# Stampiamo la lista
print("\nLista dopo aggiunta all'inizio:")
lista.stampa_lista()  # Uscita: 5 -> 10 -> 20 -> 30 -> None

# Stampiamo la lista dopo la rimozione
lista.rimuovi(20)
print("\nLista dopo la rimozione del nodo con dato 20:")
# Uscita: 5 -> 10 -> 30 -> None
lista.stampa_lista()
