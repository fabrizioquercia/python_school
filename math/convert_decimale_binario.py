#####################################################################
###  Convertitore da numero decimale a binario (157 -> 10011101)  ###
#####################################################################
#
# Versione: 1.0
# Rilascio: 18 ott 2023
#
#####################################################################

# Importo le librerie di sistema 
import os
import time

# Importo le mie librerie specifiche per questo progetto
import libs.convertDecimaleBinario as Converter
import libs.convertDecimaleBinarioVariabili as Variabili

Converter.pulisciOutput(os)
Converter.bootstrap(time)

# Chiedo all'utente un numero decimane maggiore di 0 da convertire in binario
# Lo chiedo N volte finchè non inserisce un numero intero valido
input_numero = Converter.inputGetNumero()

if input_numero > 0:
    quoziente = input_numero
    numero_binario = ""
    while int(quoziente) > 0:
        resto = int( quoziente % 2 )
        quoziente = quoziente / 2
        numero_binario = str(resto) + numero_binario

    print("Numero: %s => binario: %s"%(input_numero, numero_binario)  )
    


