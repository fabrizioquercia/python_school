#Lezione oggi FRAZIONE

import os
os.system("cls")


numeratore = float( input("Inserisci il numeratore della frazione: ") )
denominatore = 0

while denominatore == 0:
    denominatore = float( input("Inserisci il denominatore della frazione (diverso da 0): ") )

print("Il valore della frazione è %f  \nProgramma terminato!"%(numeratore/denominatore))




