import os
import time


def bootstrap():
    time.sleep(0.1)
    print("-------------------------------------------")
    time.sleep(0.1)
    print("#####   \33[42m SOMMA E MEDIA DI n NUMERI \033[0m   ##### ")
    time.sleep(0.1)
    print("-------------------------------------------")


##### AVVIO #####
os.system("cls" if os.name=="nt" else "clear" )
bootstrap()
print()

# Chiedo quanti numeri vuole inserire
numeri = []
nRange = int( input("Quanti numeri vuoi inseire?: ") )
print()

# Variabili di calcolo
somma = 0
media = 0
massimo = 0

for x in range(nRange):
    numero = int( input( "Inserisci il %d° numero di %d: "%(x+1, nRange) ) )
    numeri.append( numero )
    somma += numero
    media += numero / nRange
    if numero > massimo: massimo = numero
print()
print("--------------------------------------------")
print("Elenco dei numeri inseriti:\n" + str(numeri))
print()
print("Somma dei numeri inseriti: %d"%(somma))
print()
print("Media calcolata: %f" %( float( somma / nRange ) ))
print("Media estesa: " + str(media))
print()
print("Massimo: %d" %(massimo))
print("--------------------------------------------")
print()
a = input("Premi un tasto qualsiasi per uscire: ")
if a:
    exit(0)