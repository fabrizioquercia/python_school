import libs.bootstrap as bootstrap
import libs.semaforoRuntime as semaforoRuntime

# variabili di configurazione e conteggio di sistema
mezzanotteDopoCicli = 3
mainCounter = 0

##### MESSAGGE DI ATTESA #####
bootstrap.bootstrapSemaforo(3)

##### AVVIA LA PROCEDURA #####
print()
while True:
    
    if mainCounter == mezzanotteDopoCicli:
        mainCounter = 0
        semaforoRuntime.lampeggiaMezzanotte()
    else:
        #print()
        semaforoRuntime.lampeggia(mainCounter, mezzanotteDopoCicli)
        mainCounter = mainCounter+1

# end while True
    
##### FINE PROCEDURA #####
