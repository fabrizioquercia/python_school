numeri = []
nRange = int( input("Quanti numeri vuoi inseire?: ") )
somma = 0
media = 0
massimo = 0
for x in range(nRange):
    numero = int( input( "Inserisci il %d° numero di %d: "%(x+1, nRange) ) )
    numeri.append( numero )
    somma += numero
    media += numero / nRange
    if numero > massimo: massimo = numero
print("Elenco dei numeri inseriti: " + str(numeri))
print("Somma dei numeri inseriti: %d"%(somma))
print("Media calcolata: %f" %( float( somma / nRange ) ))
print("Media estesa: " + str(media))
print("Massimo: %d" %(massimo))

a = input("premi un tasto per uscire: ")
if a:
    exit(0)