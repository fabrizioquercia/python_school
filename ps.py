from datetime import datetime,timedelta

class Paziente:
	def __init__(self, nome, codice,ora):
		self.nome = nome
		self.codice = codice
		self.tempo_arrivo = ora


	def __str__(self):
		return f"{self.nome} (Codice: {self.codice}) è arrivato alle {self.tempo_arrivo} del {self.tempo_arrivo}."

class Pila:
    def __init__(self):
        self.lista=[]


    def registrazione(self, nome, codice,ora):
        nuovo = Paziente(nome, codice,ora)

        # Trova la posizione giusta per inserirlo in base alla priorità
        i = 0
        while i < len(self.lista) and self.lista[i].codice <= codice:
            i += 1
            self.lista.insert(i, nuovo)

        print(f"Paziente {nome} registrato con codice {codice}.")


    def tratta_paziente(self):
        if not self.lista:
            print("Nessun paziente in attesa.")
            return
        paziente = self.lista.pop(0)
        print(f"Trattato: {paziente}")

    def visualizza_pazienti(self):
        if not self.lista:
            print("Nessun paziente in attesa.")
        else:
            ("Pazienti in attesa:")
        for p in self.lista:
            print(f"- {p}")


    def gestione_tempo(self):
        orario_corrente = datetime.now()
        for p in self.lista:
            # Converti la stringa tempo_arrivo in oggetto datetime
            tempo_arrivo = datetime.strptime(p.tempo_arrivo, "%H:%M")

            # Ricrea datetime completo (solo ora:minuti di oggi)
            tempo_arrivo = orario_corrente.replace(hour=tempo_arrivo.hour, minute=tempo_arrivo.minute, second=0, microsecond=0)

            # Se sono passati più di 60 minuti
            if orario_corrente - tempo_arrivo > timedelta(minutes=60):
                p.codice += 1  # oppure: p.codice = int(p.codice) + 1, se è una stringa

    def chiave_ordinamento(self, paziente):
        return (paziente.codice, paziente.tempo_arrivo)

paziente1=Paziente("Giulio",2, datetime.now())
print(paziente1)

pila = Pila()
pila.visualizza_pazienti()

paziente2=Paziente("Marco",1, datetime.now())
print(paziente2)
