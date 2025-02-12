class ContoBancario():
    def __init__(self, codice_conto, importo_iniziale):
        self.codice_conto = codice_conto
        self.importo_iniziale = 1000 if importo_iniziale <= 0 else importo_iniziale 

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


