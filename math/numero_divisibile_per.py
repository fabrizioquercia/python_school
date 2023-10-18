import time
import os

# Variabili globali per i conteggi delle operazioni matematiche
divisore = 7
minus = 7 # oppure minus = divisore, ma meglio di no per adesso
multiplo = divisore
multipli = []
limite_multipli = 10000
errori = 0

# Variabili usate nelle stringhe di messaggi nel comando print()
strMsgInputUtente = "Inserisci il numero che vuoi sapere se è divisibile per " + str(divisore) + ":"
strMsgInputUtenteErrori = "Inserisci un numero intero valido (5, 7, 14, 147..), non lettere:"
strRigaDivisoria = "--------------------------------------------------------------" #---------------------------
strColoreVerde = "\33[92m"
strColoreRosso = "\33[91m"
strColoreReset = "\033[0m"
strFnModulo7 = "fn:moduloN(n)  -> "
strFnMinus7 = "fn:minusN(n)   -> "
strFnPythonMod = "python:mod(%" + str(divisore) + ") -> "
strNumeroOk = "Il numero inserito è divisibile per "
strNumeroKo = "Il numero inserito NON è divisibile per "
strSalutiFinaliOk = "Bene: abbiamo risolto il problema della divisibilità!\nBye Bye!"
strSalutiFinaliKo = "Accidenti: non abbiamo risolto il problema...\nAlla prossima!"


# ***** FUNZIONI :: INIZIO *****#
def moduloN(numero):
    
    # Verifico col modulo, solo ai fini di debug
    #print ( "[ DEBUG: def modulo7(n) ] Numero:" + str(numero) + ", modulo7:" + str((numero%7)) )
    
    # Operazione passo passo
    #divisore = 7
    #divisione = int(numero / divisore)
    #prodotto_divisione = divisione * divisore
    #return numero - prodotto_divisione
   
    # Operazione semplificando il codice su una sola riga
    return numero - ( int(numero / divisore) * divisore  )
# fine def modulo7(numero)

def minusN(numero):
    #minus = 7
    numero = abs(numero)
    
    while numero > minus:
        numero = numero-minus
    
    if numero == 0 or numero == minus:
        return True
    else:
        return False
# fine def minus7(numero)

def bootstrap():
    time.sleep(0.1)
    print("-------------------------------------------------")
    time.sleep(0.1)
    print("#####   \33[42m CALCOLO NUMERO DIVISIBILE PER " + str(divisore) + " \033[0m   ##### ")
    time.sleep(0.1)
    print("-------------------------------------------------")

def calcolaMultipli():
    print("Sto calcolando tutti i multipli di " + str(divisore)+" fino a " + str(limite_multipli), end="", flush=True )
    s=1
    i=1;
    while s<=5:
        print(".", end="", flush=True)
        time.sleep(0.5)
        s+=1
    # fine di: while s==5:
    
    while i <= limite_multipli:
        global multiplo
        multiplo += 7
        multipli.append(multiplo)
        i += 1
    # fine di: while i <= limite_multipli:
# fine def calcolaMultipli()

def pulisciOutput():
    osCleanScreen = "cls" if os.name=="nt" else "clear"
    os.system( osCleanScreen )

def stampaMultipliPrimaDiMe(numero):
    i = 0
    while i < len(multipli):
        multiplo = multipli[i]
        if multiplo <= numero:
            if i==0:
                print(str(multiplo), end="", flush=True)
            else:
                print(", " + str(multiplo), end="", flush=True)
            i += 1
        else:
            break
# ***** FUNZIONI :: FINE *****#


# *****************************#
#      AVVIO DEL PROGRAMMA     #
# *****************************#
pulisciOutput()
calcolaMultipli()
pulisciOutput()
bootstrap()
print()

# Chiedo il numero all'utente
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
            break;
        else:
            input_valido = False
            input_errori = 1
    else:
        input_errori = 1

print()
print(strRigaDivisoria)


# Uso il modulo7(n) (metodo della divisibilità per 7)
is_divisibile = moduloN(numero)
if is_divisibile == 0:
    print(strColoreVerde + strFnModulo7 + strColoreReset + strNumeroOk + str(divisore) )
else:
    errori += 1
    print(strColoreRosso + strFnModulo7 + strColoreReset + strNumeroKo + str(divisore) )
print( strRigaDivisoria )

# Uso il minusN(n) (metodo della sottrazione)
is_divisibile_con_minus = minusN(numero)
if is_divisibile_con_minus == True:
    print(strColoreVerde + strFnMinus7 + strColoreReset + strNumeroOk + str(divisore) )
else:
    errori += 1
    print(strColoreRosso + strFnMinus7 + strColoreReset + strNumeroKo + str(divisore) )
print( strRigaDivisoria )

if numero%divisore == 0:
    print(strColoreVerde + strFnPythonMod + strColoreReset + strNumeroOk + str(divisore) )
else:
    errori += 1
    print(strColoreRosso + strFnPythonMod + strColoreReset +  strNumeroKo + str(divisore) )

print( strRigaDivisoria )
print()
print()


# Chiedo se vuole stampare l'elenco dei multipli compresi fra 0 e numero utente
if numero in multipli:
    print("Il numero che hai inserito è presente anche nella lista dei multipli di " + str(divisore) + " che ho generato all'inizio." )
    chiedi_stampa_multipli = input("Vuoi vedere a video la lista di tutti i multipli trovati più bassi di me? (S per si, N per no) ")
    if chiedi_stampa_multipli=="S"  or chiedi_stampa_multipli=="s"  :
        print()
        time.sleep(0.5)
        print("Elenco dei multipli di " + str(divisore) + " fino al numero che hai inserito: ", flush=True)
        print( strRigaDivisoria )
        stampaMultipliPrimaDiMe(numero)
        print()
        #print()


# Passo ai saluti finali
if errori > 0:
    print(strSalutiFinaliKo)
else:
    print()
    print()
    print(strSalutiFinaliOk)
