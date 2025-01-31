#eq 
from math import sqrt


class Equazione():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if a == 0:
            print()
            print("#####   \33[45m A = 0 ::::: EQUAZIONE IMPOSSIBILE!!!!!!!!!!!!!!! \033[0m  ##### ")
            return None

    def __calcola_delta(self):
        return self.b**2 - (4*self.a*self.c)
    
    def calcola_equazione(self):
        delta = self.__calcola_delta()
        if delta > 0:
            rad_delta = sqrt(delta)
            x1 = (-self.b - rad_delta) / 2*a
            x2 = (-self.b + rad_delta) / 2*a
            return (f"X1 = {x1} \nX2 = {x2}")
        return"Delta negativo!"

    
    def get_delta(self):
        return self.__calcola_delta()

    def get_fuoco(self):
        #-b/2a, * 1-delta/a
        clc1 = (-self.b/a*c)
        clc2 = (1-self.__calcola_delta() / self.a*4)
        return [clc1, clc2]




a = int(input("Inserisci il coefficente A: "))
b = int(input("Inserisci il coefficente B: "))
c = int(input("Inserisci il coefficente C: "))

E2 = Equazione(a,b,c)
delta = E2.get_delta()
print(f"Delta: {delta} ")
print(E2.calcola_equazione())
print()
print(f"Il fuoco è: {E2.get_fuoco()}")
print()
