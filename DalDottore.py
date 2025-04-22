import datetime, os, time

###### FUNZIONI UTLLI
# funzione che ottiene l'oario e lo ritorna (fatta stand-alone)
def get_orario():
    orario = datetime.datetime.now()
    ora=orario.strftime("%H:%M:%S")
    data=orario.strftime("%D")
    return (data + " " + ora)
# funzione che ottiene il numero di priorità (1,2,3,4) in base al ccolore
# se codice_colore=ROSSO torna 1, GIALLO torna 2, VERDE torna 3, BIANCO torna 4 
def get_codice_priorita(codice_colore):
    codice = 0
    codice_colore = str(codice_colore).upper()
    match codice_colore:
        case "ROSSO":   codice = 1
        case "GIALLO":  codice = 2
        case "VERDE":   codice = 3
        case "BIANCO":  codice = 4
    return codice
# è l'opposto di quella sopra: se codice_colore=1 torna ROSSO, 2 = GIALLO, 3=VERDE, 4=BIANCO
def get_codice_colore(codice_colore):
    codice = 0
    match codice_colore:
        case 1:  codice = "ROSSO"
        case 2:  codice = "GIALLO"
        case 3:  codice = "VERDE"
        case 4:  codice = "BIANCO"
    return codice


# CLASSE DEL PAZIENTE (Il nodo)
class Paziente:
    def __init__(self, nome, codice):
        self.nome = nome
        self.codice = get_codice_priorita(codice)
        self.orario = get_orario()
        
# CLASSE DELLA LISTA AL P.S.
class ProntoSoccorso:
    def __init__(self):
        self.lista = []

    def aggiungi_paziente(self, paziente):
        paziente.orario = get_orario()
        self.lista.append(paziente)
        self.lista.sort(key=lambda p: (p.codice, p.orario))
        print(f"Inserito il paziente {paziente.nome} con codice {get_codice_colore(paziente.codice)}: {paziente.orario}")

    def chiama_paziente(self):
        self.lista.sort(key=lambda p: (p.codice, p.orario))
        c = get_codice_colore(self.lista[0].codice)
        print("CHIAMATA PER IL SIGNOR: ",self.lista[0].nome, "CODICE", c)
        self.lista.pop(0)

    def stampa_lista_attesa(self):
        i = 0
        print("\nPAZIENTI IN ATTESA:")
        for paziente in self.lista:
            cod = get_codice_colore(paziente.codice)
            c = "7"
            i += 1
            match cod:
                case "ROSSO": c = "41"
                case "GIALLO": c = "43"
                case "VERDE": c = "42"
                case "BIANCO": c = "7"
            str = f"\033[{c}m {i} \033[0m {paziente.nome} - entrato il {paziente.orario}"
            print(str)
            
        print()
        

# ESECUZIONE PROGRAMMA
if __name__ == "__main__":
    sleeptime = 2
    os.system("cls" if os.name=="nt" else "clear" )

    # Creo qualche paziente iniziale di esempio
    pz1 = Paziente("Mario Rossi", "bianco")
    pz2 = Paziente("Giuseppe Verdi", "rosso")
    pz3 = Paziente("Antonio Bianchi", "giallo")
    pz4 = Paziente("Mauro Mauri", "bianco")
    pz5 = Paziente("Bud Spencer", "giallo")
    pz6 = Paziente("Terenz Ill", "rosso")
    pz7 = Paziente("Valentino Rossi", "verde")
    pz8 = Paziente("Fedez", "verde")
    pz9 = Paziente("Elodie", "rosso")

    os.system("cls" if os.name=="nt" else "clear" )


    PS = ProntoSoccorso()
    PS.aggiungi_paziente(pz1)
    time.sleep(sleeptime)
    PS.aggiungi_paziente(pz2)
    time.sleep(sleeptime)
    PS.aggiungi_paziente(pz3)
    time.sleep(sleeptime)
    PS.aggiungi_paziente(pz4)
    time.sleep(sleeptime)
    PS.aggiungi_paziente(pz5)
    time.sleep(sleeptime)
    PS.aggiungi_paziente(pz6)
    time.sleep(sleeptime)
    PS.stampa_lista_attesa()
    time.sleep(sleeptime)
    PS.aggiungi_paziente(pz7)
    time.sleep(sleeptime)


    PS.stampa_lista_attesa()

    
    time.sleep(sleeptime)

    PS.aggiungi_paziente(pz8)
    PS.stampa_lista_attesa()

    time.sleep(sleeptime)
    PS.aggiungi_paziente(pz9)
    time.sleep(sleeptime)
    PS.stampa_lista_attesa()



    PS.chiama_paziente()
    time.sleep(sleeptime)
    PS.stampa_lista_attesa()

    PS.chiama_paziente()
    time.sleep(sleeptime)
    PS.stampa_lista_attesa()

    pz10 = Paziente("Michael Jackson", "giallo")
    pz11 = Paziente("Madonna", "verde")
    pz12 = Paziente("Gerri Scotti", "verde")
    pz13 = Paziente("Paolo Bonolis", "verde")

    pz14 = Paziente("Luca Laurenti", "rosso")
    pz15 = Paziente("Maria De Filippi", "rosso")
    pz16 = Paziente("Morgan", "giallo")

    PS.aggiungi_paziente(pz10)
    PS.stampa_lista_attesa()
    time.sleep(sleeptime)

    PS.aggiungi_paziente(pz11)
    PS.stampa_lista_attesa()
    time.sleep(sleeptime)
    PS.aggiungi_paziente(pz12)
    PS.stampa_lista_attesa()
    time.sleep(sleeptime)
    PS.stampa_lista_attesa()

    # chiama
    PS.chiama_paziente()
    PS.stampa_lista_attesa()
    time.sleep(sleeptime)
    PS.chiama_paziente()
    PS.stampa_lista_attesa()
    time.sleep(sleeptime)

    #aggiungi...
    PS.aggiungi_paziente(pz13)
    time.sleep(sleeptime)
    PS.stampa_lista_attesa()
    PS.aggiungi_paziente(pz14)
    PS.stampa_lista_attesa()
    time.sleep(sleeptime)
    PS.aggiungi_paziente(pz15)
    PS.stampa_lista_attesa()
    time.sleep(sleeptime)
    PS.aggiungi_paziente(pz16)
    PS.stampa_lista_attesa()
    time.sleep(sleeptime)

    PS.chiama_paziente()

    pz17 = Paziente("Vasco Rossi", "rosso")
    time.sleep(sleeptime)
    PS.stampa_lista_attesa()


