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
numero = ""
print(numero)
input_numero = Converter.inputGetNumero()

if input_numero == True:
    print(numero)
    quoziente = numero
    numero_binario = ""

    while quoziente > 0:
        resto = str( quoziente % 2 )
        quoziente = int( quoziente / 2 )
        numero_binario = resto + numero_binario

    print("Numero: " + str(input_numero) + " => binario: " +str(numero_binario)  )
    


