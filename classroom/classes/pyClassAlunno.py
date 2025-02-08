import sqlite3 as DB
from . import  utils as Utils

class Alunno():

    def __init__(self):
        datapath = "./data/"
        self.fileCSV = datapath + "alunni.csv"
        self.fileLOG = datapath + "logs.csv"
        self.ConnectionDB = datapath + "Classroom.db"

    def creaNuovo(self, nomeAlunno, cognomeAlunno, matricolaAlunno, emailAlunno):
        if self.esisteAlunnoSuDB(nomeAlunno, cognomeAlunno, matricolaAlunno) == False:
            self.salvaSuFileCSV(nomeAlunno, cognomeAlunno, matricolaAlunno, emailAlunno)
            s_log = " == Alunno %s %s (mat: %s) creato correttamente ==" % (nomeAlunno, cognomeAlunno, matricolaAlunno)
            self.add_log_csv(Utils.stringa_log_csv("INSERT--CSV", s_log))
            print(s_log)
            lastid = self.salvaSuDB(nomeAlunno, cognomeAlunno, matricolaAlunno, emailAlunno)
            s_log = " == [%d]: Inserito su DB %s !" %(lastid, self.ConnectionDB)
            self.add_log_csv(Utils.stringa_log_csv("INSERT---DB", s_log))
            print(s_log)
        else:
            print(" >> L'alunno esiste già, pertanto verra scartato! << ")

    def salvaSuDB(self, nomeAlunno, cognomeAlunno, matricolaAlunno, emailAlunno):
        sql = "INSERT INTO alunno (nome, cognome, matricola, email) "
        sql += "VALUES ('" + nomeAlunno + "','" + cognomeAlunno + "', '" + matricolaAlunno + "', '" + emailAlunno + "') "
        self.add_log_csv(Utils.stringa_log_csv("INSERT--SQL", sql))
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
        self.add_log_csv(Utils.stringa_log_csv("SELECT--CSV", "Richiesta lista alunni da file CSV"))
        f = open(self.fileCSV, "r+")
        for data in f.readlines():
            print(data.replace(";", " "), end="")
        f.close()

    def elencoAlunniDB(self):
        self.add_log_csv(Utils.stringa_log_csv("SELECT---DB", "Richiesta lista alunni da file CSV"))
        sql = "SELECT id, cognome,nome,matricola,email FROM alunno ORDER BY cognome, nome "
        with DB.connect(self.ConnectionDB) as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()

        print()
        print("Database: " + self.ConnectionDB )
        print("Tabella:  alunno")
        print("Record:   " + str(len(rows)) )

        if len(rows) > 0:
            print("-------------------------------------------------------------")
            print("ID   Nome                Matricola   E-Mail                  ")
            print("-------------------------------------------------------------")
            for row in rows:
                id = Utils.fstring(row[0], 5)
                nome = Utils.fstring(row[1] + " " +row[2], 20)
                matricola = Utils.fstring(row[3], 12)
                email = Utils.fstring(row[4], 25)
                print(f"{id} {nome} {matricola} {email}")
            print("-------------------------------------------------------------")
        print()
        conn.close()

    def askElencoAlunni(self):
        stampa_lista = str(input("Vuoi stampare la lista di tutti gli alunni? (premi 'S' se vuoi stampare, qualsiasi tasto per annullare): "))
        if stampa_lista == "S" or stampa_lista == "s": self.elencoAlunniDB()

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
        print()
        print(" 1 - Inserisci un nuovo alunno")
        print(" 2 - Inserisci una serie di alunni")
        print(" 3 - Chiedi la stampa della lista degli alunni")
        print(" 4 - Stampa i logs di sistema")
        print(" 0 - --- Esci dal programma ---")
        print("--------------------------------")
        print()

    def add_log_csv(self, log):
        f = open(self.fileLOG, "a")
        f.write(log + "\n")
        f.close()

    def show_logs(self):
        f = open(self.fileLOG, "r")
        for data in f.readlines():
            print(data)
        f.close()

