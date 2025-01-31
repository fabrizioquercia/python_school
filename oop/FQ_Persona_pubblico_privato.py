import os

os.system("cls")

'''
class Persona():
    
    def __init__(self, nome, cognome, stipendio):
        self.nome = nome
        self.cognome = cognome
        self.__stipendio = stipendio
    
    def get_nome(self):
        return f"{self.nome} {self.cognome}"
    
    def get_stipendio(self):
        return f"Stipendio: {self.__stipendio}"

    def aumenta_stipendio(self, soldi):
        self.__stipendio = self.__stipendio + soldi
        return self.__stipendio

persona = Persona("Mario", "Rossi", 19999)
print(persona.nome)
print(persona.get_nome())
print(persona.get_stipendio())
aumento = int(input("de quanto aumentamo? "))
persona.aumenta_stipendio(aumento)
print(persona.get_stipendio())
'''


'''
class GestioneStipendio():

    def __init__(self, nome, stipendio_base, ore_extra, bonus_annuo):
        self.nome = nome
        self.__stipendio_base = stipendio_base
        self.__ore_extra = ore_extra
        self.__bonus_anno = bonus_annuo
    
    def __calcola_extra(self):
        return self.__ore_extra*20
    
    def __calcola_bonus(self):
        return self.__bonus_anno / 12
        
    def calcola_stipendio_totale(self):
        extra = self.__calcola_extra()
        bonus = self.__calcola_bonus()
        stip = self.__stipendio_base + extra + bonus
        return int(stip)
    
    def get_bonus(self):
        return self.__calcola_bonus()
    def get_extra(self):
        return self.__calcola_extra()
        
    def get_stipendio_base(self):
        return self.__stipendio_base


stipendio = GestioneStipendio("Mario", 1400, 10, 130)
print(stipendio.nome)
print("Stipendio base", stipendio.get_stipendio_base())
print("Comprensivo totale:")
print(stipendio.calcola_stipendio_totale()) 
print("Di cui extra:", stipendio.get_extra())
print("Di cui bonus:", stipendio.get_bonus())
'''

class Calcolatrice():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __somma(self):
        return self.a + self.b
    
    def __sottrai(self):
        return self.a - self.b
    
    def __moltiplica(self):
        return self.a * self.b
    
    def moltiplica(self):
        return (self.a * self.b)
    
    def operazione_complessa(self):
        print(f"Operazione complessa di (a+b) (a-b): ({self.a}+{self.b}) ({self.a}-{self.b})")
        #print(f" a = {self.a} , b = {self.b}")
        somma = self.__somma()
        sottrai = self.__sottrai()
        moltiplica = self.__moltiplica()
        calcola = ((a+b) * (a-b))
        return f"Totale: {calcola}"


a = 10
b = 7

calcola = Calcolatrice(a,b)

print()
print(calcola.operazione_complessa())

