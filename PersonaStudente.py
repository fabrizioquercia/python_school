class Persona:
    
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def vedi_persona(self):
        return(f"Nome= {self.nome}, Cognome= {self.cognome}, Eta= {self.eta}")

class Studente(Persona):
    
    def __init__(self, nome, cognome, eta, classe, scuola):
        super().__init__(nome, cognome, eta)
        self.classe = classe
        self.scuola = scuola

    def vedi_studente(self):
        print(f"Nome= {self.nome}, Cognome= {self.cognome}, Eta= {self.eta}, Classe= {self.classe}, Scuola= {self.scuola}")


s1 = Studente("Fabrizio", "Quercia", 45, "4SIA", "ITT")
s1.vedi_studente()
print(s1.vedi_persona())