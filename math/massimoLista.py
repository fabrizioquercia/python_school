# Massimo di una lista
lista = [1,71,14,66]
massimo = 0
for numero in lista:
    if numero > massimo: massimo = numero
print("Lista: %s\nMax:   %d"%(lista, massimo))