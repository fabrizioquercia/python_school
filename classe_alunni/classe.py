# file

import os
import time
import math


os.system("cls" if os.name=="nt" else "clear")

# Variabili di sistema (configurazione e percorsi cartelle)
path_app = os.getcwd() + "\\classe_alunni"
path_data = path_app + "\\data"
file_data_materie = path_data + "\\materie.txt"
file_data_alunni = path_data + "\\" + "alunni.txt"

## Variabili applicazione
lista_materie = []
lista_alunni = []


### FUNZIONI ###

## Apro il file che contiene l'elenco delle materie
## è un file di testo materie.txt presente nella cartella /data/materie.txt
def caricaListaMaterie():
    global lista_materie 
    file_materie = open(file_data_materie, "r")
    lista_materie = [ m.replace("\n", "").title()  for m in file_materie ]
    file_materie.close()
    

def caricaListaAlunni():
    global lista_alunni 
    file_alunni = open(file_data_alunni, "r")
    lista_alunni = [ a.replace("\n", "").title()  for a in file_alunni ]
    file_alunni.close()
    print(lista_alunni)
    

def aggiungiMateria(materia):
    global lista_materie
    file_m = open(file_data_materie, "r")
    lista_m = [ m for m in file_m ]
    if materia in lista_m:
        print("La materia %s è già presente in lista."%(materia))
    else:
        lista_materie.append(materia)
        print(lista_materie)
        scriviSuFile(file_data_materie, materia)
        print("Aggiunta la materia %s"%(materia))
        

## Scrivo su file
def scriviSuFile(fl, testo):
    try:
        f = open(fl, "a")
        f.write(testo+"\n")
        f.close()
    except:
        print("Impossibile scrivere sul file %s: "%(fl))
            




caricaListaMaterie()


aggiungiMateria("informatica")


print()
print()
print()