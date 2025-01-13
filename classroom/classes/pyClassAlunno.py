import sqlite3 as DB

class Alunno():

    def __init__(self):
        self.fileCSV = "./data/alunni.csv"
        self.ConnectionDB = "./data/Classroom.db"

    def creaNuovo(self, nomeAlunno, cognomeAlunno, matricolaAlunno, emailAlunno):
        if self.esisteAlunnoSuDB(nomeAlunno, cognomeAlunno, matricolaAlunno) == False:
            self.salvaSuFileCSV(nomeAlunno, cognomeAlunno, matricolaAlunno, emailAlunno)
            print(" == Alunno %s %s (mat: %s) creato correttamente ==" % (nomeAlunno, cognomeAlunno, matricolaAlunno))
            lastid = self.salvaSuDB(nomeAlunno, cognomeAlunno, matricolaAlunno, emailAlunno)
            print(" == [%d]: Inserito su DB %s !" %(lastid, self.ConnectionDB))
        else:
            print(" >> L'alunno esiste già, pertanto verra scartato! << ")

    def salvaSuDB(self, nomeAlunno, cognomeAlunno, matricolaAlunno, emailAlunno):
        sql = "INSERT INTO alunno (nome, cognome, matricola, email) "
        sql += "VALUES ('" + nomeAlunno + "','" + cognomeAlunno + "', '" + matricolaAlunno + "', '" + emailAlunno + "') "
        with DB.connect(self.ConnectionDB) as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            return cursor.lastrowid

    def salvaSuFileCSV(self, nomeAlunno, cognomeAlunno, matricolaAlunno,emailAlunno):
        f = open(self.fileCSV, "a")
        f.write(nomeAlunno + ";" + cognomeAlunno + ";" + matricolaAlunno + ";" + emailAlunno + "\n")
        f.close()

    def esisteAlunno(self, nomeAlunno, cognomeAlunno, matricola):
        nome = nomeAlunno+";"+cognomeAlunno+";"+matricola
        f = open(self.fileCSV, "r")
        for data in f.readlines():
            dato = data.replace("\n", "")
            if dato is not None and dato == nome:
                f.close()
                return True
        f.close()
        return False
    
    def esisteAlunnoSuDB(self, nome, cognome, matricola):
        sql = "SELECT * FROM alunno WHERE nome = '" + nome +"' AND cognome = '" + cognome +"' AND matricola = '" + matricola +"' "
        with DB.connect(self.ConnectionDB) as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            if cursor.rowcount > 0: return True
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
        matricola = input("Matricola: ")
        email = input("E-mail: ")
        if email == "":  email = nome + "." + cognome + "@ittterni.org"
        if nome.strip() != "" and cognome.strip() != "" and matricola.strip() != "" and email.strip() != "":
            self.creaNuovo(nome, cognome, matricola, email)

    def askCreaAlunni(self):
        quanti_alunni = int(input("Quanti alunni vuoi inserire?: "))
        incremento = 0
        while True:
            if incremento >= quanti_alunni: break
            if quanti_alunni > 0 and incremento < quanti_alunni:
                sNomeAlunno = str(input("[Alunno %d di %d]> Nome: " % (incremento + 1, quanti_alunni)))
                sCognomeAlunno = str(input("[Alunno %d di %d]> Cognome: " % (incremento + 1, quanti_alunni)))
                sMatricolaAlunno = str(input("[Alunno %d di %d]> Matricola: " % (incremento + 1, quanti_alunni)))
                sEmailAlunno = str(input("[Alunno %d di %d]> E-Mail: " % (incremento + 1, quanti_alunni)))
                if sEmailAlunno.strip() == "":  sEmailAlunno = sNomeAlunno + "." + sCognomeAlunno + "@ittterni.org"
                self.creaNuovo(sNomeAlunno, sCognomeAlunno, sMatricolaAlunno, emailAlunno="")
                incremento = incremento + 1
            else:
                break

    def BootStrap(self):
        print()
        print("Operazioni su [%s]:" % (self.__class__.__name__) )
        print("--------------------------------")
        print(" 1 - Inserisci un nuovo alunno")
        print(" 2 - Inserisci una serie di alunni")
        print(" 3 - Chiedi la stampa della lista degli alunni")
        print("--------------------------------")



