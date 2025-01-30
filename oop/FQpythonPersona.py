class Persona():

  def __init__(self, nome, eta, sesso):
    self.nome = nome
    self.eta = eta
    self.sesso = sesso
	
  def presentati(self):
    saluto = "Ciao, mi chiamo" + self.nome + " ed ho " + str(self.eta) + " anni"
    return saluto


class Animale():

  def __init__ (self, nome, specie):
    self.nome = nome
    self.specie = specie
    
  def emetti_suono(self):
    match self.specie:
      case "cane": return "Wwwwoooffffff.... wwwooooffffff"
      case "gatto": return "miauuuuuu... prrrr prrrrrr"
      case "scimmia": return "HU-U- HU HU UH!"
      case _: return " ...... :-| Sono un pesce, sò muto!!!!"


class Impiegato():

  def __init__(self, nome, cognome, matricola, stipendio):
    self.nome=nome
    self.cognome=cognome
    self.matricola=matricola
    self.stipendio=stipendio

  def aumenta_stipendio(self, aumento):
    return str(aumento) + "%: " + str(int(self.stipendio + ((self.stipendio*aumento)/100)))
    
# -----------------------------------------
persona = Persona("Marco Rossi", 32, "M")
print()
print("----- PERSONA -----")
print()
print(persona.presentati())
print()

# -----------------------------------------
cane = Animale("Rocky", "cane")
gatto = Animale("Felix", "gatto")
scimmia = Animale("BingoBongo", "scimmia")
pesce = Animale("Nemo", "pesce")
print("----- ANIMALI -----")
print()
print(cane.nome, "(", cane.specie, ")\nDimmi qualcosa.. parla...\n", cane.emetti_suono())
print()
print(gatto.nome, "(", gatto.specie, ")\nDimmi qualcosa.. parla...\n", gatto.emetti_suono())
print()
print(scimmia.nome, "(", scimmia.specie, ")\nDimmi qualcosa.. parla...\n", scimmia.emetti_suono())
print()
print("Accidenti.....")
print()
print(pesce.nome, "(", pesce.specie, ")\nDimmi qualcosa.. parla... almeno tu...\n", pesce.emetti_suono())
print()

# -----------------------------------------
imp1 = Impiegato("Mario", "Rossi", "MT001", 1400)
imp2 = Impiegato("Antonio", "Bianchi", "MT002", 1900)
imp3 = Impiegato("Giuseppe", "Verdi", "MT003", 2150)
print()
print("----- IMPIEGATI -----")
print()
print("Impiegato (", imp1.matricola,"): ", imp1.nome, imp1.cognome, " - Stipendio base:", imp1.stipendio, " == Aumento del", imp1.aumenta_stipendio(10)) 
print("Impiegato (", imp2.matricola,"): ", imp2.nome, imp2.cognome, " - Stipendio base:", imp2.stipendio, " == Aumento del", imp2.aumenta_stipendio(5)) 
print("Impiegato (", imp3.matricola,"): ", imp3.nome, imp3.cognome, " - Stipendio base:", imp3.stipendio, " == Aumento del", imp3.aumenta_stipendio(9)) 
print()
