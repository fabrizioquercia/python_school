class Alunno(object):

    def __init__(self):
        self.fileCSV = "data/alunni.csv"

    def creaNuovo(self, nomeAlunno, cognomeAlunno):
        if self.esisteAlunno(nomeAlunno, cognomeAlunno) == False:
            self.salvaSuFileCSV(nomeAlunno, cognomeAlunno)
            print(" == Alunno %s %s creato correttamente ==" % (nomeAlunno, cognomeAlunno))
        else:
            print(" >> L'alunno esiste già, pertanto verra scartato! << ")

    def salvaSuFileCSV(self, nomeAlunno, cognomeAlunno):
        f = open(self.fileCSV, "a")
        f.write(nomeAlunno + ";" + cognomeAlunno + "\n")
        f.close()

    def esisteAlunno(self, nomeAlunno, cognomeAlunno):
        nome = nomeAlunno+";"+cognomeAlunno
        f = open(self.fileCSV, "r")
        for data in f.readlines():
            dato = data.replace("\n", "")
            if dato is not None and dato == nome:
                f.close()
                return True
        f.close()
        return False

    def elencoAlunni(self):
        f = open(self.fileCSV, "r")
        for data in f.readlines():
            print(data.replace(";", " "), end="")
        f.close()

    def askElencoAlunni(self):
        stampa_lista = str(input("Vuoi stampare la lista di tutti gli alunni? (premi 'S' se vuoi stampare, qualsiasi tasto per annullare): "))
        if stampa_lista == "S" or stampa_lista == "s": self.elencoAlunni()

    def askCreaAlunno(self):
        nome = input("Nome: ")
        cognome = input("Cognome: ")
        if nome.strip() != "" and cognome.strip() != "":
            self.creaNuovo(nome, cognome)

    def askCreaAlunni(self):
        quanti_alunni = int(input("Quanti alunni vioi inserire?: "))
        incremento = 0
        while True:
            if incremento >= quanti_alunni: break
            if quanti_alunni > 0 and incremento < quanti_alunni:
                sNomeAlunno = str(input("[Alunno %d di %d]> Nome: " % (incremento + 1, quanti_alunni)))
                sCognomeAlunno = str(input("[Alunno %d di %d]> Cognome: " % (incremento + 1, quanti_alunni)))
                self.creaNuovo(sNomeAlunno, sCognomeAlunno)
                incremento = incremento + 1
            else:
                break

    def BootStrap(self):
        print()
        print("Operazioni su [%s]:" % (Alunno.__name__) )
        print("--------------------------------")
        print(" 1 - Inserisci un nuovo alunno")
        print(" 2 - Inserisci una serie di alunni")
        print(" 3 - Chiedi la stampa della lista degli alunni")
        print("--------------------------------")



