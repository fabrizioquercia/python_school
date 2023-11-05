import libs.bootstrap as Bootstrap
import libs.semaforoRuntime as SemaforoRuntime

# variabili di configurazione e conteggio di sistema
mezzanotteDopoCicli = 3
mainCounter = 0

##### MESSAGGE DI ATTESA #####
Bootstrap.bootstrapSemaforo(3)

##### AVVIA LA PROCEDURA #####
print()
while True:
    
    if mainCounter == mezzanotteDopoCicli:
        mainCounter = 0
        SemaforoRuntime.lampeggiaMezzanotte()
    else:
        #print()
        SemaforoRuntime.lampeggia(mainCounter, mezzanotteDopoCicli)
        mainCounter = mainCounter+1

# end while True
    
##### FINE PROCEDURA #####
