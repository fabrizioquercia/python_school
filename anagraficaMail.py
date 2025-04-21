class Anagrafica():
    def __init__(self, nome, cognome, email=None, registrato=False):
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.registrato = registrato

    def registra(self, email):
        self.registra=True

    def is_registrato(self):
        if self.registrato == True:
            return "SI"
        return "NO"
    def get_email(self):
        if self.email != None:
            return self.email
        return " - nessuna - "
    
    def imposta_mail(self, email):
        self.email = email
        self.registrato = True

    def stampa_anagrafica(self):
        return f"Nome;{self.nome}, Cognome: {self.cognome}, Email: {self.get_email()}, Registrato: { self.is_registrato() }"
    
    def visita_sito(self, sito):
        if self.registrato==True:
            return f"Benvenuto sul sito: {sito}"
        return f"Spiacente {self.nome}, purtroppo non sei registrato e non hai accesso al sito desiderato!"

class Studente(Anagrafica):
    def __init__(self, nome, cognome, email=None, registrato=False):
        super().__init__(nome, cognome, email, registrato)
        self.matricola = ""
    
    def imposta_matricola(self, matricola):
        self.matricola = matricola
        print(f" >> inserita matricola {self.matricola} allo studente {self.nome} {self.cognome}")

    def stampa_anagrafica(self):
        return super().stampa_anagrafica() + "Matricola:"+self.matricola


class Dipendente(Anagrafica):
    def __init__(self, nome, cognome, email=None, registrato=False, stipendio_base=0):
        super().__init__(nome, cognome, email, registrato)
        self.stipendio_base = stipendio_base
        self.livello = 1
    def aumenta_livello(self, livello):
        self.livello = livello

    def __aumenta_stipendio_10(self):
        self.stipendio_base = (self.stipendio_base*(10 * self.livello))/100
        

def main():
    sito = "https://www.google.it/"
    anag = Anagrafica("Mario", "Rossi")
    print(anag.stampa_anagrafica())
    print(anag.visita_sito(sito))
    print()
    anag.imposta_mail("pippo@cj.com")
    print(anag.stampa_anagrafica())
    print(anag.visita_sito(sito))
    print()


if __name__ == "__main__":
    main()


def parse_mail(email:str):
    try:
        if email.strip() == "": return "Email mancante!"
        if (email.find("@") == -1): return "Email non valida. Manca la chiocciola!"

        email = email.strip()
        #pos_chiocciola = email.index("@")
        txt_user = email.split("@")
        txt_domain = email.rsplit("@")
        if str(txt_domain).find(".") == -1: return "Manca il dominio, ad esempio .com!"
        return "OK Mail ce piace!"
    except:
        return "Email non valida!"
    
