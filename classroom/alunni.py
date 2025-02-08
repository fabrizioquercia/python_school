import os
from classes.pyClassAlunno import Alunno

#Pulisco lo schermo
os.system("cls" if os.name=="nt" else "clear" )

while True:
    Al = Alunno()
    Al.BootStrap()
    input_command_number = int(input("Cosa desideri fare? (inserisci il numero dell'operazione): "))
    print()
    if input_command_number > 0:
        match input_command_number:
            case 1: Al.askCreaAlunno()
            case 2: Al.askCreaAlunni()
            case 3: Al.askElencoAlunni()
            case 4: Al.show_logs()
    else:
        exit(0)
