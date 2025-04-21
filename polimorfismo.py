#Polimorfismo
class Veicolo():
    def __init__(self, velocita_masssima, km_percorsi):
        self.velocita_masssima = velocita_masssima
        self.km_percorsi = km_percorsi

    def fai_strada(self, velocita, tempo):
        if velocita < self.velocita_masssima and tempo > 0:
            self.km_percorsi += (velocita*tempo)
            return f"KM Percorsi aggiornati; {self.km_percorsi}!"
        return f"Non è stato possibile aggiornre i percorsi, tempo non valido {tempo} o velocità maggiore della velocità massima!"

class Autobus(Veicolo):
    def __init__(self, velocita_masssima, km_percorsi, num_posti_massimi, num_persone_attuali):
        if velocita_masssima > 100: velocita_masssima = 100
        super().__init__(velocita_masssima, km_percorsi)
        self.num_posti_massimi = num_posti_massimi
        self.num_persone_attuali = 0

    def fermata(self, quanti_salgono, quanti_scendono):
        if quanti_salgono == 0 and quanti_scendono == 0:
            return f"Non è salito e sceso nessuno!"
        self.num_persone_attuali = self.num_persone_attuali-quanti_scendono+quanti_salgono
        return f"Sono salite {quanti_salgono} persone, scese {quanti_scendono}, passeggeri totali attuali: {self.num_persone_attuali}"

    def dal_gommista(self):
        return f"Hai speso: {60*4} euro!"

class Moto(Veicolo):
    def __init__(self, velocita_masssima, km_percorsi, tipo_moto):
        super().__init__(velocita_masssima, km_percorsi)
        self.tipo_moto = tipo_moto

    def dal_gommista(self):
        return f"Per le gomme della moto hai speso: {40*2} euro!"

def main():

    v = Veicolo(120, 5)
    print(v.velocita_masssima)
    print(v.fai_strada(20,10))

    print()
    bus = Autobus(1555, 20, 24, 10)
    print(f"Persone attuali sul bus: {bus.num_persone_attuali}")
    print(bus.fermata(0, 0))
    print(f"Persone attuali sul bus dopo sali_e_scendi_1: {bus.num_persone_attuali}")

    print()
    print(bus.fermata(10, 4))
    print(f"Persone attuali sul bus dopo sali_e_scendi_2: {bus.num_persone_attuali}")

    print()
    print(bus.fermata(25, 28))
    print(f"Persone attuali sul bus dopo sali_e_scendi_3: {bus.num_persone_attuali}")

    print()
    print(bus.fermata(15, 2))
    print(f"Persone attuali sul bus dopo sali_e_scendi_4: {bus.num_persone_attuali}")

    print()
    print("AUTOBUS... con tutto questo sali e scendi.. mi si sono sgonfiate le gomme.\nQuasiquasi vado dal gommista va...")
    print( bus.dal_gommista() )
    print("AMMAZZA quant'è caro! Sto autobus me costa un occhio.. quasiquasi mi compro la moto...")

    print()
    moto = Moto(205,100,"Enduro")
    print(moto.dal_gommista())
    print()
    print("...Fortuna che me costava de meno la moto ....")

# Langio il tutto!
if __name__ == "__main__": main()