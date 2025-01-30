#eq 
import os

class Equazione():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if a == 0:
            print("IMPOSSIBILE!!!!!!!!!!!!!!!")
            return None

    def __calcola_delta(self,a,b,c):
        return b**2 - (4*a*c)
    
    def get_delta(self):
        return self.__calcola_delta(self.a, self.b, self.c)

eq = Equazione(2,10,22)
print(f"Delta: {eq.get_delta()} ")

