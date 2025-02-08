#eq 
from math import sqrt

'''
Vertice	V = (−(Δ)/(4a),−(b)/(2a))
Fuoco	F = ((1−Δ)/(4a),−(b)/(2a))
'''

class Equazione():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def controlla_equazione(self):
        if self.a > 0: return True
        return False

    def __calcola_delta(self):
        return ((self.b**2) - (4*self.a*self.c))
    
    def calcola_equazione(self):
        delta = self.__calcola_delta()
        if delta >= 0:
            rad_delta = sqrt(delta)
            x1 = (-self.b - rad_delta) / (2*a)
            x2 = (-self.b + rad_delta) / (2*a)
            return (f"X1 = {x1} \nX2 = {x2}")
        return"Delta negativo!"
    
    def get_delta(self):
        return self.__calcola_delta()

    '''Fuoco F = ((1−Δ)/(4a),−(b)/(2a))'''
    def get_fuoco(self):
        #-b/2a, * 1-delta/a
        clc1 = (-self.b/(a*a))
        clc2 = ((1-self.__calcola_delta()) / (4*self.a))
        return [clc1, clc2]

    def get_vertice(self):
        v1= -self.b/(self.a*2)
        v2= (-self.__calcola_delta()) / (2*a)
        return f"v1={v1} v2={v2} v3= {v3}"

    def errore_a0(self):
        print()
        print("#####   \33[45m A = NN Capisci!!!!!!!!!!!!!!! \033[0m  ##### ")
        exit
        return None

# AVVIO PROGRAMMA #
if __name__ == "__main__":

    a = int(input("Inserisci il coefficente A: "))
    b = int(input("Inserisci il coefficente B: "))
    c = int(input("Inserisci il coefficente C: "))
    if a == None: a = 0
    if b == None: b = 0
    if c == None: b = 0



E2 = Equazione(a,b,c)

if a == 0:
    E2.errore_a0()
else:

    delta = E2.get_delta()
    print(f"Delta: {delta} ")
    print(E2.calcola_equazione())
    print()
    print(f"Il fuoco è: {E2.get_fuoco()}")
    print (f"Il vertice è: {E2.get_vertice()}")
    
