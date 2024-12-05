import os
from classes.pyClassAlunno import Alunno

while True:
    Al = Alunno()
    Al.BootStrap()
    input_command_number = int(input("Cosa desideri fare? (inserisci il numero dell'operazione): "))
    print()
    if input_command_number > 0:
        match input_command_number:
            case 0: exit(0)
            case 1: Al.askCreaAlunno()
            case 2: Al.askCreaAlunni()
            case 3: Al.askElencoAlunni()
            case _: exit()


