# Ricevente binario bit di parità
import os
import time

# FUNZIONI
def bootstrap():
    os.system("cls" if os.name=="nt" else "clear" )
    time.sleep(0.1)
    print("------------------------------------------")
    time.sleep(0.1)
    print("#####   \33[41m  CALCOLO BIT DI PARITA'  \033[0m   ##### ")
    time.sleep(0.1)
    print("------------------------------------------")

bootstrap()
print()

# Inizializzo una lista (array) con 5 elementi null
lenx = 5
msg = [None]*lenx

for x in range( lenx ):
    bit = int(input("Inserisci il bit (0,1) alla posizione %s di %s: "%(x+1, lenx)))
    
    while bit < 0 or bit > 1:
        bit = int(input("ERRORE: Inserisci il bit (0,1) alla posizione %s di %s: "%(x+1, lenx)))
    
    msg[x] = bit

print() 
print(msg)
print()