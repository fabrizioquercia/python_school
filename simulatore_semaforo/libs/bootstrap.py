import os
import time

osCls = ""
if os.name=="nt":
    osCls = "cls"
else:
    osCls = "clear"

def bootstrapSemaforo(versione):
    os.system( osCls )
    
    time.sleep(0.25)
    print()
    print("Attenzione: Il semaforo si accendera' fra 3 secondi ...", end="\r", flush=True)
    time.sleep(1)
    print("Attenzione: Il semaforo si accendera' fra 2 secondi ...", end="\r", flush=True)
    time.sleep(1)
    print("Attenzione: Il semaforo si accendera' fra 1 secondo ...", end="\r", flush=True)
    time.sleep(1)
    
    os.system( osCls )
    print()
    
    time.sleep(0.1)
    print("---------------------------------------------------")
    time.sleep(0.1)
    print("#####   \33[45m SIMULATORE SEMAFORO (versione " + str(versione) + ") \033[0m   ##### ")
    time.sleep(0.1)
    print("---------------------------------------------------")
    time.sleep(0.3)
#### fine funzione [def bootstrapSemaforo()]