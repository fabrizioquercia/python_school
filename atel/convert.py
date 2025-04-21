#creo una lista dei file da ciclare
lista_files = [
    "terni reti gennaio.csv",
    "terni reti febbraio.csv",
    "terni reti marzo.csv"
]

def fomatta_valore(valore, lunghezza):
    val = str(valore)
    lenv = len(str(valore))
    delta = lunghezza-lenv
    if delta > 0:
        valore = str(val)
        for i in range(delta):
            val += str(" ")
    return val

def formatta_orario(secondi):
    ore = int(secondi / 3600)
    minuti = int((secondi % 3600) / 60)
    sec = int(secondi % 60)
    tempo_formattato = f"{ore:02}:{minuti:02}:{sec:02}"
    return tempo_formattato

#intestazione tabella
tabella  = "\n----------------------------------------------------"
tabella += "\n| Nome File                   | Ore      | Secondi |"
tabella += "\n----------------------------------------------------"

for f in lista_files:
    tot_secondi_globale = 0
    file = open(f, "r")
    file.seek(0)
    r = 1
    
    for linea in file:
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
    
    file.close()

    nome_file = fomatta_valore(f, 28)
    totale_sec = fomatta_valore(tot_secondi_globale, 7)
    totale_orario = formatta_orario(tot_secondi_globale)

    #scrivo (aggiungo) la riga sulla tabella
    tabella += f"\n| {nome_file}| {totale_orario} | {totale_sec} |"

#Fine tabella, riga finale
tabella += "\n----------------------------------------------------"

print(tabella)
