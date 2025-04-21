import datetime, os, time

###### FUNZIONI UTLLI

def BootStrap():
    print()
    print(":: BENVENUTO AL PRONTO SOCCORSO ::")
    print("----------------------------------")
    print()
    print(" 1 - Inserisci un nuovo Paziente in ingresso")
    print(" 2 - Chiama Paziente")
    print(" 3 - Stampa lista di attesa")
    print(" 0 - --- Esci dal programma ---")
    print("----------------------------------")
    print()
# funzione che ottiene l'oario e lo ritorna (fatta stand-alone)
def get_orario():
    orario = datetime.datetime.now()
    ora=orario.strftime("%H:%M")
    data=orario.strftime("%D")
    return (data + " " + ora)

# funzione che ottiene il numero di priorità (1,2,3,4) in base al ccolore
# 1 = ROSSO, 2 = GIALLO, 3 = VERDE, 4 = BIANCO
def get_codice_priorita(codice_colore):
    codice = 0
    codice_colore = str(codice_colore).upper()
    match codice_colore:
        case "ROSSO":   codice = 1
        case "GIALLO":  codice = 2
        case "VERDE":   codice = 3
        case "BIANCO":  codice = 4
    return codice

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
        self.lista.append(paziente)
        self.lista.sort(key=lambda p: (p.codice, p.orario))
        print(f"Inserito il paziente {paziente.nome} con codice {get_codice_colore(paziente.codice)}: {paziente.orario}")

    def stampa_lista_attesa(self):
        i = 1
        print("\nPAZIENTI IN ATTESA:")
        print()

        for paziente in self.lista:
            cod = get_codice_colore(paziente.codice)
            s = ""
            c = "\033[7m"
            match cod:
                case "ROSSO": c = "\033[41m"
                case "GIALLO": c = "\033[43m"
                case "VERDE": c = "\033[42m"
                case "BIANCO": c = "\033[7m"
            str = f"{c} {i} \033[0m {paziente.nome} - entrato il {paziente.orario}"
            print(str)
            i = i+1
        
        print()
        

def pulisci_schermo():
    os.system("cls" if os.name=="nt" else "clear" )

# ESECUZIONE PROGRAMMA
if __name__ == "__main__":
    sleeptime = 2
    pulisci_schermo()

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

    pulisci_schermo()


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
    pulisci_schermo()
    PS.aggiungi_paziente(pz8)

    time.sleep(sleeptime)
    PS.aggiungi_paziente(pz9)
    time.sleep(sleeptime)
    PS.stampa_lista_attesa()





