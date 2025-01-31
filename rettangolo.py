class Rettangolo():
	
	def __init__(self, base, altezza):
		self.base = base
		self.altezza = altezza
        
	def calcola_perimetro(self):
		return self.base*2 + self.altezza*2
        
	def calcola_area(self):
		return self.base * self.altezza
        
	

print()
base = 10
altezza = 12

rettangolo1 = Rettangolo(base, altezza)
print("Base:", base, "- Altezza:", altezza, "Perimetro:", rettangolo1.calcola_perimetro(), "- Area:", rettangolo1.calcola_area())

