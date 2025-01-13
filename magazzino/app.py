import os
import Prodotto as  from magazzino

while True:
    P = Prodotto
    
    input_command_number = int(input("Cosa desideri fare? (inserisci il numero dell'operazione): "))
    print()
    if input_command_number > 0:
        match input_command_number:
            case 0: exit(0)
            #case 1: Al.askCreaAlunno()
            
            case _: exit()


