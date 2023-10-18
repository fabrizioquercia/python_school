import time

# variabili di durata e colori di output semaforo V-G-R
statoSemaforo = [0, 1, 2] ## verde,giallo,rosso => es: v=0, g=1, r=2
durataSemaforo = [3, 2, 5]  ## verde,giallo,rosso => es: v=3secondi, g=2secondi, r=5secondi
statoCodice = ["V", "G", "R"]
statoColore = ["\33[42m", "\33[43m", "\33[101m"]
resetColore = "\033[0m"


# Lampeggi alla mezzanotte
def lampeggiaMezzanotte():
    
    conta=0
    contaInterno=0
    limite=20
    timeSleep = 0.5
    
    print("")
    print("")
    print("[ 00.00.00 ] == STAND-BY MODE: ON (E' mezzanotte, Lampeggio in arancione ogni " + str(timeSleep) + " secondi.")
    print("")

    while conta < limite:
        
        if conta%2 == 0:
            print(" \33[43m" + "\33[30m" + " S " + "\033[0m", end="\r", flush=True)
            contaInterno = contaInterno+1
        else:
            print (" \33[90m" + " S " + "\033[0m" , end="\r", flush=True)
        
        conta = conta+1
        time.sleep(timeSleep)
        
    print("")
    print("")
    print("[ 00.05.30 ] == STAND-BY MODE: OFF (Semaforo operativo fino alla prossima mezzanotte)")
    print("")
    
# fine def lampeggiaMezzanotte()
    

# Lampeggia normalmente (verde, giallo, rosso)
def lampeggia(mainCounter, mezzanotteDopoCicli):
    i = 0
    contatore = 1
    
    #print("", end="\r", flush=True)
    
    #print("MainCounter: " + str(mainCounter) )
    while i < len(statoSemaforo):
        
        ##print("I=" + str(i) + " - len(statoSemaforo)=" + str(len(statoSemaforo)) + " - contatore=" + str(contatore) )
        
        # prendo i dati del vettore posizionale su iterator i
        s_StatoCodice = statoCodice[i]
        
        if s_StatoCodice == "R":
            s_ProssimoStato = statoCodice[0]
        else:
            s_ProssimoStato = statoCodice[i+1]
        
        # stampo il colore corrente
        if mainCounter == (mezzanotteDopoCicli-1) and s_StatoCodice == "R":
            print(" " + statoColore[i] + " " + statoCodice[i] + " " + resetColore + " (E' quasi mezzanotte: Entro on modalità STAND-BY fra " + str(durataSemaforo[i]) + " secondi)", end="\r", flush=True )
        else:
            print(" " + statoColore[i] + " " + statoCodice[i] + " " + resetColore + " (diventa " + s_ProssimoStato + " fra " + str(durataSemaforo[i]) + " secondi)", end="\r", flush=True )
        
        # attendo i suoi secondi per cmbiare al prossimo stato
        time.sleep( durataSemaforo[i] )
        #print("", end="\r", flush=True)
        # metto  il rosso a solo rosso senza testo
        print(" " + statoColore[2] + " " + statoCodice[2] + "\033[0m", end="\r", flush=True )

        
        # incremento il contatore
        i = i+1
        
        # incremento il contatore generale del ciclo
        if i == (mezzanotteDopoCicli-1):
            contatore = 1
        else:
            contatore += 1

    #print()
    
#### fine funzione [def lampeggia()]
