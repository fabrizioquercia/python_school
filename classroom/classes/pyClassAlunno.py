class Alunno(object):

    def __init__(clsAlunno):
        clsAlunno.nome = ""
        clsAlunno.cognome = ""
        clsAlunno.fileCSV = "data/alunni.csv"

    def creaNuovo(clsAlunno, nomeAlunno, cognomeAlunno):
        if clsAlunno.esisteAlunno(nomeAlunno, cognomeAlunno) == False:
            clsAlunno.scriviFile(nomeAlunno, cognomeAlunno)
            print(" == Alunno %s %s creato correttamente ==" % (nomeAlunno, cognomeAlunno))
        else:
            print(" >> L'alunno esiste già, pertanto verra scartato! << ")

    def scriviFile(clsAlunno, nomeAlunno, cognomeAlunno):
        f = open(clsAlunno.fileCSV, "a")
        f.write(nomeAlunno + ";" + cognomeAlunno + "\n")
        f.close()

    def esisteAlunno(clsAlunno, nomeAlunno, cognomeAlunno):
        nome = nomeAlunno+";"+cognomeAlunno
        f = open(clsAlunno.fileCSV, "r")
        for data in f.readlines():
            dato = data.replace("\n", "")
            if dato is not None and dato == nome:
                f.close()
                return True
        f.close()
        return False

    def elencoAlunni(clsAlunno):
        f = open(clsAlunno.fileCSV, "r")
        for data in f.readlines():
            print(data.replace(";", " "), end="")
        f.close()

    def askElencoAlunni(clsAlunno):
        stampa_lista = str(input("Vuoi stampare la lista di tutti gli alunni? (premi 'S' se vuoi stampare, qualsiasi tasto per annullare): "))
        if stampa_lista == "S" or stampa_lista == "s": clsAlunno.elencoAlunni()

    def askCreaAlunno(clsAlunno):
        nome = input("Nome: ")
        cognome = input("Cognome: ")
        if nome.strip() != "" and cognome.strip() != "":
            clsAlunno.creaNuovo(nome, cognome)

    def askCreaAlunni(clsAlunno):
        quanti_alunni = int(input("Quanti alunni vioi inserire?: "))
        incremento = 0
        while True:
            if incremento >= quanti_alunni: break
            if quanti_alunni > 0 and incremento < quanti_alunni:
                sNomeAlunno = str(input("[Alunno %d di %d]> Nome: " % (incremento + 1, quanti_alunni)))
                sCognomeAlunno = str(input("[Alunno %d di %d]> Cognome: " % (incremento + 1, quanti_alunni)))
                clsAlunno.creaNuovo(sNomeAlunno, sCognomeAlunno)
                incremento = incremento + 1

    def BootStrap(self):
        print()
        print("Operazioni:")
        print("--------------------------------")
        print(" 1 - Inserisci un nuovo alunno")
        print(" 2 - Inserisci una serie di alunni")
        print(" 3 - Chiedi la stampa della lista degli alunni")
        print("--------------------------------")



