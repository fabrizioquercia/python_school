# Variabili globali per i calcoli matematici e di input


# Variabili per le stringhe di testo in output per il comando print();
strInputUtenteNumero = "Inserisci il numero decimale maggiore di 0 che desideri convertire in binario:"
strInputUtenteNumeroErrore = "Numero inserito non valido: Inserisci un numero maggiore di zero:"

# Funzioni


# Funzione di inizio script che chiede input() all'utente
def bootstrap(time):
    time.sleep(0.1)
    print("----------------------------------------------------")
    time.sleep(0.1)
    print("#####   \33[5;30;43m CONVERTITORE da DECIMALE a BINARIO \033[0m   ##### ")
    time.sleep(0.1)
    print("----------------------------------------------------")
    
def pulisciOutput(os):
    osCleanScreen = "cls" if os.name=="nt" else "clear"
    os.system( osCleanScreen )
    


def inputGetNumero():
    input_valido = False
    input_errori = 0
    
    while input_valido == False:
        msg = strInputUtenteNumero if input_errori == 0 else strInputUtenteNumeroErrore
        numero_input = input( msg  + " " )
        if numero_input.isnumeric():
            numero_input = int(numero_input)
            if numero_input > 0:
                global numero
                numero = numero_input
                input_valido = True
                break
            else:
                input_valido = False
                input_errori = 1
        else:
            input_valido = False
            input_errori = 1
    
    return input_valido


def __test():
	fn = __test.__name__
	return "fn:" + str(fn) + "() => Hello World!"
	