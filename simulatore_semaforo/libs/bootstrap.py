import os
import time

osCls = ""
if os.name=="nt":
    osCls = "cls"
else:
    osCls = "clear"
    
strMsg = "Attenzione: Il semaforo si accendera' fra secondi: %s..."

def bootstrapSemaforo(versione):
    os.system( osCls )
    
    time.sleep(0.25)
    print()
    print(strMsg %("3"), end="\r", flush=True)
    time.sleep(1)
    print(strMsg %("2"), end="\r", flush=True)
    time.sleep(1)
    print(strMsg %("1"), end="\r", flush=True)
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


