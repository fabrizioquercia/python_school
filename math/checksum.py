# Calcolo Checksum
import os, time, math, sys

# Variabili
default_sender = 10000101
default_receiver = default_sender
bit_send = ""
bit_receive = ""
bit_send_reverse = ""
bit_receive_reverse = ""

sleep_time_bootstrap = 0.05
sleep_time = 3 # in secondi


# Funzioni
def bootstrap():
    time.sleep( sleep_time_bootstrap )
    print("--------------------------------------------------------")
    time.sleep( sleep_time_bootstrap )
    print("#####   \033[91m  CALCOLO E CONTROLLO CHECKSUM (8 bit)  \033[0m   ##### ")
    time.sleep( sleep_time_bootstrap )
    print("--------------------------------------------------------")
    
def pulisciOutput():
    osCleanScreen = "cls" if os.name=="nt" else "clear"
    os.system( osCleanScreen )

def loadingMessage(): # demo, pè solo una fighetteria estetica
    print("Caricamento dell'interfaccia in corso. Attendere", end="", flush=True)
    for i in range(5):
        if i == 4:
            time.sleep(1)
            print(".", end="\r", flush=True)    
        else:
            time.sleep(1)
            print(".", end="", flush=True)
        
def pythonVersion():
    v = sys.version
    l = len(v)
    r = ""
    for i in range(1, l+10): r += "-"
    print("\033[90m")
    print(r)
    print(" Python %s"%(v))
    print(" " + str(sys.version_info) + "")
    print(r)
    print("\033[0m")

def messageProbabileErrore():
    print()
    print("\033[33m:: ATTENZIONE :: \033[90mIl mittente ed il ricevente sono diversi, probabile errore di Checksum.\033[0m")
    print()


##### AVVIO #####
pulisciOutput()
bootstrap()


# chiedo il sender
print()
loadingMessage() 
time.sleep(1)

# Chiedo il mittente
print("Inserisci il numero a 8 bit del mittente  (premi invio per il default = %d): " %(default_sender), end="", flush=True)
bit_send = input()

# Chiedo il ricevente
print("Inserisci il numero a 8 bit del ricevente (premi invio per il default = %d): " %(default_receiver), end="", flush=True)
bit_receive = input()

# Do un avviso dimostrativo se il mittente e ricevende sono diversi, per un probabile errore di checksum
if bit_send != bit_receive: messageProbabileErrore()

# Se l'utente preme invio (non inserisce nulla) allora uso i valori di default, e non avrò probabilmetne alcun errore
if bit_receive=="" or bit_receive == "s": bit_receive = default_receiver
if bit_send=="" or bit_send == "s": bit_send = default_sender
    

    


print()
print()

print("Mittente: %s - Ricevente: %s"%(bit_send, bit_receive))

print()


print()
pythonVersion()
print()