#funzioni interne per def testo()
def media():
    lista = [39, 22, 12,3,5]
    somma = 0
    for i in lista:
        somma += i
    media = somma / len(lista)
    stringa = "La media fra i numeri " + str(lista) + " e' " + str(media) + " - La somma e': " + str(somma)
    return str(stringa)

def fattoriale():
    # Calcolo il fattoriale col ciclo for
    numero = 7
    fattorialeFor = 1
    for i in range(1, numero+1):
        fattorialeFor *= i
    stringa = "Il fattoriale del numero " + str(numero) + " ( " + str(numero) +"! ) e': " + str(fattorialeFor)
    return stringa
    
def potenza():
    numero = 147
    potenza = numero **2
    stringa = "Il numero " + str(numero) + " elevato a potenza e' " + str(potenza)
    return stringa