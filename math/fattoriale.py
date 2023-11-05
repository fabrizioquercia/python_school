# Fattoriale di un numeri, con ciclo For, While e funzione ricorsiva

import math
import os
import time


# Pulisco lo schermo
os.system( "cls" if os.name=="nt" else "clear"  )

# Funzione ricorsiva per il fattoriale
def fattoriale(n):
    if n == 0:
        return 1
    else:
        return n*fattoriale(n-1)
    
def tabellaRisultato(mathF, fattorialeFor, fattorialeWhile, fattorialeRicorsiva ):
    print("-----------------------------------------------------------------------")
    print(" \33[95mFUNZIONE o CICLO\033[0m | \33[95mRISULTATO\033[0m               ")
    print("-----------------------------------------------------------------------")
    print(" math.factorial() | " + splitText(str(mathF)) )
    print("-----------------------------------------------------------------------")
    print(" for              | " + splitText(str(fattorialeFor) ) )
    print("-----------------------------------------------------------------------")
    print(" while            | " + splitText(str(fattorialeWhile) ) )
    print("-----------------------------------------------------------------------")
    print(" fattoriale()     | " + splitText(str(fattorialeRicorsiva) ) )
    print("-----------------------------------------------------------------------")

def bootstrap():
    time.sleep(0.1)
    print("---------------------------------------------")
    time.sleep(0.1)
    print("#####   \33[95m  CALCOLO NUMERO FATTORIALE  \033[0m   ##### ")
    time.sleep(0.1)
    print("---------------------------------------------")

def splitText(testo, lenght=50):
    sTesto = str(testo)
    cicli = 0
    i = cicli
    text = ""
    start = 0
    stop = lenght
    if len(str(sTesto)) > lenght:
        cicli = math.ceil(len(str(sTesto)) / lenght)
        while i < math.ceil(cicli):
            if i == 0:
                start = i
                stop = lenght
                text += sTesto[start:stop]
            else:
                start = lenght*i
                stop = (lenght*i) + lenght
                text += "\n                  | " + sTesto[start:stop]
            i += 1
    else:
        text = sTesto
    return text


##### AVVIO PROGRAMNA #####
bootstrap()
print()

# Chiedo il numero all'utente
strMsgInputUtente = "Inserisci il numero per il quale vuoi sapere il fattoriale:"
strMsgInputUtenteErrori = "Inserisci un numero intero valido (5, 7, 14, 147..), non lettere:"
input_valido = False
input_errori = 0
while input_valido == False:
    msg = strMsgInputUtente if input_errori == 0 else strMsgInputUtenteErrori
    numero = input(msg + " ")
    if numero.isnumeric():
        #print( type(numero) )
        numero = int(numero)
        if numero > 0:
            input_valido = True
            break
        else:
            input_valido = False
            input_errori = 1
    else:
        input_errori = 1


# Ho un impur valido, procedo al calcolo del fattoriale
if input_valido:
    
    
    # Calcolo il fattoriale con la funzione math di Python (fnuzione di controllo)
    mathF = math.factorial(numero)
    
    # Calcolo il fattoriale col ciclo for
    fattorialeFor = 1
    for i in range(1, numero+1):
        fattorialeFor *= i
    
    # Calcolo il fattoriale col ciclo while
    fattorialeWhile = 1
    x = 1
    while x <= numero:
        fattorialeWhile *= x
        x += 1
    
    # Calcolo con la ricorsiva
    fattorialeRicorsiva = fattoriale(numero)
    
    
    # Stampo la tabella del risultato
    print()
    tabellaRisultato(mathF, fattorialeFor, fattorialeWhile, fattorialeRicorsiva)
    print()
    
    
