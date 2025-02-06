class ContoBancario():
    def __init__(self, codice_conto, importo_iniziale):
        self.codice_conto = codice_conto
        self.importo_iniziale = importo_iniziale if importo_iniziale > 0 else 0

    def __verifica_prelievo(self, importo_richiesto):
        if self.importo_iniziale >= importo_richiesto:
            return True
        return False
    
    def deposita(self, importo):
        if importo > 0:
            self.importo_iniziale += importo
            return self.importo_iniziale
        return 0
    
    def preleva(self, importo):
        if self.__verifica_prelievo(importo):
            self.importo_iniziale -= importo
            return self.importo_iniziale
        return 0
    
    def saldo(self):
        return self.importo_iniziale


def main():
    codice_conto = input("Inserisci il tuo codice conto: ")
    importo_iniziale = input("Inserisci il tuo saldo iniziale (deve essere maggiore di 0): ")
    if importo_iniziale=="":
        importo_iniziale = 100
        print("Dovevi inserire un importo iniziale maggiore di 0, per default ho aggiunto io 100!") 
    
    print("--------------------------------")
    Conto = ContoBancario(codice_conto, importo_iniziale)
    print(f"Conto: {codice_conto}, Importo iniziale: {importo_iniziale}")
    saldo = Conto.saldo()
    print("--------------------------------")

    print()
    print("--------------------------------")
    deposita = int(input(f"Quanto vuoi depositare? (saldo attuale: {saldo}) "))
    if deposita > 0:
        print(f"Saldo attuale: {saldo}")
        prelievo = Conto.deposita(deposita)
        print(f"Richiesta di deposito: {deposita}")
        print(f"Saldo dopo prelievo: {saldo+deposita}")
    else:
        print(f"Spiacenti, non puoi depositare importi minori di 1 euro (zero non ammesso)")
    print("--------------------------------")

    print()
    print("--------------------------------")
    preleva = int(input(f"Quanto prelevi? (max: {saldo}) "))
    if preleva > 0:
        print(f"Saldo attuale: {saldo}")
        prelievo = Conto.preleva(preleva)
        print(f"Richiesta di prelievo: {preleva}")
        print(f"Saldo dopo prelievo: {saldo-preleva}")
    else:
        print(f"Spiacenti, non puoi prelevare importi minori di 1 euro (zero non ammesso)")




if __name__ == "__main__":
    main()