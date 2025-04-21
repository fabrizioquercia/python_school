# File da elaborare
nome_file = "terni reti febbraio.csv"

def formatta_orario(secondi):
    ore = int(secondi / 3600)
    minuti = int((secondi % 3600) / 60)
    sec = int(secondi % 60)
    tempo_formattato = f"{ore:02}:{minuti:02}:{sec:02}"
    return tempo_formattato

tot_secondi_riga = 0
tot_secondi_globale = 0
file = open( nome_file , "r")
file.seek(0)
r = 1
for linea in file:
    #print("riga",r,": ", end="")
    r+=1
    tot_secondi_riga = 0
    riga = linea.split(";")
    array_orario = riga[4].split(":")
    ore = array_orario[0]
    minuti = array_orario[1]
    secondi = array_orario[2]

    if int(ore) > 0:
        tot_secondi_riga = tot_secondi_riga + (int(ore)*60)
    if int(minuti) > 0:
        tot_secondi_riga = tot_secondi_riga + (int(minuti)*60)
    if int(secondi) > 0:
        tot_secondi_riga = tot_secondi_riga + int(secondi)
    

    tot_secondi_globale += tot_secondi_riga
    #print("tot_secondi_riga", tot_secondi_riga)
file.close()

print()
print("---------------------------------------")
print("Nome del File: ",nome_file)
print("Totale secondi:", tot_secondi_globale)
print("Totale orario: ", formatta_orario(tot_secondi_globale) )
print("---------------------------------------")
