from magazzino import  Prodotto

while True:
    P = Prodotto
    
    input_command_number = int(input("Cosa desideri fare? (inserisci il numero dell'operazione): "))
    print()
    if input_command_number > 0:
        match input_command_number:
            case 0: exit(0)
            case 1: P.lista_prodotti()
            
            case _: exit()


