# Simula apertura e chiusura di una sbarra o cancello

import time
import libs.cancelloRuntime as cancelloRuntime

codiceUtente=0
codiceInterno=150 # Il codice di apertura del cancello
tentativiSistema=3 # tentativi concessi
tentativi=0


while tentativi < tentativiSistema:
    codiceUtente = int(input("Inserisci il codice di apertura (Tentativo %d di %d): " %( (tentativi+1), tentativiSistema) ))
    if codiceUtente == codiceInterno:
        cancelloRuntime.apri()
        break
    else:
        print("Spiacente: Il codice inserito non è valido. Riprova!")
        tentativi += 1
    pass




# se non ho finito i tentativi... allora avvio il programma
print("Proseguo..")
print("Proseguo..")
print("Proseguo..")

