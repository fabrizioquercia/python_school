# Classe Persona

class Persona:
    
    cognome =""
    nome=""
    
    def __init__(self):
        self.cognome=""
        self.nome=""

    def setCognome(self, sCognome):
        self.cognome = sCognome
        
    def getCognome(self):
        return self.cognome
    
    def setNome(self, sNome):
        self.nome = sNome
        
    def getNome(self):
        return self.nome
    
    def toString(self):
        return self.nome + " "  + self.cognome
    


persona = Persona();
persona.setCognome( input("Inserisci il cognome: ") )
persona.setNome( input("Inserisci il nome: ") )


#print("Hai creato " + str( persona.getCognome() ) + " " + str( persona.getNome() ) )
#print("Nominativo: " + persona.toString() )
print("Hai inserito il nominativo %s %s" %(persona.getNome(), persona.getCognome()) )