class Persona:
    
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.__privato = "Ciao"

    def ottieni_privato(self):
        return self.__privato

    def vedi_persona(self):
        return(f"Nome= {self.nome}, Cognome= {self.cognome}, Eta= {self.eta}")

class Studente(Persona):
    
    def __init__(self, nome, cognome, eta, classe, scuola):
        super().__init__(nome, cognome, eta)
        self.classe = classe
        self.scuola = scuola
        privato = self.ottieni_privato()
        print("PRIvato: ", privato)

    def stampa_studente(self):
        print(f"Nome= {self.nome}, Cognome= {self.cognome}, Eta= {self.eta}, Classe= {self.classe}, Scuola= {self.scuola}")

class Operaio(Persona):
    def __init__(self, nome, cognome, eta, ruolo, matricola):
        super().__init__(nome, cognome, eta)
        self.ruolo = ruolo
        self.matricola = matricola

    def stampa_operaio(self):
        print(f"Nome= {self.nome}, Cognome= {self.cognome}, Eta= {self.eta}, Matricola= {self.matricola}, Ruolo= {self.ruolo}")
  

s1 = Studente("Fabrizio", "Quercia", 45, "4SIA", "ITT")
s1.stampa_studente()
print(s1.vedi_persona())

operaio1 = Operaio("Antonio", "Ottaviani", 49,"Supervisore", "ANT001")
operaio1.stampa_operaio()
operaio2 = Operaio("Marco", "antonini", 33, "RUTTER", "RRRR")
operaio2.stampa_operaio()
