from click import pause
from time import  sleep
from Strumenti import  *

sleep_value = 3

def main():
    # batteria
    print()
    print("Batteria... vai!")
    batteria = Batteria("Yamaha F11", "Pelle di Daino, Acero", 11)
    print("Batteria:", batteria.nome)
    print("Materiale:", batteria.get_descrizione())
    print(batteria.sbatti_tamburi())
    sleep(sleep_value)

    # Chitarra
    print()
    print("Chitarra... accordati!")
    chitarra = Chitarra("Fender Stratocaster Classic Vibe 60's", "Tastiera in Palissandro, Corpo in Acero", 6)
    print("Chitarra:", chitarra.nome)
    print("Materiale:", chitarra.get_descrizione())
    print(chitarra.accordare())
    print("Ottimo chitarra: Tiette pronta!")
    sleep(sleep_value)

    # piano
    print()
    print("Piano: inizia. Piano!")
    piano = Pianoforte("Yamaha Gold Gran Concert", "Legno massello", 88)
    print("Pianoforte:", piano.nome)
    print("Materiale:", piano.get_descrizione())
    print(piano.suona_accompagnamento())
    print("... che meraviglia !!!")
    sleep(sleep_value)

    # violino
    print()
    print(".. e adesso.. la magia del violino!!!")
    violino = Violino("Violin Dolce", "Ciliegio, corpo in noce",4)
    print("Violino:", violino.nome)
    print("Materiale:", violino.get_descrizione())
    print(violino.pizzica_violino())
    print(".. che armonia... che leggerezza... assoluta!")

    print()
    pause("PROGRAMMA COMPLETATO:: Stiaccia un qualsiasi tasto per andare a casa...")
