from idlelib.replace import replace

prezzo = int(input("Inserisci il prezzo su cui calcolare le percentuali di sconto: "))
prezzo_corrente = prezzo
prezzo_con_tutti_sconti = 0
prezzo_scontato_finale = 0
quanti_sconti = int(input("Quante percentuali di sconto vuoi applicare? "))
somma_percentuali = 0
i = 0
for i in range(quanti_sconti):
    x = i+1
    str = "Inserisci il valore dello sconto n. %s "

    percntuale_sconto = int(input(str))
    calcola_sconto = (prezzo_corrente * percntuale_sconto) /100
    prezzo_corrente -= calcola_sconto
    somma_percentuali += percntuale_sconto
    print("Prezzo di partenza:", prezzo, "- Prezzo CORRENTE:", prezzo_corrente, "- Applica Perc. sconto", percntuale_sconto, "- Importo scontato: ", calcola_sconto, "- Prezzo attuale scontato: ", prezzo_corrente)
